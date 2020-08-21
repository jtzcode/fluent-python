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