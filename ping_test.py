# /usr/bin/python

import os
import subprocess, platform  #standard library
from termcolor import colored #extended library

#ping_test.py

def ping_msg(func, host):
    """This will take 2 values: a function and and a host
    Return values will be an output message and a boolean
    The boolean is used to make a decision if the 'host' is unreachable
    """
    if func == True:
        return colored('reachability to {} OK!'.format(host), 'green') , True
    else:
        return colored('host {} unreachable!'.format(host), 'red'), False

#FUNCTION FOR SINGLE HOST/IP EXECUTION
def ping_func(host):
    """Return True if host(str) responds to a ping request.
    Only works for a singe host.
    """
    print("Checking reachability to host {}...".format(dev_name))
    try:
        pingstatus = subprocess.check_output('ping -c 1 {}'.format(dev_ip), shell=True)
    except Exception as e:
        return False
    return True

#FUNCTION FOR MULTIPLE HOSTS/IPs EXECUTION
def mping_func(dict):
    """This will conduct ping test to every host in a dictionary
    Takes an input of multiple hosts in a dictonary format
    """
    new_dict = {}  #VALIDATION: will remove unreachable hosts
    for k, v in dict.items():
        try:
            print('Checking connectivity to {}...'.format(k))
            pingstatus = subprocess.check_output('ping -c 1 {}'.format(v), shell=True)
            print(colored('Reachability to {} is OK!'.format(k), 'green'))
            flag = True
        except Exception as e:
            flag = False
            print(colored('host {} unreachable!'.format(k), 'red'))
        if flag == True:
            new_dict[k] = v
    return new_dict
