
# Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

a = "aaabbbcc"
mc = Counter(a)
print(mc)
# Diccionario: key el caracter, value: el counter

print(mc.most_common(1))
# mc.most_common(1)[0] una tupla
# mc.most_common(1)[0][0] elemento 0

#desempaquetar en lista
print(list(mc.elements()))

# namedtuple
Point = namedtuple('Point','x,y')
pt = Point(1, -4)
print(pt.x)

# OrderedDict

ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 4
ordered_dict['d'] = 6
ordered_dict['a'] = 0
print(ordered_dict)

# defaultdickt

d = defaultdict(int)
d['a'] = 1
d['b'] = 2

print(d['c'])

# deque

d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(0)
print(d)
d.pop()
print(d)
d.popleft()
print(d)

d.extend([4, 5, 6])
print(d)
d.extendleft([0, -1])
print(d)

d.rotate(1)
print(d)

