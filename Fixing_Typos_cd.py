#!/usr/bin/env python
#http://codeforces.com/problemset/problem/363/C
window = list()
def check_window():
    global window
    if window[0] == window[1]== window[2] or (window[0] == window[1] and window[2]==window[3]):
        return True
    return False

s = list(raw_input())

i =3
L = len(s)
window.append(s[0])
window.append(s[1])
window.append(s[2])
window.append(s[3])
while i < L:
    if check_window():
        del s[i-1]
    window.pop(0)

print s
