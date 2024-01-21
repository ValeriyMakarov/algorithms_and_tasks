a = 10

def ifelse():
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 3
    elif a == 4:
        return 4
    elif a == 5:
        return 5
    elif a == 6:
        return 6
    elif a == 7:
        return 7
    elif a == 8:
        return 8
    elif a == 9:
        return 9
    elif a == 10:
        return 10
    else:
        return a

def mtch():
    match a:
        case 0: return 0
        case 1: return 1
        case 2: return 2
        case 3: return 3
        case 4: return 4
        case 5: return 5
        case 6: return 6
        case 7: return 7
        case 8: return 8
        case 9: return 9
        case 10: return 10
        case _: return a

import timeit
print(timeit.timeit(mtch, number=1_000_000_00))
print(timeit.timeit(ifelse, number=1_000_000_00))