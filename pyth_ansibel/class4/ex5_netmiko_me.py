#!/usr/bin/env python
'''
Using Netmiko enter into configuration mode on a network device.
'''

from getpass import getpass
from netmiko import ConnectHandler
from test_devices import pynet1, pynet2, juniper_srx



#pynet2 = {
#    'device_type' : 'cisco_ios',
#    'ip' : '50.76.53.27',
#        'username' : 'pyclass',
#        'password' : '88newclass',
#    'port'     : 8022
#}

def main():
    '''
    Using Netmiko enter into configuration mode on a network device.
    Verify that you are currently in configuration mode.
    '''

    ip_addr = raw_input("Enter IP Address: ")
    password = getpass()
    
    for a_dict in (pynet1, pynet2, juniper_srx):
        a_dict['ip'] = ip_addr
        a_dict['password'] = password

    pynet_rtr2 = ConnectHandler(**pynet2)

    pynet_rtr2.config_mode()

    print "\n>>>>"
    print "Checking pynet-rtr2 is in configuration mode"
    print "Config mode check: {}".format(pynet_rtr2.check_config_mode())
    print "Current prompt: {}".format(pynet_rtr2.find_prompt())
    print ">>>>\n"



if __name__ == "__main__":
    main()

