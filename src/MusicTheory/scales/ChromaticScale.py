#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#クロマティック・スケール
#半音階
class ChromaticScale:
    def __init__(self):
        # キーがC, C#のときしか使えないスケール
        self.__intervals = [*([1]*11)]
#        self.__names = []
#        self.__index = 0
#        self.__intervals = [2,2,2,2,2,2,2]

#    @property
#    def Index(self): return self.__index
#    @property
#    def Name(self): return self.__names[self.__index]
    @property
    def Intervals(self): return self.__intervals
    """
    def GetIntervalsFromName(self, name):
        if name.title() not in self.__names: raise Exception(f'nameは{self.__names}のいずれかにしてください。')
        index = self.__GetIntervalsIndex(name)
        return self.GetIntervalsFromIndex(index)
    def GetIntervalsFromIndex(self, base_index):
        if base_index < 0 or len(self.__names) <= base_index: raise Exception('base_indexは0〜{len(self.__names)-1}の整数値にしてください。')
        self.__index = base_index
        self.__intervals.clear()
        self.__intervals.extend(self.__ionian_intervals[base_index:])
        self.__intervals.extend(self.__ionian_intervals[:base_index])
#        print(self.__names[base_index], self.__intervals)
        return self.__intervals
    def __GetIntervalsIndex(self, name):
        for i, n in enumerate(self.__names):
            if name.title() == self.__names[i].title(): return i
        return -1
    """


if __name__ == '__main__':
    s = ChromaticScale()
    print('========== クロマティック・スケール ==========')
    print('s.Intervals', s.Intervals)
    """
    print('---------- index ----------')
    for index in range(len(s.Intervals)):
        s.GetIntervalsFromIndex(index)
        print(index, s.Index, s.Name, s.Intervals)
    print('---------- name ----------')
    for name in ['C', 'C#']:
        s.GetIntervalsFromName(name)
        print(s.Index, s.Name, s.Intervals)
    """
