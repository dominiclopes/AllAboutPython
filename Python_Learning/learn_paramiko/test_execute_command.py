import time

from learn_paramiko.ssh_helper import SshHelper

helper = SshHelper("10.10.107.183", "root", "protegrity")
helper.connect(timeout=None, banner_timeout=None, auth_timeout=None)
helper.create_sftp_session()

time.sleep(2)

# Printing the variables that say the connection is active
print("SFTP active = ", not helper.sftp_shell.sock.closed)
print("SSH  active = ", helper.ssh_client._transport.active)

# Example of Command timeout
helper.execute_command_on_remote("sleep 2; echo 'Done'", 1)
# print(helper.sftp_shell.listdir())
#
# # Trying the re-logging thingy
# # helper.execute_command_on_remote("shutdown -r now")
# # helper.execute_command_on_remote("echo 'Did that work ?'")
# # print(helper.listdir())
#
#
# # Printing the variables that say the connection is active
# print("SFTP active = ", not helper.sftp_shell.sock.closed)
# print("SSH  active = ", helper.ssh_client._transport.active)

# Close the ssh session once you are done
helper.disconnect()
