#!/usr/bin/env python
'''
Connect to Juniper device using PyEZ. Display device facts.
'''

from jnpr.junos import Device
from getpass import getpass
from pprint import pprint


def main():
    '''
    Connect to Juniper device using PyEZ. Display device facts.
    '''
    #pwd = getpass()
    pwd = '88newclass' 
   # ip_addr = raw_input("Enter Juniper SRX IP: ")
    ip_addr = '50.76.53.27' 
    ip_addr = ip_addr.strip()

    juniper_srx = {
        "host": ip_addr,
        "user": "pyclass",
        "password": pwd
    }

    print "\n\nConnecting to Juniper SRX...\n"
    a_device = Device(**juniper_srx)
    a_device.open()
    pprint(a_device.facts)
    print


if __name__ == "__main__":
    main()
