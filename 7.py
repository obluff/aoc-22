from collections import defaultdict
import re
def load():
    with open("/home/obluff/Downloads/input") as inp:
        return [x for x in inp.read().split("\n") if x]
#        return [_ for _ in inp.read().split("\n") if _]
#inp = """
  
def parse(inp):
    dirs = set()
    kids = defaultdict(set)
    files = defaultdict(set)
    file_size = defaultdict(int)
    d = ["home"]
    
    for cmd in inp[1:]:
        curr_path = "/".join(d)
        dirs.add(curr_path)
        if '$ cd' in cmd:
            new_dir = cd(cmd)
            if new_dir == '..':
                d.pop()
            else:
                d.append(new_dir)
            continue
        if '$ ls' in cmd:
            continue
        if 'dir' in cmd:
            kids[curr_path].add(curr_path + "/" + cmd.split(" ")[-1])
            continue
        
        size, file = cmd.split(" ")
        print(file)
        fn = curr_path + "/" + file
        files[curr_path].add(fn)
        file_size[fn] = size
    
    return dirs, kids, files, file_size
 
def cd(p):
    return re.findall("cd (.*)", p)[0]

def calc(target, dirs, kids, files, file_size):
    curr_lvl = sum([int(file_size[_]) for _ in files[target]])
    if not kids[target]:
        return curr_lvl
    return  curr_lvl + sum([calc(kid, dirs, kids, files, file_size) for kid in kids[target]])

inp = load()
dirs, kids, files, file_size = parse(inp)
data = dict([(_, calc(_, dirs, kids, files, file_size)) for _ in dirs])

print(sum([_ for _ in data.values() if _ <= 100000]))

delta = 70000000 - 30000000
print([x for x in sorted(data.items(), key=lambda x: x[1]) if data['home']-x[1]<=delta][0])
