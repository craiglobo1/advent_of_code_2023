sample = 1
with open(("2d_input.txt" if sample else "sample.txt"),"r+") as rf:
    lines = [line.strip() for line in rf.readlines()]

def pt1():
    mr = 12
    mg = 13
    mb = 14
    data = []
    for line in lines:
        line = line.split(":")[1]
        line = line.split(';')
        data.append([{ pick.strip().split(" ")[1] : int(pick.strip().split(" ")[0]) for pick in turn.split(', ')} for turn in line])

    ans = 0
    for i,game in enumerate(data):
        pos = True
        for gs in game:
            if 'blue' in gs and gs['blue'] > mb:
                pos = False
            if 'red' in gs and gs['red'] > mr:
                pos = False
            if 'green' in gs and gs['green'] > mg:
                pos = False
        if pos:
            # print(i+1, game)
            ans += i+1
    return ans

def pt2():
    data = []
    for line in lines:
        line = line.split(":")[1]
        line = line.split(';')
        data.append([{ pick.strip().split(" ")[1] : int(pick.strip().split(" ")[0]) for pick in turn.split(', ')} for turn in line])
    
    ans = 0
    for game in data:
        max_r = max([ turn['red']  if 'red' in turn else -1 for turn in game ])
        max_b = max([ turn['blue']  if 'blue' in turn else -1 for turn in game ])
        max_g = max([ turn['green']  if 'green' in turn else -1 for turn in game ])
        ans += max_r*max_b*max_g
    return ans

print(f"pt 1: {pt1()}")
print(f"pt 2: {pt2()}")
