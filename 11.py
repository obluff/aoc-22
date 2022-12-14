"""This day turned me into the joker. I believe solution only has part 2. Never revisting this"""
from dataclasses import dataclass, replace
from typing import List, Callable, Dict
from collections import defaultdict
from functools import reduce
import numpy as np

@dataclass
class Monkey:
    """Trying to do scala in python. Lol"""
    number: int
    items: List[int]
    op: Callable
    test: Callable
    second_test: Callable
    mod: int
    
    def turn(self) -> Dict[int, List[int]]:
        end = defaultdict(list)
        for item in self.items:
      
            lol = self.op(item)
            new_wl = 3 - int(lol % 3)
            nm = self.test(new_wl)
            end[nm].append(new_wl)
            print(f"Monkey inspects item with level: {item}")
            print(item)
            print(f"""
            Worry level increases by {item} to {lol}.
            Monkey gets bored with item. Worry level is divided by three to {new_wl}.
            Item with worry level {new_wl} is thrown to monkey {nm}. 
            """)
        return end
    
    def turn2(self, mod_zero) -> Dict[int, List[int]]:
        end = defaultdict(list)
        for item in self.items:
            lol = self.op(item) % mod_zero
            nm = self.test(lol)
            end[nm].append(lol)
            #print(f"Monkey inspects item with level: {item}")
            #print(item)
            #print(f"""
            #Worry level increases by {item} to {lol}.
            #Monkey gets bored with item. Worry level is divided by three to {new_wl}.
            #Item with worry level {new_wl} is thrown to monkey {nm}. 
            #""")
        return end
    
    
    def clear(self):
        cp = replace(self)
        cp.items = []
        return cp
    
    def update(self, items) -> Monkey:
        cp = replace(self)
        cp.items += items
        return cp
    
    def copy(self) -> Monkey:
        return replace(self)
    
def parse_monkey(m) -> Monkey:
    mn = int(re.findall("Monkey (\d+):", m)[0])
    si = [int(_) for _ in re.findall("Starting items: (.*)\n", m)[0].split(",")]
    op = re.findall("Operation: new = (.*)\n", m)[0]
    print(op)
    op_f = eval(f"lambda old: {op}")
    divisible = int(re.findall("Test: divisible by (\d+)", m)[0])
    mt = int(re.findall("If true: throw to monkey (\d+)", m)[0])
    mf = int(re.findall("If false: throw to monkey (\d+)", m)[0])
    d_f = lambda x: mt if not x % divisible else mf
    other_f = lambda x: mt if not (x % divisible)*(3**-1 % divisible)%divisible else mf
    return Monkey(mn, si, op_f, d_f, other_f, divisible)   


def run_round(_mmap):
    mids = sorted(_mmap.keys())
    mmap = {a: b.copy() for a, b in _mmap.items()} 
    for mid in mids:
        print(f"Monkey {mid}")
        curr_m = mmap[mid]
        nxt = curr_m.turn()
        for _mid, items in nxt.items():
            mmap[_mid] = mmap[_mid].update(items)
        mmap[mid] = curr_m.clear()
    return mmap

def run_round(_mmap, mod_zero):
    mids = sorted(_mmap.keys())
    mmap = {a: b.copy() for a, b in _mmap.items()} 
    for mid in mids:
        print(f"Monkey {mid}")
        curr_m = mmap[mid]
        nxt = curr_m.turn2(mod_zero)
        for _mid, items in nxt.items():
            mmap[_mid] = mmap[_mid].update(items)
        mmap[mid] = curr_m.clear()
    return mmap


def run():
    ms = inp.split("\n\n")
    monkeys = [parse_monkey(_) for _ in ms]
    
    mod_zero = reduce(lambda x, y: x*y, [x.mod for x in monkeys])
    mmap = {m.number: m for m in monkeys}
    rounds = [{a: b.copy() for a, b in mmap.items()}]
    for i in range(10000):
        mmap = run_round(mmap, mod_zero)
        fullcp = {a: b.copy() for a, b in mmap.items()} 
        rounds.append(fullcp)              
        
    
    np.sort(np.array([[len(m[mid].items) for mid in rounds[0].keys()] for m in rounds[:-1]]).sum(axis=0))   
