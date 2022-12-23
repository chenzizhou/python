# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:50:44 2022

@author: Administrator
"""

import collections
import threading
import time
candle=collections.deque('candle')

def burn(direction,nextSource):
    while True:
        try:
            next=nextSource()
        except IndexError:
            break
        else:
            print("%s:%s\n"%(direction,next))
            time.sleep(0.1)
    print("done %s\n"%direction)
    return 


left=threading.Thread(target=burn,args=('left',candle.popleft))
right=threading.Thread(target=burn,args=('right',candle.pop))

left.start()
right.start()

left.join()
right.join()

