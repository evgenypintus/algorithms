
t = (x for x in range(10))

def generator(n):

    for i in range(n):
        yield i

for i in generator(5):
    print(i)