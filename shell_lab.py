#!/usr/bin/python3
# Ruben Bustamante, OS, 02/26/2021

import os, sys, re
def exec_command(command, child):
    
    if child == 0:
        commands = command.split()
        for dir in re.split(":", os.environ['PATH']):
            possbile_path = "%s/%s" % (dir, commands[0])
            try:
                os.execve(possbile_path, commands, os.environ)
            except:
                pass

        
def redirc(command,child):
    commands = command.split()
    if child == 0:
        os.close(STDOUT)
        os.open(command[1].strip(), os.O_CREAT | os.O_WRONLY)
        os.set_inheritable(STDOUT, True)
        for dir in re.split(":", os.environ['PATH']):
            possbile_path = "%s/%s" % (dir, commands[0])
            try:
               os.execve(possbile_path, commands, os.environ)
            except:
                pass
def pipes(command, child):
    commands = os.pipe()
    if child == 0:
        os.dup(commands[0]. STDIN)
        os.close(commands[0])
        os.close(commands[-1])
        os.execv(commands[0], commands)
        
        
def main():
    command = ' '
    while(1):
        
        command = input(" $$$ ")

        if command== 'cd':
            child = os.fork()
            os.chdir(exec_command(command, child))
        if command != 'exit':
            child = os.fork()
            exec_command(command, child)
            os.wait()
        if command == '<' or command =='>':
            child =os.fork()
            redirc(command, child)
            os.wait()
        if command == '|':
            child = os.fork()
            pipes(command,child)
            os.wait()
        else:
            break
    sys.exit(1)
main()
