#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#https://ja.wikipedia.org/wiki/%E3%83%9E%E3%82%AB%E3%83%BC%E3%83%A0
#日本の音階(雅楽、俗楽などの古典邦楽の音階)
#メジャー・ペンタトニック・スケールと同一のスケール
class YonanukiJapanScale:
    def __init__(self):
        #C D E G A
        # 2 2 3 2
        #C D Eb G Ab
        # 2 1  3 1
        #C Eb F G Bb
        # 3  2 2 3
        #C E F G B
        # 4 1 2 4
        #C D Eb G A
        # 2 1 4  2
        #C Db F Gb Bb
        # 1  4 1  4
        self.__interval_patterns = [[2,2,3,2],[2,1,3,1],[3,2,2,3],[4,1,2,4],[2,1,4,2],[1,4,1,4]] #(1/4音さげるのを表現できない)
        self.__names = ['ヨナ抜き長音階', 'ヨナ抜き短音階', 'ニロ抜き短音階', 'ニロ抜き長音階', '雲井音階', '岩戸音階']
        self.__index = 0
        self.__intervals = [2,2,3,2]
    
    @property
    def Index(self): return self.__index
    @property
    def Name(self): return self.__names[self.__index]
    @property
    def Intervals(self): return self.__intervals
    @property
    def IntervalPatterns(self): return self.__interval_patterns
    
    def GetIntervalsFromName(self, name):
        if name.title() not in self.__names: raise Exception(f'nameは{self.__names}のいずれかにしてください。')
        index = self.__GetIntervalsIndex(name)
        return self.GetIntervalsFromIndex(index)
    def GetIntervalsFromIndex(self, base_index):
        if base_index < 0 or len(self.__names) <= base_index: raise Exception('base_indexは0〜{len(self.__names)-1}の整数値にしてください。')
        self.__index = base_index
        self.__intervals = self.__interval_patterns[self.__index]
        return self.__interval_patterns[self.__index]
    def __GetIntervalsIndex(self, name):
        for i, n in enumerate(self.__names):
            if name.title() == self.__names[i].title(): return i
        return -1


if __name__ == '__main__':
    s = YonanukiJapanScale()
    print('========== 古典邦楽・スケール ==========')
    print('s.Intervals', s.Intervals)
    print('---------- index ----------')
    for index in range(len(s.IntervalPatterns)):
        s.GetIntervalsFromIndex(index)
        print(index, s.Index, s.Name, s.Intervals)
    print('---------- name ----------')
    for name in ['ヨナ抜き長音階', 'ヨナ抜き短音階', 'ニロ抜き短音階', 'ニロ抜き長音階', '雲井音階', '岩戸音階']:
        s.GetIntervalsFromName(name)
        print(s.Index, s.Name, s.Intervals)
