# /usr/bin/python

import subprocess, platform #standard lib
from datetime import datetime   #standard lib
import parser  #user package
import ConnectToHost
import termcolor

class ssh_host:
    """Instantiate a username object by passing it here."""

    def __init__(self, uname):
        self.uname = uname

    def setUname(self, uname):
        if len(uname) == 4 && uname.isAlpha():
            self.uname = uname
        else:
            print('Input not accapted. Please enter your CAI: ')

    def setTemplate(self, template):
        if type(template) is list:
            self.template = template
        else:
            print('Template not yet valid.')

    def getUname(self):
        return uname

    def getTemplate(self):
        return template

class main:
    """This is the main class for Project002 that will call the ff packages
    : parser.py --> to parse input inventory in csv to dictionary
    : ConnectToHost --> paramiko SSHClient to initiate ssh session to hosts
    """
#ASK THE USER FOR THE INVENTORY OF HOSTS
    inventory = input('Please provide inventory of hosts: ')
    dict_of_hosts = parser.csv_in_parser(inventory)
#ASK THE USER FOR TEMPLATE TO PUSH TO DEVICES
    template = input('Please enter template reference for hosts: ')
#ASK FOR THE USERNAME TO USE
    UNAME = input('Please provide username: ')
#CREATE OBJECT FOR USERNAME; ensures that username is valid
    u1 = ssh_host()
    u1.setUname(UNAME.lower().strip())
    u1.setTemplate(template)
#ITERATE ON THE DICTIONARY OF HOSTS
    count = 0
    for k,v in dict_of_hosts.items():
        print('Accessing {}...'.format(k))
        ConnectToHost.initiateConnection(u1.getUname(), v, u1.getTemplate())
        count += 1
        print(colored('Successfully executed {} host(s)'.format(count), 'green')
    print(colored("#"*10 + "THIS ENDS THE PROGRAM. YOU MAY NOW CHECK THE LOG FILES." + "#"*10), 'blue')
    

if __name__ == '__main__':
    main()
