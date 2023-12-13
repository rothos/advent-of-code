from collections import Counter
from itertools import *
import astar

x = '8A004A801A8002F478'

s = "".join([format(int(d,16),'b') for d in x])

print(s)