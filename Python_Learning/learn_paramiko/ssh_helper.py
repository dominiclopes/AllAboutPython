import socket

import paramiko
import logging
import time
import sys


class SshHelper(object):

    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.ssh_shell = None  # for interactive session
        self.sftp_shell = None # for sftp

        # Set the logging
        log_format = "[%(name)-20s] [%(levelname)-8s] [%(asctime)s] %(message)s"
        logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    def connect(self, timeout=None, banner_timeout=None, auth_timeout=None):
        logging.info("Logging into {}".format(self.hostname))
        self.ssh_client.connect(hostname=self.hostname, username=self.username, password=self.password,
                                look_for_keys=False, timeout=timeout, banner_timeout=banner_timeout,
                                auth_timeout=auth_timeout)

    def re_login(self):
        counter = 0
        while not getattr(self.ssh_client, "_transport").active:
            try:
                self.connect()
            except paramiko.ssh_exception.SSHException as e:
                logging.error(exc_info=e, msg="Wow")
            except TimeoutError:
                logging.error("Timeout Connecting {}".format(self.hostname))
                time.sleep(10)
            except Exception as e:
                logging.error(exc_info=e, msg="Why on earth ?")
            else:
                self.create_sftp_session()
            counter += 1
            logging.info("-" * 50)
        logging.info("Logged in at {} attempt, time required = {} sec".format(counter, (counter-1)*10))

    def disconnect(self):
        self.sftp_shell.close()
        self.ssh_client.close()

    def create_sftp_session(self):
        try:
            self.sftp_shell = self.ssh_client.open_sftp()
        except Exception as e:
            logging.error(exc_info=e, msg="What is it?")

    def execute_command_on_remote(self, command, timeout=None):
        try:
            logging.info("Executing command: {}".format(command))
            start = time.time()
            output_tuple = self.ssh_client.exec_command(command=command, timeout=timeout)
            logging.info("Time taken to execute the command = {}".format(time.time()-start))
            self.print_command_execution_output(output_tuple)
        except socket.timeout as e:
            logging.error("Increase the timeout for the command execution", exc_info=e)
        except paramiko.ssh_exception.SSHException:
            self.re_login()
            self.execute_command_on_remote(command, timeout)
        except Exception as e:
            logging.error(exc_info=e, msg="What is it?")

    @staticmethod
    def print_command_execution_output(command_execution_output_tuple):
        output = command_execution_output_tuple[1].readlines()
        output += command_execution_output_tuple[2].readlines()
        logging.info("Command Output: \n{}".format(" ".join(output)))

    def create_interactive_shell(self):
        self.ssh_shell = self.ssh_client.invoke_shell(term='vt100', width=1000, height=1000)

    def execute_command_interactively(self, command):
        self.ssh_shell.send(command)
        self.print_command_output_execute_using_interactive_shell()

    def print_command_output_execute_using_interactive_shell(self):
        self.ssh_shell.recv_ready()
        while True:
            try:
                logging.info(self.ssh_shell.recv(65535).decode("utf-8", "ignore"))
            except Exception:
                break

    def listdir(self):
        try:
            self.sftp_shell.listdir()
        except OSError:
            logging.error("Socket is closed, Re-creating it")
        except Exception as e:
            logging.error("This is an unhandled exception")
            raise e
