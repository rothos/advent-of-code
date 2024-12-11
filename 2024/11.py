text = open("input11.txt", 'r').read()
# text = open("input11test.txt", 'r').read()

from functools import cache
import math
from itertools import chain

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

@cache
def getnext(n):
    if n == 0:
        return 1
    if math.floor(math.log(n,10)) % 2:
        b = math.floor(math.log(n,10))
        return (n // 10**(b//2+1), n % 10**(b//2+1))
    else:
        return n*2024


nn = list(map(int, text.split()))
for _ in range(25):
    nn = flatten(getnext(n) for n in nn)
    # print(nn)

print(len(nn))


### PART 2

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        #Warning: You may wish to do a deepcopy here if returning objects
        return self.memo[args]

@Memoize
def do_iters(n, iters):
    if iters == 0:
        return 1
    if n == 0:
        return do_iters(1, iters-1)
    if math.floor(math.log(n,10)) % 2:
        b = math.floor(math.log(n,10))
        return sum([do_iters(n // 10**(b//2+1), iters-1), do_iters(n % 10**(b//2+1), iters-1)])
    else:
        return do_iters(n*2024, iters-1)


nn = list(map(int, text.split()))
print(sum(do_iters(n, 75) for n in nn))
