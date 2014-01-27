# benchmark.py
from __future__ import print_function
import time
from contextlib import contextmanager

class Timer(object):
    def __init__(self,name,start):
        self.name = name
        self.start = start
        
def timethis(what,print_interval=True):
    @contextmanager
    def benchmark():
        start = time.time()
        t = Timer(what,start)
        yield t
        t.end = time.time()
        t.interval = t.end - t.start
        if print_interval:
            print("%s : %0.3f seconds" % (what, t.interval))
        
    if hasattr(what,"__call__"):
        def timed(*args,**kwargs):
            with benchmark():
                return what(*args,**kwargs)
        return timed
    else:
        return benchmark()
   
if __name__ == "__main__":
    with timethis("test",print_interval=False) as b:
        total = 0
        for i in range(1,100000):
            total += i
       
    print("benchmark=%0.3f seconds",b.interval)
    
    with timethis("test1") as b:
        try:
            time.sleep(2)
            raise ValueError("Exception raised !")
        except:
            pass
    
    print("benchmark1=%0.3f seconds",b.interval)