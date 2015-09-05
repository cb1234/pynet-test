#!/usr/bin/env python

import paramiko
import time

MAX_BUFFER = 65535

def clear_buffer(remote_conn):
    '''
    Clear any data in the receive buffer
    '''
    #send_command(remote_conn, cmd='', delay=1)
    if remote_conn.recv_ready():
       return remote_conn.recv(MAX_BUFFER)

def disable_paging(remote_conn, cmd='terminal length 0'):
    '''
    Disable paging ( .ie. --more--)

    '''
    send_command(remote_conn, cmd ='terminal length 0')   

def send_command(remote_conn, cmd ='', delay =1):
    '''
    Send a command down the ssh channel. Retrieve and return the output
    '''
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
    Use paramiko to send entire show version output.
    '''

    ip_addr = '50.76.53.27'
    username = 'pyclass'
    password = '88newclass'
    port = 8022

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)
    remote_conn = remote_conn_pre.invoke_shell()
    time.sleep(1)
    clear_buffer(remote_conn)
    disable_paging(remote_conn)
    output = send_command(remote_conn, cmd='show version')
    print '\n>>>>>'
    print output
    print '>>>>>\n'
if __name__ == "__main__":
    main()

