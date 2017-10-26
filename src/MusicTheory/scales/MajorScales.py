#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#http://www.chaco2008.com/theory/1-3_majorscale.html
#http://www.chaco2008.com/theory/2-3_minorscale.html
#メジャー・スケール=全,全,半,全,全,全,半
#マイナー・スケール=全,半,全,全,半,全,全
#全音=2, 半音=1
#CMajor=C,D,E,F,G,A,B
#Cminor=C,D,D#,F,G,G#,A#
#import MusicTheory.scales.Scales
#class MajorScales(MusicTheory.scales.Scales):
class MajorScales:
    def __init__(self):
        self.__ionian_intervals = [2,2,1,2,2,2,1]
        self.__names = ['Ionian', 'Dorian', 'Phrigian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian']
        self.__index = 0
        self.__intervals = [2,2,1,2,2,2,1]

    @property
    def Index(self): return self.__index
    @Index.setter
    def Index(self, v):
        if v < 0 or len(self.__names) <= v: raise Exception('indexは0〜{len(self.__names)-1}の整数値にしてください。')
        self.__index = v
        self.__intervals.clear()
        self.__intervals.extend(self.__ionian_intervals[self.__index:])
        self.__intervals.extend(self.__ionian_intervals[:self.__index])
    @property
    def Name(self): return self.__names[self.__index]
    @Name.setter
    def Name(self, v):
        if v.title() not in self.__names: raise Exception(f'nameは{self.__names}のいずれかにしてください。')
        self.Index = self.__GetIntervalsIndex(v)
    @property
    def Intervals(self): return self.__intervals
    def __GetIntervalsIndex(self, name):
        for i, n in enumerate(self.__names):
            if name.title() == self.__names[i].title(): return i
        return -1


if __name__ == '__main__':
    s = MajorScales()
    print('========== メジャー・スケール ==========')
    print('---------- index ----------')
    for index in range(len(s.Intervals)):
        s.Index = index
        print(index, s.Index, s.Name, s.Intervals)
    print('---------- name ----------')
    for name in ['Ionian', 'Dorian', 'Phrigian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian']:
        s.Name = name
        print(s.Index, s.Name, s.Intervals)
