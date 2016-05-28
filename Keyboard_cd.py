#!/usr/bin/env python
#http://codeforces.com/problemset/problem/474/A
KEYBOARD = "qwertyuiopasdfghjkl;zxcvbnm,./"
Direction = raw_input()
if Direction == 'R':
    shift = -1
else:
    shift = 1
String = raw_input()
output = list()
for s in String:
    output.append(KEYBOARD[KEYBOARD.find(s)+shift])
print ''.join(output)
