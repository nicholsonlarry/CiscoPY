import netmiko
from netmiko import ConnectHandler
from getpass import getpass

USERNAME = input("What is your Username?")
SECRET = getpass()  
COMMAND = input("Enter command Device#")
#  Open file with list of switches
f = open ("devices.txt")
print('Loading "devices.txt" file')

for line in f:
    DEVICE = line.strip()
    print("Connecting to:", DEVICE)
    device = ConnectHandler(device_type="cisco_ios", ip=DEVICE, username=USERNAME, password=SECRET)
    output1 = device.send_command(COMMAND)
    save_file = open(COMMAND+str(DEVICE)+".txt","w")
    save_file.write(output1)
    save_file.close()
    device.disconnect()
    print(str(DEVICE)+"Complete")
    #need to build error handling to expect
    #netmiko.ssh_exception.NetmikoTimeoutException: Connection to device timed-out: cisco_ios 172.19.0.1:22
print("Script Complete")
