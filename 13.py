"""-.-"""
from functools import reduce
from functools import cmp_to_key

def evaluate_dumb(a, b):
    if not a and not b:
        return 0 
    
    if not a:
        return 1
    
    if not b:
        return -1
    
    x, y = a[0], b[0]
    if isinstance(x, int) and isinstance(y, int):
        if x < y:
            return 1
        if x > y:
            return -1
        return evaluate_dumb(a[1:], b[1:])
    
    if isinstance(x, int):
        x = [x]
        
    if isinstance(y, int):
        y = [y]
        
    lols = evaluate_dumb(x, y)
    if lols == 0:
        return evaluate_dumb(a[1:], b[1:])
    return lols


def run():
    inps = [[_ for _ in x.split("\n") if _] for x in inp.split("\n\n")]
    data = [(eval(x), eval(y)) for x, y in inps] 
    print(sum([i+1 for i, _ in enumerate(data) if evaluate_dumb(*_) > -1]))
    input_two = reduce(lambda x, y: x + y, [list(_) for _ in data]) +  [[[2]], [[6]]]
    sort = sorted(input_two, key=cmp_to_key(evaluate_dumb))
    res = [i+1 for i, j in enumerate(reversed(sort)) if j in [[[6]], [[2]]]]
    print(res[0] * res[1])
