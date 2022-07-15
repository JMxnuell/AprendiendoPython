# shallow copy: one level deep, only references of nested child objects
# deep copy: full independent copy

import copy

original = [1, 2, 3]
# it's fine if we work in one level deep
# cpy = copy.copy(original)
# cpy  = list(original)
# cpy = original [:]
# cpy[0] =- 10
original2 = [[1, 2, 3], [1, 2, 3]]
cpy = copy.deepcopy(original2)
cpy[0][1] = -100
print(original2, cpy)
