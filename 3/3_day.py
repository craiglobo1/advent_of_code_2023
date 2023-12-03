import re
sample = 1
with open(("3d_input.txt" if sample else "sample.txt"),"r+") as rf:
    lines = [line.strip() for line in rf.readlines()]

def pt1():
    pos = []
    nums= {}
    
    for i in range(len(lines)):
        haspart = False     
        for j in range(len(lines[i])):
            if lines[i][j] not in ".1234567890":
                pos.append((i,j))


    pattern = re.compile("\d+")
    for i,line in enumerate(lines):
        for m in pattern.finditer(line):
            nums[(i,(m.start(), m.end()-1))] = m.group()   
        
    ans = []
    for pi,pj in pos:
        for val in nums:
            i,j = val
            js,je = j
            for rr in [-1,0,1]:
                for cc in [-1,0,1]:
                    if pi+rr  == i and (js <= pj+cc <= je):
                        ans.append(((pi,pj),int(nums[val])))
                        

    return sum([val[1] for val in list(set(ans))])     

def pt2():

    pos = []
    nums= {}
    
    for i in range(len(lines)):
        haspart = False     
        for j in range(len(lines[i])):
            if lines[i][j] not in ".1234567890":
                pos.append((i,j))


    pattern = re.compile("\d+")
    for i,line in enumerate(lines):
        for m in pattern.finditer(line):
            nums[(i,(m.start(), m.end()-1))] = m.group()   
        
    ans = []
    for pi,pj in pos:
        for val in nums:
            i,j = val
            js,je = j
            for rr in [-1,0,1]:
                for cc in [-1,0,1]:
                    if pi+rr  == i and (js <= pj+cc <= je):
                        ans.append(((pi,pj),int(nums[val])))

    ans = list(set(ans))  
    ansd = {}            
    for a in ans:
        pos, val = a
        if pos not in ansd:
            ansd[pos] = [val]
        else:
            ansd[pos].append(val)
    rem = []
    for val in ansd:
        if len(ansd[val]) <= 1:
            rem.append(val)

    for val in rem:
        del ansd[val]
    
    fans = 0
    for val in ansd:
        tot = 1
        for num in ansd[val]:
            tot *= num
        fans += tot
    return fans
    
print(f"pt1: {pt1()}")
print(f"pt1: {pt2()}")
