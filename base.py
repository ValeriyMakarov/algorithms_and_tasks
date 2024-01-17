a = 12
match a:
    case 1 | 12:
        print(1)
    case 2:
        print(2)
    case aa:
        print(aa)

a = 0b0101
print(a)
b = 0x10
print(b)
c = 0o10
print(c)
print(a & c == 0)
print(a | c == 0b1101)
print('xor', a ^ c == 0b1101)