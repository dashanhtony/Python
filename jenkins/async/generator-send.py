__author__ = 'Administrator'


def MyGenerator():
    a = (yield 10)
    print(a)
    b = (yield 12)
    print(b)


gen = MyGenerator()
print(gen.__next__())
print(gen.send(4))
print(gen.send(3))