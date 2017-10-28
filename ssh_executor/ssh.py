#!/usr/bin/env python

import argparse,paramiko,sys
from termcolor import colored

def parser():
    parser = argparse.ArgumentParser(description='SSH Command Executor')
    parser.add_argument('-a','--address', help='Remote Host Address', required=True)
    parser.add_argument('-c','--command', help='Command To Execute, Wrap in quotes(\'\') for commands with multiple fields.', required=True)
    parser.add_argument('-k','--key', help='Path To Key', required=True)
    parser.add_argument('-u','--user', help='Remote User', required=True)
    return parser.parse_args()

def connect(address,user,key,command):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    try:
        ssh.connect((address),username=(user),key_filename=(key))
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
        return ssh_stdout.read()
    except paramiko.ssh_exception.SSHException:
        print colored('Unable to connect.', 'red')
        sys.exit(1)

def main():
    args = parser()
    address = args.address
    command = args.command
    key = args.key
    user = args.user
    print colored(connect(address,user,key,command),'green')

if __name__ == '__main__':
    main()
