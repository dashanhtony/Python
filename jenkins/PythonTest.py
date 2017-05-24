import random
import math
import sys
import os

abc = 1234
def setabc(abc):
    abc = 234
    print(locals())
    print(globals())
setabc(11)
print(sys.platform)
x=raw_input
