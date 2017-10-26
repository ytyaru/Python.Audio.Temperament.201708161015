#!python3.6
from collections import OrderedDict
#変化記号(♭、♯)
class Accidental:
    def __init__(self):
        self.__NAMES = ('-','+')
        self.__VALUES = (-1, 1)
        self.__ACCIDENTALS = OrderedDict(zip(self.__NAMES, self.__VALUES))
    @property
    def Names(self): return self.__NAMES
    @property
    def Values(self): return self.__VALUES
    @property
    def Accidentals(self): return self.__ACCIDENTALS
    def ToName(self, value):
        for n,v in self.__ACCIDENTALS.items():
            if v == value: return n
        raise Exception(f'valueは{self.__ACCIDENTALS.values()}のいずれかにしてください。')
    def ToValue(self, name):
        if name not in self.__ACCIDENTALS: Exception(f'nameは{self.__ACCIDENTALS.keys()}のいずれかにしてください。')
        return self.__ACCIDENTALS[name]

if __name__ == '__main__':
    ac = Accidental()
    print(ac.Accidentals)
    print(ac.Names)
    print(ac.Values)
    for name in ('-','+'): print(ac.ToValue(name))
    for name in (-1, 1): print(ac.ToName(name))

