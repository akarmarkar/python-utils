#!/usr/bin/python
import sys
sys.setrecursionlimit(10)

def recursive_flatten(iterable,result=None):
	if result is None:
		result = []

	for item in iterable:
		if isinstance(item,list) or isinstance(item,tuple):
			result.extend(flatten(item))
		else:
			result.append(item)

	return result			

def iterative_flatten(iterable,result=None):
	if result is None:
		result = []
	
	stack = [iter(iterable)]
	while stack:
		_iter = stack.pop()
		while _iter:
			try:
				item = _iter.next()
			except StopIteration:
				break
			if isinstance(item,list) or isinstance(item,tuple):
				stack.append(_iter)
				stack.append(iter(item))
				break
			else:
				result.append(item)
	
	return result			

def flatten(iterable,result=None):
	if result is None:
		result = []
	
	stack = [iter(iterable)]
	while stack:
		iterable = stack.pop()
		for item in iterable:
			if isinstance(item,list) or isinstance(item,tuple):
				stack.append(iter(iterable))
				stack.append(iter(item))
				break
			else:
				result.append(item)

	return result			

if __name__ == "__main__":
	#assert flatten([1,[2,3,4],5,6,[7,8,[9,[10],11]]]) == range(1,12)
	#print flatten([1,[2,3,4],5,6,[7,8,[9,[10],11]]])
	str = "l = "
	count = 40
	for i in range(count+1):
		str += "[%d," % i
	str += "]" * (count + 1)
	print "str=",str
	exec(str)
	print flatten(l)
	l = [0,1,[2,3,(4,5),6],7]
	print iterative_flatten(l)
	print flatten(l)
