#!/usr/bin/env python
#http://codeforces.com/problemset/problem/158/C


def rem_last_dir(path):
    path = path[:-1]
    path = path.rsplit('/',1)[0]
    return path+'/'


cmds = input()
PATH = '/'
while cmds>0:
    cmd = raw_input()
    if cmd=='pwd':
        print PATH
    else:
        cmd=cmd.split(' ')
        path = cmd[1]
        if path=='/':
            PATH = '/'
        elif path[0]=='/':
            PATH = '/'
        
        for p in path.split('/'):
            if p =='..':
                PATH = rem_last_dir(PATH)
            elif p!='':
                PATH =PATH+p+'/'
    cmds-=1
