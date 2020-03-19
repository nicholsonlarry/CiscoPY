import netmiko
from netmiko import ConnectHandler
from getpass import getpass

USERNAME = input("What is your Username?")
SECRET = getpass()  
#  Open file with list of switches
f = open ("controllers.txt")

for line in f:
    # need to fix, doesn't like (line)
    #print ("Getting running config") + str(line)
    #
    #left over from manually asking IP address
    #controller = input("What is IP address of the WLC?")
    CONTROLLER = line.strip()

    device = ConnectHandler(device_type="cisco_wlc_ssh", ip=CONTROLLER, username=USERNAME, password=SECRET)
    output1 = device.send_command("config paging disable")
    output2 = device.send_command("show running-config")
    save_file = open("Runconfig"+str(CONTROLLER)+".txt","w")
    save_file.write(output2)
    save_file.close()
    device.disconnect()
print("complete")
