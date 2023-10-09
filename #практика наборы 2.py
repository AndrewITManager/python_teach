#практика наборы 2
a = {'abc', 'd', 'f', 'y'}
b = {'abc', 'd', 'f', 'l'}

print((a | b) - (a & b))
print(a.symmetric_difference(b))

c = {12, 23, 34, 25, 45}
d = {12, 5, 34, 50, 67, 45}
c.add(89)
print(c)
e = c.intersection(d)
print(e)
print(list(e))