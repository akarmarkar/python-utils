# benchmark.py
"""
A benchmarking context-manager/decorator function.
@author: Amol Karmarkar, 2014.
The code has been adapted from David Beazley's blog at :
http://dabeaz.blogspot.com/2010/02/function-that-works-as-context-manager.html
@version: 0.1
"""

from __future__ import print_function
import time,sys
from contextlib import contextmanager

def get_name(obj):
    if sys.version > '3':
        return obj.__qualname__
    else:
        return obj.__name__
    
class TimingInfo(object):
    def __init__(self,benchmark_name,start):
        self.benchmark_name = benchmark_name
        self.start = start
    
    @property
    def interval(self):
        return self.end - self.start
    
def timethis(what,print_interval=False):
    """
    :param what : This can be either a function or a string representing the
    benchmark name. If this is a function, then the benchmark name is either
    the __name__ attribute of the function or __qualname__, depending on the
    version of python you are running.
    :param print_interval : A boolean value that controls if the timing info
    is to be printed to stdout by default.
    
    Example usage : 
    This function can be used in 2 ways :
    
    * Time a block using the with statement. 
    
    with timethis("some_benchmark",print_interval=True) as timing_info:
        ...
        code block to benchmark
        ...
    print("benchmark {0:s}={1:.3f} seconds".format(timing_info.benchmark_name,
    timing_info.interval))

    * As a decorator :
    
    @timethis
    def function_to_be_timed():
        ...
        return x,y,z

    (x,y,z),timing_info = function_to_be_timed()
    print("benchmark {0:s}={1:.3f} seconds".format(timing_info.benchmark_name,
    timing_info.interval))
        
    """

    # define an internal benchmark method using contextmanager
    @contextmanager
    def benchmark(benchmark_name):
        start = time.time()
        t = TimingInfo(benchmark_name,start)
        yield t
        t.end = time.time()
        if print_interval:
            print("{0:s} : {1:0.3f} secs".format(benchmark_name, t.interval))
        
    if callable(what):
        # If what is being timed is callable, return a wrapper that
        # uses the internal benchmark method in combination with 
        # the 'with' block
        def timed(*args,**kwargs):
            with benchmark(get_name(what)) as timing_info:
                # Make the actual call
                return what(*args,**kwargs),timing_info
        return timed
    else:
        return benchmark(what)

# The py.test tests  :

@timethis
def function_to_be_timed():
    total = 0
    tot_mul = 1
    for i in range(1,100):
        total += i
        tot_mul = tot_mul *i
    return total,tot_mul

def test_decorator():
    (total,tot_mul),timing_info = function_to_be_timed()
    print("total=",total,"tot_mul=",tot_mul)
    print("benchmark {0:s}={1:.3f} seconds".format(timing_info.benchmark_name,
                                                   timing_info.interval))

def test_contextmgr1():
    with timethis("benchmark_big_loop",print_interval=True) as timing_info:
        total = 0
        for i in range(1,100000):
            total += i  
    print("benchmark {0:s}={1:.3f} seconds".format(timing_info.benchmark_name,
                                                   timing_info.interval))   

def test_contextmgr2():
    with timethis("benchmark_sleep") as timing_info:
        try:
            total = 0
            time.sleep(2)
            raise ValueError("Exception raised !")
            for i in range(1,100):
                total += i     
        except:
            pass
         
    print("benchmark {0:s}={1:.3f} seconds".format(timing_info.benchmark_name,
                                                   timing_info.interval))    
