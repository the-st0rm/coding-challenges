

def anagrams2(S1, S2):
    if len(S1) != len(S2):
        return False
        
    S1.sort()
    S2.sort()
    for i in xrange(len(S1)):
        if S1[i] != S2[i]:
            return False
    return True

def anagrams2(S1, S2):
    if len(S1) != len(S2):
        return False
    
    occurnces = [0]*256
    for i in xrange(len(S1)):
        occurnces[ord(S1[i])]+=1
        occurnces[ord(S2[i])]-=1
    for i in occurnces:
        if i > 0:
            return False
    return True

def main():
    S1 = list(raw_input())
    S2 = list(raw_input())
    if anagrams2(S1, S2):
        print "YES"
    else:
        print "NO"



if __name__ == '__main__':
    main()