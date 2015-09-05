#!/usr/bin/env python
'''
Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx
'''

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from test_devices import pynet1, pynet2, juniper_srx


def main():
    '''
    Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2 and juniper-srx'
    '''

    ip_addr = raw_input("Enter IP Address: ")
    password = getpass()
    
    #Get connection parameters setup correctly
    for a_dict in (pynet1, pynet2, juniper_srx):
        a_dict['ip'] = ip_addr
        a_dict['password'] = password
        a_dict['verbose'] = False

    
    print "\nStart time: "  +str(datetime.now())

    for rtr in (pynet1, pynet2, juniper_srx):
        rtr = ConnectHandler(**rtr)
        output = rtr.send_command("show arp")
        print 
        print '#' * 80
        print "Device: {}:{}".format(rtr.ip, rtr.port)
        print
        print output
        print '#' * 80
        print

    print "\nEnd time: " + str(datetime.now())


if __name__ == "__main__":
    main()

