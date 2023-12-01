sample = 1

no_str = ["one", "two" ,"three", "four", "five", "six", "seven", "eight", "nine"]

with open(("1d_input.txt" if sample else "sample.txt"),"r+") as rf:
    lines = [line.strip() for line in rf.readlines()]


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

s = 0
for i, line in enumerate(lines):
    found = []
    for k,c in enumerate(line):
        if c.isnumeric():
            found.append((k,int(c))) 
    for j, no_rep in enumerate(no_str):
        for idx in find_all(line, no_rep):
            found.append((idx,j+1)) 

    found.sort()
    s += int(str(found[0][1]) + str(found[-1][1]))
    
print(s)