#!/usr/bin/env python

PATH = []

def pwd(path):
    if len(PATH)==0:
        print '/'
    else:
        print '/'+'/'.join(PATH)+'/'
def cd(cmd):
    global PATH
    dirs = cmd.split(' ')[1]
    if dirs[0]=='/': PATH = []
    for d in dirs.split('/'):
        if d =='..':
            PATH.pop()
        elif len(d)>0:
            PATH.append(d)
    pass
    

cmds = input()
while cmds >0:
    cmds -=1
    cmd = raw_input()
    if cmd =='pwd':
        pwd(PATH)
    else: cd(cmd)