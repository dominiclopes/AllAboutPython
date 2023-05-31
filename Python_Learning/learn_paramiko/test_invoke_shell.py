import time

import paramiko

def print_output(stdout, stderr):
    if stdout:
        print("Stdout: \n" + "".join(stdout.readlines()))
    if stdout:
        print("Stderr: \n" + "".join(stderr.readlines()))

ssh_session = paramiko.SSHClient()
ssh_session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh_session.connect(hostname="10.10.109.214", username="root", password="root1234", look_for_keys=False,
                    allow_agent=False, banner_timeout=10)


# ssh_shell = ssh_session.invoke_shell(term='vt100', width=1000, height=1000)
# ssh_shell.settimeout(6) # if no data could be sent before the timeout set by settimeout.
# a = ssh_shell.send("admin\n")
# ssh_shell.send("admin123\n")
# print(a)
# print(ssh_shell.recv_ready())
#
# time.sleep(10)
# while True:
#     try:
#         print(ssh_shell.recv(65535).decode("utf-8", "ignore"))
#     except Exception as e:
#         print(e)
#         break