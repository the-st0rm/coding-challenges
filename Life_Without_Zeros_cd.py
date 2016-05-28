#!/usr/bin/env python

#http://codeforces.com/problemset/problem/75/A

num1 = raw_input();num2= raw_input()
res = int(num1)+int(num2)
res = str(res).replace('0','');num1=num1.replace('0','');num2=num2.replace('0','')
print 'YES' if int(num1)+int(num2)==int(res) else 'NO'