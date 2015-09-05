#!/usr/bin/env python
'''
Use Netmiko to change the logging buffer size on pynet-rtr2.
'''

from getpass import getpass
from netmiko import ConnectHandler
from test_devices import pynet1, pynet2, juniper_srx





def main():
    '''
    Use Netmiko to change the logging buffer size on pynet-rtr2.
    '''
    
    ip_addr = raw_input("Enter IP Address: ")
    password = getpass()
    
    #Get connection parameters setup correctly
    for a_dict in (pynet1, pynet2, juniper_srx):
        a_dict['ip'] = ip_addr
        a_dict['password'] = password
        a_dict['verbose'] = False


    pynet_rtr2 = ConnectHandler(**pynet2)

    config_commands = [ 'logging buffered 19999']
    pynet_rtr2.send_config_set(config_commands)

    output = pynet_rtr2.send_command("show run | inc logging buffer")

    print 
    print '#' * 80
    print "Device: {}:{}".format(pynet_rtr2.ip, pynet_rtr2.port)
    print
    print output
    print '#' * 80
    print



if __name__ == "__main__":
    main()

