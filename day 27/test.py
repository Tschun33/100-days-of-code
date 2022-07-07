def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(2,3,4,5,6,6,7))

def calculate(n, **kwargs):
    if kwargs.get("add"):
        n += kwargs.get("add")
    if kwargs.get("multi"):
        n *= kwargs.get("multi")
    print(n)

calculate(2, multi=3)
