#!/usr/bin/env python

import paramiko
import time
from getpass import getpass

ip_addr = '50.76.53.27'
username = 'pyclass'
password = getpass()
#password = '88newclass'

port = 8022

remote_conn_pre = paramiko.SSHClient()
#remote_conn_pre

remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#rempte_conn_pre.load_system_host_keys()


remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)


#stdin, stdout, stderr = remote_conn_pre.exec_command('show ip int brief\n')
#print stdout.read()

remote_conn = remote_conn_pre.invoke_shell()

output = remote_conn.recv(65535)

outp = remote_conn.send("show ip int brief\n")
time.sleep(1)

output = remote_conn.recv(65535)
remote_conn.settimeout(6.0)
remote_conn.gettimeout()

print output

