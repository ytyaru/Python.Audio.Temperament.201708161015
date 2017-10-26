#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#https://ja.wikipedia.org/wiki/%E3%83%9E%E3%82%AB%E3%83%BC%E3%83%A0
#中国の音階(調式)
#メジャー・ペンタトニック・スケールと同一のスケール
class SpainScale:
    def __init__(self):
        #1 2 3 5 6
        #C D E G A
        # 2 2 3 2
        self.__ionian_intervals = [2,2,3,2] # (1/4音さげるのを表現できない)
        self.__names = ['宮調式', '商調式', '角調式', '徴調式', '羽調式']
        self.__index = 0
        self.__intervals = [2,2,3,2]

    @property
    def Index(self): return self.__index
    @property
    def Name(self): return self.__names[self.__index]
    @property
    def Intervals(self): return self.__intervals
    
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


if __name__ == '__main__':
    s = SpainScale()
    print('========== 中国の音階(調式)・スケール ==========')
    print('s.Intervals', s.Intervals)
    print('---------- index ----------')
    for index in range(len(s.Intervals)):
        s.GetIntervalsFromIndex(index)
        print(index, s.Index, s.Name, s.Intervals)
    print('---------- name ----------')
    for name in ['宮調式', '商調式', '角調式', '徴調式', '羽調式']:
        s.GetIntervalsFromName(name)
        print(s.Index, s.Name, s.Intervals)
