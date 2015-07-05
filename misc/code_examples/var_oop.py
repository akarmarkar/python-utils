#!/usr/bin/python

x = 1
l = l1 = [1,2,3]
l2 = [1,2,3]
def f(x,l=[]):
    x = 42
    l.append(x)
    print l

f(x,l)
print x,l,l1,l2

#---------------------------

def g(l=[]):
    l.append(22)
    print l
g()
g()

#---------------------------

class Base(object):
    def f(self):
        print "Base f called"
    def g(self):
        print "Base g called"
    def h(self):
        print "Base h called"

class P1(Base):
    def g(self):
        print "P1 g called"

class P2(Base):
    def h(self):
        print "P2 h called"

class C(P1,P2):
    pass

c= C()
c.f()
c.g()
c.h()

# What is the output of the program when run ?
