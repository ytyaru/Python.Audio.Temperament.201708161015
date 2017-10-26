#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#http://www.chaco2008.com/theory/1-3_majorscale.html
#http://www.chaco2008.com/theory/2-3_minorscale.html
#メジャー・スケール=全,全,半,全,全,全,半
#マイナー・スケール=全,半,全,全,半,全,全
#全音=2, 半音=1
#CMajor=C,D,E,F,G,A,B
#Cminor=C,D,D#,F,G,G#,A#
#ポピュラー音楽においては使用される事が少なく、さらにハーモニック・マイナー・スケールとハーモニック・マイナー・パーフェクト5th・ビロウ・スケール以外はほぼ使われない。
class HarmonicMinorScale:
    def __init__(self):
        # ナチュラル・マイナー・スケールにおける__aeolian_intervalsの最後の要素を半音上げたものと同じ
        self.__aeolian_intervals = [2,1,2,2,1,2,3]
#        self.__names = ['Aeolian', 'Locrian', 'Ionian', 'Dorian', 'Phrigian', 'Lydian', 'Mixolydian']
        self.__names = ['Harmonic', 'Locrian', 'Aeolian', 'Ionian', 'Dorian', 'HarmonicMinorPerfect5thBelow(PhrigianMajor)', 'Lydian', 'SuperLocrian(Altered)']
        self.__index = 0
        self.__intervals = [2,1,2,2,1,2,3]

    @property
    def Index(self): return self.__index
    @property
    def Name(self): return self.__names[self.__index]
    @property
    def Intervals(self): return self.__intervals
    
    def GetIntervalsFromName(self, name):
        print('name', name)
        if name not in self.__names: raise Exception(f'nameは{self.__names}のいずれかにしてください。')
#        if name.title() not in self.__names: raise Exception(f'nameは{self.__names}のいずれかにしてください。')
        index = self.__GetIntervalsIndex(name)
        return self.GetIntervalsFromIndex(index)
    def GetIntervalsFromIndex(self, base_index):
        if base_index < 0 or len(self.__names) <= base_index: raise Exception('base_indexは0〜{len(self.__names)-1}の整数値にしてください。')
        self.__index = base_index
        self.__intervals.clear()
        self.__intervals.extend(self.__aeolian_intervals[base_index:])
        self.__intervals.extend(self.__aeolian_intervals[:base_index])
#        print(self.__names[base_index], self.__intervals)
        return self.__intervals
    def __GetIntervalsIndex(self, name):
        for i, n in enumerate(self.__names):
            if name.title() == self.__names[i].title(): return i
        return -1


if __name__ == '__main__':
    s = HarmonicMinorScale()
    print('========== ハーモニック・マイナー・スケール ==========')
    print('---------- index ----------')
    for index in range(len(s.Intervals)):
        s.GetIntervalsFromIndex(index)
        print(index, s.Index, s.Name, s.Intervals)
    print('---------- name ----------')
    for name in ['Harmonic', 'Locrian', 'Aeolian', 'Ionian', 'Dorian', 'Harmonic Minor Perfect 5th Below( Phrigian Major )', 'Lydian', 'Super Locrian ( Altered )']:
#        s.GetIntervalsFromName(name)
        print(name.title().replace('5Th','5th').replace(' ', ''))
        print(name.title().replace('5Th','5th').replace(' ', '') == 'HarmonicMinorPerfect5thBelow(PhrigianMajor)')
        s.GetIntervalsFromName(name.title().replace('5Th','5th').replace(' ', ''))
        print(s.Index, s.Name, s.Intervals)
