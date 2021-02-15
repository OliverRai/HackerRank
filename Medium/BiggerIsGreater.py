import sys

def per(l):
    t1 = len(l)-1
    while t1>0 and l[t1-1]>=l[t1]:  t1 -= 1
    if t1 <= 0:     return False
    t2 = len(l)-1
    while l[t2]<=l[t1-1]:   t2 -= 1
    l[t1-1], l[t2] = l[t2], l[t1 - 1]
    l[t1:] = l[len(l)-1:t1-1:-1]
    return True


for cases in xrange(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    l = [ord(i) for i in s]
    if per(l):
        ans = ""
        for i in l:
            ans += chr(i)
        print(ans)
    else:
        print("no answer")
                
    
