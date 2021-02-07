#!/usr/bin/python3
# Ruben Bustamante, OS, 02/26/2021

import os, sys, re
def exec_command(command):
    child = os.fork()
    commands = command.split()
    if child == 0:
        for dir in re.split(":", os.environ['PATH']):
            possbile_path = "%s/%s" % (dir, commands[0])
            try:
                os.execve(possbile_path, commands, os.environ)
            except:
                pass
    else:
        os.waitpid(child,0)
        child2 = os.fork()
    if commands =='>' or child2 ==0:
        print('b', commands)
        child2 =os.fork()
        os.open(commands[-1], os.O_CREAT | os.O_WRONLY)
        os.set_inheritable(1,True)
        for dir in re.split(":", os.environ['PATH']):
            possbile_path = "%s/%s" % (dir, commands[0])
            try:
                os.execve(possbile_path, commands, os.environ)
            except:
                pass
    else:
        os.waitpid(child2,0)

                       
def main():
    command = ''
    while(1):
        command = input(" $$$ ")
        if command == 'exit':
            break
        else:
            exec_command(command)
    
    sys.exit(1)
main()
