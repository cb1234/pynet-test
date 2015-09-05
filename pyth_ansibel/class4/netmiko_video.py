#!/usr/bin/env python


from netmiko import ConnectHandler
from getpass import getpass
password = getpass()


pynet1 = { 
    'device_type' : 'cisco_ios',
    'ip' : '50.76.53.27',
        'username' : 'pyclass',
        'password' : password
}



pynet2 = { 
    'device_type' : 'cisco_ios',
    'ip' : '50.76.53.27',
        'username' : 'pyclass',
        'password' : password,
    'port'     : 8022
}

juniper_srx = {
    'device_type' : 'juniper',
    'ip': '50.76.53.27',
    'username': 'pyclass',
    'password': password,
    'secret': '',
    'port': 9822,
}


pynet_rtr1 = ConnectHandler(**pynet1)
pynet_rtr2 = ConnectHandler(**pynet2)
srx = ConnectHandler(**juniper_srx)

dir(pynet_rtr1)
dir(pynet_rtr2)
dir(srx)



pynet_rtr1
pynet_rtr1.find_prompt()
pynet_rtr1.config_mode()
pynet_rtr1.check_config_mode()
pynet_rtr1.exit_config_mode()
outp = pynet_rtr1.send_command("show version")
print outp

outp += pynet_rtr1.send_command("show ip int brief")
print outp



pynet_rtr1.send_command("show run | i logg")


config_commands = [ 'logging buffered 19999']
outp += pynet_rtr1.send_config_set(config_commands)

print outp

pynet_rtr1.send_command("show run | i logg")

