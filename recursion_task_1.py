import typing

t = [1, [2.2, 22, ['dfsr', 3], 4], 5]

def rec(*args):
    res = 0

    for arg in args:
        if isinstance(arg, typing.Iterable) and not isinstance(arg, str):
            res += rec(*arg)
        elif isinstance(arg, (int, float)):
            res += arg

    return res


print(rec(t))
