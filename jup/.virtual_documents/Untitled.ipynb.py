[x*3 for x in range(6)]


[[0 for x in range(3)] for y in range(4)]


def make_double(x):
    return x * 2


list(range(3))


list(map(make_double, [1,2,3]))


is_even = lambda x: x % 2 == 0


is_even(8)


is_even(7)


list(map(is_even, [3,4,6]))


list(filter(is_even, [1,2,3,4,5,6]))


[x*3 for x in range(6) if xget_ipython().run_line_magic("2", " == 0]")


[x*3 for x in range(6)]


import random


for _ in range(8):
    print(random.randint(0,3))
print("Done")



