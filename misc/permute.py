
from itertools import product,permutations
def permute(s):
    """
    Compute permutations of a string."
    :param s: string like 'abc'
    :return: set{'abc','acb','bac','bca','cab','cba'}
    which is 6 permutations. In general, length is n!
    if no repeating characters and n!/r! if r chars repeat.
    """
    if len(s) == 1:
        return set([s])

    if len(s) == 2:
        return set([s,s[::-1]])

    l = []
    i = 0
    while i< len(s):
        # Fixup a character like 'a' from 'abcd' and permute 'bcd'. Fixup a
        # different character each time.
        c,s1 = s[i],s[:i]+s[i+1:]
        i +=1
        l.extend([c+s2 for s2 in permute(s1)])

    diff = len(l) - len(set(l))
    if diff:
        print("Diff=",diff)
    return set(l)

def factorial(num):
    prod = 1
    for i in range(1,num+1):
        prod *= i

    return prod


s = "abcd"
s1 = permute(s)
print(s1,factorial(len(s)))
assert len(s1) == factorial(len(s))

s = "abb"
s1 = permute(s)
print("s1=",s1,factorial(len(s)))
print("len(s1)=",len(s1),"perms=", len(list(permutations(s))))
p = set(''.join(items) for items in permutations(s))
print("permutations(s)=",p,len(p))
print("diff=",p-s1)
#assert len(s1) == factorial(len(s))