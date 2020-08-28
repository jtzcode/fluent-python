# List Comprehension
symbols = 'python-learner'
codes = [ord(s) for s in symbols if ord(s) <= 100]
filter_codes = list(filter(lambda c: c <= 127, map(ord, symbols)))
print(codes)
print(filter_codes)

colors = ['blue', 'yellow']
sizes = ['M', 'L', 'XL']

shirts = [(color, size) for color in colors for size in sizes]
print(shirts)

# Generator expressions
tup = tuple(ord(symbol) for symbol in symbols)
print(tup)
import array
arr = array.array('I', (ord(symbol) for symbol in symbols))
print(arr)

# Save memory to store temp tuples.
for shirt in ( '%s %s' % (c, s) for c in colors for s in sizes):
    print(shirt)

# un-pack tuples
travelers = [('CHN', '222888666'), ('USA', '111444555'), ('IND', '333333333')]
for passport in sorted(travelers):
    print('%s/%s' % passport)

coordinates = (10, 23)
month, day = coordinates
print('%s - %s' % (month, day))

a = 10
b = 20
b, a = a, b
print('a={0}, b={1}'.format(a, b))

import os
_, filename = os.path.split('c:\windows\test\python.exe')
print(filename)

a, *oneandtwo, c, d = range(5)
print(oneandtwo)

# named tuple
from collections import namedtuple
City = namedtuple('City', 'name region size coordinates')
nanjing = City('Nanjing', 'China', 30000, (30, 142))
print(nanjing.size)
print(nanjing.coordinates)
print(nanjing[1])

Location = namedtuple('Location', 'lat long')
cityData = ('Beijing', 'China', 100000, Location(56, 120))
beijing = City._make(cityData)
beijing._asdict()
