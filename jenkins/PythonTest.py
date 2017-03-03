#!/usr/bin/env python3
# -*- coding: utf-8 -*-



class dummyclass(object):
    def __init__(self):
        self.is_d = True
        pass

class childdummyclass(dummyclass):
    def __init__(self, isman):
        self.isman = isman

    @classmethod
    def can_speak(self): return True

    @property
    def man(self): return self.isman

if __name__ == "__main__":
    object1 = dummyclass()
    object = childdummyclass('true')
    print(object.can_speak())

    print(object.is_d)
