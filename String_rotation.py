#!/usr/bin/env python

def is_rotation(S1, S2):
    if len(S1) != len(S2):
        return False
    S1 = S1+S1
    if ''.join(S1).find(''.join(S2)) > 0:
        return True
    return False



def main():
    S1= list(raw_input())
    S2 = list(raw_input())
    if is_rotation(S1, S2):
        print 'TRUE'
    else:
        print 'FALSE'
    

if __name__ == '__main__':
    main()