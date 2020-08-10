# Your code here

import random
import math
import time

# temporarily copied hashtable.py to this directory for the assignment
from hashtable import HashTable

lookup = HashTable(128)
dict_lookup = {}

# Estimated runtime: 47 hours
def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

# Runtime: 9.51 seconds with HashTable, 9.07 seconds with dict
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # # Implementation with my HashTable
    # key = str(x) + ',' + str(y)
    # cached = lookup.get(key)
    # if cached is None:
    #     # no cached answer, calculate it
    #     value = slowfun_too_slow(x, y)
    #     lookup.put(key, value)
    #     return value
    # else:
    #     return cached  # we have already calculated this
    
    # Implementation with dict
    key = str(x) + ',' + str(y)
    if key not in dict_lookup:
        # no cached answer, calculate it
        value = slowfun_too_slow(x, y)
        dict_lookup[key] = value
        return value
    else:
        return dict_lookup[key]  # we have already calculated this



# Do not modify below this line!  (I just added timer code)

before = time.time()
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
print(f"\nDone in {(time.time() - before):.2f} seconds")