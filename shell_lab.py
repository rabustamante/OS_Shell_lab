#!/usr/bin/python3
# Ruben Bustamante, OS, 02/26/2021
import os, sys, re
def exec_command(command):
    child = os.fork()
    if child == 0 and command != 'exit':
        commands = command.split()
        print(commands)
        for dir in re.split(":", os.environ['PATH']):
            possbile_path = "%s/%s" % (dir, commands[0])
            try:
                os.execve(possbile_path, commands, os.environ)
            except:
                pass


def main():
    command = ''
    while(1):
        command = input(" $$$ ")
        if command != 'exit':
            exec_command(command)
        else:
            break
main()
