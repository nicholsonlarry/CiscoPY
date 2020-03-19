import netmiko
from netmiko import ConnectHandler
from getpass import getpass

USERNAME = input("What is your Username?")
SECRET = getpass()  
#  Open file with list of switches
f = open ("mode.txt")
print('Loading "mode.txt" file')
save_file = open("show mode.txt","w")
for line in f:
    DEVICE = line.strip()
    print("Connecting to:", DEVICE)
    device = ConnectHandler(device_type="cisco_ios", ip=DEVICE, username=USERNAME, password=SECRET)
    output1 = device.send_command("show ver | be Mode")
    #save_file = open("show .txt","w")
    #save_file = open("show mode.txt","w")
    save_file.write(DEVICE)
    save_file.write(output1)
    #save_file.close()
    #moving file close to end
    device.disconnect()
    print(str(DEVICE)+"Complete")
    # need to add else if or something to handle time out errors or bad username/password return
save_file.close()
print("Script Complete")
