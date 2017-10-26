#!python3.6
from collections import OrderedDict
class NaturalTone:
    def __init__(self):
        self.__NAMES = ('C','D','E','F','G','A','B')
        self.__INTERVALS = (0, 2, 2, 1, 2, 2, 2)
        self.__TONES = OrderedDict(zip(self.__NAMES, [sum(self.__INTERVALS[:n+1]) for n in range(len(self.__INTERVALS))]))
    @property
    def Tones(self): return self.__TONES
    @property
    def Names(self): return self.__NAMES
    @property
    def Intervals(self): return self.__INTERVALS
    def ToName(self, value):
        for n,v in self.__TONES.items():
            if v == value: return n
        raise Exception(f'valueは{self.__TONES.values()}のいずれかにしてください。')
    def ToValue(self, name):
        if name not in self.__TONES: Exception(f'nameは{self.__TONES.keys()}のいずれかにしてください。')
        return self.__TONES[name]

if __name__ == '__main__':
    nt = NaturalTone()
    print(nt.Tones)
    print(nt.Names)
    print(nt.Intervals)
    for name in ('C','D','E','F','G','A','B'): print(nt.ToValue(name))
    for name in [0,2,4,5,7,9,11]: print(nt.ToName(name))

