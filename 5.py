# yikes -- no bash.. no stacks -- not cleaning this up

import numpy as np
import re 

def prepro(inp):
    return [[x for x in _.split("\n") if x] for _ in inp.split("\n\n")]

def pp(x):
    new = []
    for i in range(0, len(x), 4):
        new.append(x[i:i+4][1])
    return new
    
def move(board, flip, mag, f, t):
    f = f -1 
    t = t-1
    new = board.copy()
    nempty_f = (new[f] == ' ').sum()
    nempty_t = (new[t] == ' ').sum()
    to_add = new[f][nempty_f:nempty_f + mag]
    if flip:
        to_add = np.flip(to_add)
    new[t][nempty_t - mag: nempty_t] = to_add
    new[f][nempty_f:nempty_f+mag] = ' '
    return new

def setup():
    pat = re.compile("move (\d+) from (\d+) to (\d+)")
    def extract_move(s):
        return [int(_) for _ in re.findall(pat, s)[0]]
    states, _moves = prepro(inp)
    moves = [extract_move(move) for move in _moves]
    items = [pp(_) for _ in states[:-1]]
    arr = np.array(items).T
    _arr = arr.tolist()
    # lol padding
    arr = np.array([[' ' for i in range(100000)] + _ for _ in _arr])
    return arr, moves


def end(arr):
    s = ''
    for i in range(arr.shape[0]):
        nempty_f = (arr[i] == ' ').sum()
        s += arr[i][nempty_f]
    return s
        

arr, moves = setup()
arr1, arr2 = arr.copy(), arr.copy()
for m in moves:
    arr1 = move(arr1, True, *m)
    arr2 = move(arr2, False, *m)

print(end(arr1))
print(end(arr2))
