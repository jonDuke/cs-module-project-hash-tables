"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# cache answers to f(x)
cache = {}
for n in q:
    cache[n] = f(n)

# check all combinations of a,b,c,d
for a in q:
    for b in q:
        for c in q:
            for d in q:
                # check the condition
                if cache[a] + cache[b] == cache[c] - cache[d]:
                    # print this combination
                    print(f"f({a}) + f({b}) = f({c}) - f({d})    {cache[a]} + {cache[b]} = {cache[c]} - {cache[d]}")
