import collections

dict1 = collections.defaultdict(int)

dict1[1] = 1
dict1[2]+=1

print(dict1)

dict2 = collections.Counter([1,2,1,2,3])

dict2[1] += 1

print(dict2)

dict2 += collections.Counter({1,2,3,4,5})

print(dict2)


Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
# p.x =3 !
print(p.x, p.y)