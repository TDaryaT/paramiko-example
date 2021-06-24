import paramiko
import sys
    
# get public IP address from command line
try:
    hostname = sys.argv[1]
except IndexError:
    print("Enter public IP address")
    sys.exit(1)
# standart name of user
myuser = 'ec2-user'
# path for private key
key = "d:\\Users\\user\\Downloads\\test.pem"
# list of commands
commands = ["ls", "sudo shutdown -h now"]

k = paramiko.RSAKey.from_private_key_file(key)
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("connecting....")

try:
    # connect
    c.connect(hostname=hostname, username=myuser, pkey=k)
except TimeoutError:
    print("TimeoutError: check host/username/private key or maybe your instance is alrady shutdown")
    sys.exit(1)

print("connected!")
for command in commands:
    print("Executing {}".format(command))
    stdin, stdout, stderr = c.exec_command(command)

    # printing
    output = ''
    outputErr = ''
    for line in stdout.readlines():
        output += line

    for line in stderr.readlines():
        outputErr += line

    if output:
        print(output)
    else:
        print("There was no output for this command")
    if outputErr:
        print(outputErr)
c.close()
