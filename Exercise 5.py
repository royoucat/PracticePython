import random

a = []
b = []
c = []

for i in range(15):
    a.append(random.randint(1, 100))
for i in range(20):
    b.append(random.randint(1, 100))



for i in a:
    if i in b:
        print(i)
        if i not in c:
            c.append(i)


print(c)
