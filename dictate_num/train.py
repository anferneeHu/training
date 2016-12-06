import os
import sys
import pyttsx
import random
from data import *


EXIT_TAG = 'n'

class CTrain(object):
    def __init__(self):
        self._eng = pyttsx.init()
    
    def pre(self):
        print "*"*10,"DICTATE NUMBER TRAING", "*"*10
        name = raw_input("Please enter your name: ")
        data = CData(name).load()
        if data is not None:
            self._data = data
            print "See you again ", name, ", your score is followings:"
            self._data.showSt()
            self._data.showDaySt()
        else:
            self._data = CData(name)
            print "Welcome new challenger", name
        
        print "You will start on level", self._data.level
        return

    def aft(self, doCnt):
        self._data.save()
        print "Bye %s, finish [%3d] , your score is followings:"%(self._data.name, doCnt)
        self._data.showDetail(doCnt)
        return

    def run(self):
        IsCon = True
        idx = 1
        while IsCon:
            lvl = self._data.level
            print "\n[%3d]"%( idx,), " now level", lvl,", Please listening..."
            nums = self.genNum(lvl)
            self.readNum(nums)
            d = raw_input("enter what you heard(n for exit): ")
            if d.lower().find(EXIT_TAG) >= 0:
                IsCon = False
                break
            ans,lvl = self._data.score(d, nums)
            if ans:
                print "SUCC"
            else:
                print "FAIL: ", nums
            idx += 1

        return idx-1


    def genNum(self, lvl):
        s = ""
        for _ in range(lvl):
            d = random.randint(0,9)
            s += str(d)
        return s

    def readNum(self, nums):
        for d in nums:
            self._eng.say(d)
        self._eng.runAndWait()
        return
   

def main():
    train = CTrain()
    train.pre()
    doCnt = train.run()
    train.aft(doCnt)


if __name__ == "__main__":
    main()
