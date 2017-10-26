import math
#import MusicTheory.Key
#十二平均律
class EqualTemperament:
    def __init__(self, A4_PITCH=440):
        self.__ids = (0,1,2,3,4,5,6,7,8,9,10,11)
        self.__names = ('C','C#','D','D#','E','F','F#','G','G#','A','A#','B')
        self.__diffs = (-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2)
        self.__denominator = 12 # 平均律の分母(3,4,6,12,19,24,31,53がある)
        self.__A4_PITCH = A4_PITCH
    def __calc_frequency(self, key_id, pitch):
#        print('{0:<2} {1:>2} {2:>3} {3:f}'.format(self.__names[key_id], key_id, pitch, 440 * math.pow(2, self.__diffs[key_id] * (1/12.0))))
#        print('{0:<2} {1:>2} {2:>3}'.format(self.__names[key_id], key_id, pitch))
        noteNumber = key_id + ((pitch + 1) * self.__denominator) # pitch=-1〜9
        A4noteNumber = ((4+2) * self.__denominator) - 3 #C-1=0とするとA4=69。A4(ラ)音=440Hzにおけるオクターブ数(4+2)から、半音3つ分引くとA4。
#        print('noteNumber:', noteNumber)
        return self.__A4_PITCH * math.pow(2, (noteNumber - A4noteNumber) / self.__denominator)
        """
        if 4 == pitch: return 440 * math.pow(2, self.__diffs[key_id] * (1/12.0))
        elif pitch < 4: return ( 440 * math.pow(2, self.__diffs[key_id] * (1/12.0)) ) / ((4 - pitch) + 1)
        elif 4 < pitch: return ( 440 * math.pow(2, self.__diffs[key_id] * (1/12.0)) ) * ((pitch - 4) + 1)
        else: raise Exception('実行されることのないelse文。')
        """
    def FromId(self, key_id, pitch=4): return self.__calc_frequency(key_id, pitch)
#    def FromKey(self, key:MusicTheory.Key.Key, pitch=4): return self.__calc_frequency(key.Id, pitch)
    @property
    def Ids(self): return self.__ids
    @property
    def Names(self): return self.__names
#    @property
#    def Frequencies(self): return self.__frequencies
