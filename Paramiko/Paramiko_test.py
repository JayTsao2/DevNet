import paramiko

router_ip = "192.168.56.101"
router_username = "cisco"
router_password = "cisco123!"

ssh = paramiko.SSHClient()

# Load SSH host keys.
ssh.load_system_host_keys()
# Add SSH host key automatically if needed.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Connect to router using username/password authentication.
ssh.connect(router_ip, 
            username=router_username, 
            password=router_password,
            look_for_keys=False )

# Run command.
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("show ip interface brief")

output = ssh_stdout.readlines()
# Close connection.
ssh.close()

print(output)
# Analyze show ip route output

#for line in output:
#    if "0.0.0.0/0" in line:
#        print("Found default route:")
#        print(line)
