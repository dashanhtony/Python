__author__ = 'Administrator'


def MyGenerator():
    a = (yield 10)
    print('a=%d' % a)
    b = (yield 12)
    print('b=%d' % b)


gen = MyGenerator()
print(gen.__next__())#执行MyGenerator到yield 10
print(gen.send(4))#把4赋值给a，执行print(a)，到yield 12
print(gen.send(3))#把3赋值给b，并尝试执行下一个yield，无，报错