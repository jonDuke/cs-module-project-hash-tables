"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# First solution: O(n^4) time complexity

# # cache answers to f(x)
# cache = {}
# for n in q:
#     cache[n] = f(n)

# # check all combinations of a,b,c,d
# for a in q:
#     for b in q:
#         for c in q:
#             for d in q:
#                 # check the condition
#                 if cache[a] + cache[b] == cache[c] - cache[d]:
#                     # print this combination
#                     print(f"f({a}) + f({b}) = f({c}) - f({d})    {cache[a]} + {cache[b]} = {cache[c]} - {cache[d]}")


# Second solution: O(n^2) time complexity (I think)

# build cache with the results as the key, and a,b,c,d as values
left_cache = {}
for a in q:
    for b in q:
        result = f(a) + f(b)
        if result in left_cache:
            left_cache[result].append((a,b))  # append the tuple
        else:
            left_cache[result] = [(a,b)]  # start a new list

right_cache = {}
for c in q:
    for d in q:
        result = f(c) - f(d)
        # only positive results can have a match, ignore negative ones
        if result >= 0:
            if result in right_cache:
                right_cache[result].append((c,d))
            else:
                right_cache[result] = [(c,d)]

# Compare results to find matches
for n in left_cache.keys():
    if n in right_cache:
        # this result is in both caches,
        # print all combinations of a,b,c,d that resulted in it
        for left in left_cache[n]:
            for right in right_cache[n]:
                print(f"f({left[0]}) + f({left[1]}) = f({right[0]}) - f({right[1]})\t"+
                      f"{f(left[0])} + {f(left[1])} = {f(right[0])} - {f(right[1])}")
