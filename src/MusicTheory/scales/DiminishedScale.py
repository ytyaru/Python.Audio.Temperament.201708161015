#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#https://ja.wikipedia.org/wiki/%E7%A7%BB%E8%AA%BF%E3%81%AE%E9%99%90%E3%82%89%E3%82%8C%E3%81%9F%E6%97%8B%E6%B3%95
#ディミニッシュト・スケール
#移調の限られた旋法第2旋法
class DiminishedScale:
    def __init__(self):
        # 1 2 b3 4 b5 #5 6 7
        # C D Eb F Gb G# A B
        #  2 1  2 1  2  1 2
        self.__intervals = [2,1,2,1,2,1,2]
        self.__names = ['C', 'C#', 'D']
        self.__index = 0
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
    s = DiminishedScale()
    print('========== ディミニッシュト・スケール ==========')
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
