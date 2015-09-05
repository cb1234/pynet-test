#!/usr/bin/env python

import paramiko
import time
from getpass import getpass
MAX_BUFFER = 65535

def clear_buffer(remote_conn):
    '''
    Clear any data in the receive buffer
    '''
    if remote_conn.recv_ready():
        return remote_conn.recv(MAX_BUFFER)

def disable_paging(remote_conn):
    '''
    disable output paging (i.e. ...More...)
    '''
    send_command(remote_conn, cmd='terminal length 0')

def send_command(remote_conn, cmd='', delay=1):
    if cmd != '':
        cmd = cmd.strip()
    remote_conn.send(cmd + '\n')
    time.sleep(delay)
    if remote_conn.recv_ready():
            return remote_conn.recv(MAX_BUFFER)
    else:
            return ''
def main():
    '''
    Use Paramiko to change logging buffered config
    '''

    ip_addr = '50.76.53.27'
    username = 'pyclass'
    password = '88newclass'
    #password = getpass()
    port = 8022

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)
    remote_conn = remote_conn_pre.invoke_shell()
    time.sleep(1)
    clear_buffer(remote_conn)
    disable_paging(remote_conn) 
    
    send_command(remote_conn, cmd="configure t")
    send_command(remote_conn, cmd="logging buffered 19999")
    send_command(remote_conn, cmd="end")
   
    output = send_command(remote_conn, cmd="show run | inc logging")
    print '\n>>>>>'
    print output
    print '>>>>>\n'


if __name__ == "__main__":
    main()

