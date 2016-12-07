import os
import sys
import pickle
import time
from collections import OrderedDict

DEFAULT_NAME = 'anonymous'
DEFAULT_LEVEL = 3
DEFAULT_TRYCNT = 3
DEFAULT_SAVEPATH='./save'
PRE_SAVETAG='savefile_'


#------------------------------------------------
class CRcd(object):
    def __init__(self, usr_data, rlt):
            self._time = time.time()
            self._usr = usr_data
            self._rlt = rlt
            self._level = len(rlt)
            self._ans = self.chk()
    def chk(self):
        if self._usr == self._rlt:
            return True
        else:
            return False

    #------------- property -----------------
    @property
    def ans(self):
        return self._ans

    @property
    def time(self):
        return self._time

    @property
    def usr(self):
        return self._usr

    @property
    def rlt(self):
        return self._rlt

    @property
    def level(self):
        return self._level

    #------------- save/load -----------------
    def toStr(self):
        strs = ''
        strs += "[ "+str(time.ctime(self._time))+" ] " 
        if self._ans:
            strs += "SUCC: [%3d] -- %s"%(len(self._rlt), self._rlt)
        else:
            strs += "FAIL: [%3d] -- %s : %s"%(len(self._rlt), self._rlt, self._usr)
        return strs



#------------------------------------------------

class CData(object):
    def __init__(self, name=DEFAULT_NAME):
        self._name = name
        self._level = DEFAULT_LEVEL
        self._trycnt = DEFAULT_TRYCNT
        self._history = OrderedDict()
        self._nowsucc = 0
        self._nowfail = 0
    #------------- property -----------------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, nm):
        self._name = nm

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, lv):
        self._level = lv

    @property
    def trycnt(self):
        return self._trycnt

    @trycnt.setter
    def trycnt(self, cnt):
        self._trycnt = cnt


    #------------- save/load -----------------
    def save(self, filepath = DEFAULT_SAVEPATH):
        if not os.path.exists(filepath):
            print "save path doesn't exist.", filepath
            return False
        dump_file = os.path.join(filepath, PRE_SAVETAG+self._name)
        pickle.dump(self, open(dump_file, 'w'))
        return True

    def load(self, filepath=DEFAULT_SAVEPATH):
        dump_file = os.path.join(filepath, PRE_SAVETAG+self._name)
        if not os.path.exists(dump_file):
            print "load file doesn't exist.", dump_file
            return None
        else:
            data = pickle.load(open(dump_file , 'r'))
            return data

    #------------- record ----------------
    def score(self, usr_data, rlt):
        rcd  = CRcd(usr_data, rlt)
        self.addHistory(rcd)
        ans = rcd.ans
        return (ans, self.mvLevel(ans))

    def addHistory(self, rcd):
        self._history[rcd.time] = rcd
        return

    def mvLevel(self, ans):
        if ans:
            self._nowsucc +=1
            if self._nowsucc >= self._trycnt:
                self._level += 1
                self._nowsucc = 0
                self._nowfail = 0
            else:
                pass
        else:
            self._nowsucc -= 1
            if self._nowsucc <= (-1) * self._trycnt:
                self._level -= 1
                if self._level <1:
                    self._level = 1
                self._nowsucc = 0
            else:
                pass
        return self._level
    
    #------------- cals ----------------
    def getMaxLevel(self):
        maxlv = 0
        for _, v in self._history.items():
            if v.level > maxlv and v.ans:
                maxlv = v.level
        return maxlv

    def getStat(self):
        stat = OrderedDict()
        for _, v in self._history.items():
            lvl = v.level
            ans = v.ans
            if lvl not in stat:
                stat[lvl] = [0,0]
            if ans:
                stat[lvl][0] += 1
            else:
                stat[lvl][1] += 1
        
        strs = ''
        for k, v in stat.items():
            strs += '[%3d] SUCC: %5d, FAIL: %5d\n'%(k, v[0],v[1])
        return strs


    def getDayStat(self):
        stat = OrderedDict()
        for k, v in self._history.items():
            lvl = v.level
            ans = v.ans
            day = time.strftime( "%Y-%m-%d", time.localtime( k ) )
            if day not in stat:
                stat[day] = OrderedDict()
            if lvl not in stat[day]:
                stat[day][lvl] = [0,0]
            if ans:
                stat[day][lvl][0] += 1
            else:
                stat[day][lvl][1] += 1
        
        strs = ''
        for day, st in stat.items():
            strs += '---[Day: %s]---\n'%(day,)
            for k, v in st.items():
                strs += '[%3d] SUCC: %5d, FAIL: %5d\n'%(k, v[0],v[1])
        return strs

    #------------- show rlt ----------------
    def toStrHead(self):
        strs =  '-'*5+'name: '+str(self._name)+'-'*5
        strs += '-'*5+'mlvl: '+str(self.getMaxLevel())+'-'*5
        strs += '-'*5+'trys: '+str(len(self._history))+'-'*5
        return strs

    def toStrBegin(self, desc):
        return '-'*10+' beg '+str(desc)+' '+'-'*10

    def toStrEnd(self,desc):
        return '-'*10+' end '+str(desc)+' '+'-'*10

    def showSt(self):
        print self.toStrHead()
        print self.toStrBegin('stat')
        print self.getStat()        
        print self.toStrEnd('stat')
        return

    def showDaySt(self):
        print self.toStrHead()
        print self.toStrBegin('day stat')
        print self.getDayStat()
        print self.toStrEnd('day stat')
        return

    def showDetail(self, doCnt):
        print self.toStrHead()
        print self.toStrBegin('detail')
        lens = len(self._history)
        idx = 0
        for _,v in self._history.items():
            idx += 1
            if idx > lens - doCnt:
                print v.toStr()
        print self.toStrEnd('detail')
        return
