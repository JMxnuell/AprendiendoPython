import random, secrets, numpy as np


a = random.random()
print(a) # 0 to 1

a = random.uniform(1, 10)
print(a)

a = random.randint(1, 10)
print(a)

a = random.randrange(1, 10) # upperbound not inclidung
print(a)

a = random.normalvariate(0, 1) # for normal distribution
print(a)

l = list("ABCDE")
print(random.choice(l))
print(random.sample(l, 3)) # elements unique
print(random.choices(l, k=3)) # elements mutiple times
random.shuffle(l) # intercambia los lugares
print(l)
# random.seed(1)

# secrets
# password, things mores securities
a = secrets.randbelow(10)
print(a)

print(secrets.randbits(4))
print(secrets.choice(l))

# numpy
print(np.random.rand(3,3))
