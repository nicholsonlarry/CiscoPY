import netmiko
from netmiko import ConnectHandler
from getpass import getpass

USERNAME = input("What is your Username?")
SECRET = getpass()  
#  Open file with list of switches
f = open ("license.txt")
print('Loading "license.txt" file')

for line in f:
    DEVICE = line.strip()
    print("Connecting to:", DEVICE)
    device = ConnectHandler(device_type="cisco_ios", ip=DEVICE, username=USERNAME, password=SECRET)
    output1 = device.send_command("license smart register idtoken XXXXXXXXXXXX")
    save_file = open("smart_lic"+str(DEVICE)+".txt","w")
    save_file.write(output1)
    save_file.close()
    device.disconnect()
    print(str(DEVICE)+" Complete")
    # need to add else if or something to handle time out errors or bad username/password return
print("Script Complete")
