from collections import defaultdict
import re
sample = 1
with open(("4d_input.txt" if sample else "sample.txt"),"r+") as rf:
    lines = [line.strip() for line in rf.readlines()]


def pt1():
    tot = 0
    for line in lines:
        line = line.split(":")[1]
        win, check = line.split("|")
        win = win.split()
        check = check.split()
        
        cur = 0
        for val in check:
            if val in win:
                cur += 1
        
        if cur:
            tot += 2**(cur-1)
    return tot


def pt2():
    tot = 0
    ins = {}
    N= defaultdict(int)
    for i, line in enumerate(lines):
        N[i] += 1
        line = line.split(":")[1]
        win, check = line.split("|")
        win = win.split()
        check = check.split()
        
        cur = 0
        for val in check:
            if val in win:
                if cur in ins:
                    ins[cur] += 1
                else:
                    ins[cur] = 1
                cur += 1
        
        for j in range(cur):
            N[i+1+j] += N[i]
    return sum(N.values())

print(f"pt1: {pt1()}")
print(f"pt2: {pt2()}")