from collections import defaultdict
import numpy as np

with open("/home/obluff/Downloads/input") as r:
    inp = r.read()
    
instructions = [_.split(" ") for _ in inp.split("\n") if _]

# part 2 
res = defaultdict(int)
cycles = 0
for i, item in enumerate(instructions):
    if item[0] == 'addx':
        res[cycles + 2] = int(item[1])
        cycles += 2
        continue
    cycles += 1
cs = np.cumsum([res[i] for i in range(max(res.keys()) + 1)]) + 1
idxs = np.array([20, 60, 100, 140, 180, 220])
sum(idxs * cs[idxs- 1])

# part 2
fin = []
for sub_arr in np.array_split(cs, 6):
    nxt = []
    for crt, reg in enumerate(sub_arr):
        if abs(reg - crt) < 2:
            nxt.append("#")
        else:
            nxt.append(".")
    fin.append(nxt)
print("\n".join([("".join(_)) for _ in fin]))
