# /usr/bin/python

import paramiko
#from paramiko import SSHClient, AutoAddPolicy, MissingHostKeyPolicy, Channel #extended_lib
from datetime import datetime
from getpass import getpass
import sys
import csv #To be moved
import time
import parser

class ConnectToHost:
    """This will be used to connect to a host"""

    def initiateConnection (uname, host, template):
        """This will open an SSH session to host and execute commands stated in template.
        : uname (str) - tacacs username to pass
        : host (arg) - A dictonary of host(s) where key is the hostname and value is the ip
        : template (arg) - text file consisting of commands to execute
        : RETURN (text file) -->output_file
        """
        standard_param = {
            'port' : 22,
            'username' : uname,
            'password' : getpass(),
            #'password' : '>zUoKvT3bes7c<YFtl',
            'look_for_keys' : False,
            'timeout' : None
        }
#CONNECT TO HOST VIA SSH
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(host, **standard_param)
        except Exception as e:
            print(e)
            print("Closing session...")
            sys.exit(1)

#INVOKE SHELL FROM TARGET HOST(S)
        connection = client.invoke_shell()
        output = str()  #INSTANTIATE OUTPUT VARIABLE
        try:
            with open('Logging for {} at {}.txt'.format(host,datetime.now()),'a+') as output_file:
                output_file.write("#"*10 + "Beginning of logging at {}".format(datetime.now())+"#"*10+"\n")
                with open(template,'r') as template_file:
                    for line in template_file:
                        command = line.strip()
                        try:
                        #    stdin, stdout, stderr = connection.exec_command(command)
                            connection.send(command + "\n")
                            time.sleep(5)
                            if connection.recv_ready() == True:
                        #        output = stdout.readlines()
                                output = connection.recv(9999).decode(encoding = 'utf')
                                #output_file.write(output + "\n")
                                print(output, file=output_file)
                            else:
                                time.sleep(3)
                                return output  #RETURN BY FUNCTION
                        except Exception as e:
                            print('Somthing went wrong with sending command on shell. See below')
                            print(e)
        except Exception as e:
            print(e)
        finally:
            client.close() #Always close ssh session

class main:
    """To be moved.. testing only"""
    inventory = input('Provide csv file to parse: ')
    template = input('Enter file name of template: ')

    dict_of_hosts = parser.csv_in_parser(inventory)
#create an output file
    UNAME = 'xsqk'
    print(len(dict_of_hosts))
    for k , v in dict_of_hosts.items():
        print('FROM {} SHELL {}'.format(k, datetime.now()))
        output_from_ssh = ConnectToHost.initiateConnection(UNAME, v, template)

    print(output_from_ssh)
    print('Executed successfully..')

if __name__ == '__main__':
    main()
