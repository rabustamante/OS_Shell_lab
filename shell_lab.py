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
    commands = command.split()
    commands[0] = os.pipe()
    commands[2] = os.pipe()
    for f in (commands[0], commands[2]):
        os.set_inheritable(1,True)
    os.close(1)
    os.dup(command[2])
    for df in (commands[0], commands[2]):
           os.close(fd)
    print(df)
    
        
def main():
    command = ' '
    while(1):
        command = input(" $$$ ")
        commands = command.split()
        if commands[0]== 'cd':
            child = os.fork()
            os.chdir(exec_command(command, child))
        if commands[0]!='exit':
            child = os.fork()
            exec_command(command, child)
            os.wait()
        if commands[0] == '<' or commands[0] =='>':
            child =os.fork()
            redirc(command, child)
            os.wait()
        if commands[1] == '|':
            child = os.fork()
            pipes(command,child)
            os.wait()
        if commands[0] == 'exit':
            break
            
        sys.exit(1)
main()
