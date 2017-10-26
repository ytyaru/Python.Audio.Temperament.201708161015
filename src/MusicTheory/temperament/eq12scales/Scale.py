#音律 = EqualTemperament
#基音Hz = 440Hz
#基音Id = A
#基音Pitch = 4
#Scale = Major
#ScaleKey = C
#



import MusicTheory.temperament.EqualTemperament
#import MusicTheory.scales.MajorScales
#import MusicTheory.temperament.eq12scales.ScaleIntervals
from MusicTheory.temperament.eq12scales.ScaleIntervals import ScaleIntervals

#12平均律における12音の名前指定で周波数を取得する
#音名(key),音高(pitch)から周波数を返す
class Scale:
    def __init__(self, temperament):
        self.__temperament = temperament
    @property
    def Temperament(self): self.__temperament
    @Temperament.setter
    def Temperament(self, v): self.__temperament = v
    """
    指定したスケール、キーの構成音を返す。return ((KeyId, Pitch, 周波数),(...),...)
    """
    def Get(self, scaleKeyId, intervals):
        if scaleKeyId < 0 or self.__temperament.Denominator <= scaleKeyId: raise Exception(f'scaleKeyIdは0〜{self.__temperament.Denominator-1}の整数値にしてください。')
#        tones = list(self.__GetScaleTones(scaleKeyId, intervals))        
#        scales = []
        return list(self.__GetScaleTones(scaleKeyId, intervals))
    
    def __GetScaleTones(self, scaleKeyId, intervals):
        keyId = scaleKeyId
        l = [0]
        l.extend(intervals)
        for interval in l:
            keyId += interval
#            yield self.__temperament.Cycle(keyId)
            k, p = self.__temperament.Cycle(keyId)
            yield (k, p, self.__temperament.GetFrequency(k, self.__temperament.BaseKeyPitch + p))
#            yield (keyId, self.__temperament.BaseKeyPitch + pitch, self.__temperament.GetFrequency(keyId, self.__temperament.BaseKeyPitch + pitch))
    
    """
    #スケールキー音の周波数を取得する（基音とスケールキー音との差を考えて）
    #self.__BaseKeyId = 9
    #scaleKeyId = 0: -9
    #scaleKeyId = 11: +2
    #(scaleKeyId - self.__temperament.BaseKeyId) / self.Denominator
    def __GetScaleKeyFrequency(self, scaleKeyId):
        return self.__temperament.BaseFrequency * math.pow(2, (scaleKeyId - self.__temperament.BaseKeyId) / self.Denominator)
    def __GetOctaveFrequency(self):
        for tone in range(self.__temperament.Denominator):
            yield self.__temperament.BaseFrequency * math.pow(2, (tone + scaleKeyId - self.__temperament.BaseKeyId) /
    """
if __name__ == '__main__':
    scale = Scale()
    print(scale.Get(0, ScaleIntervals.Major))
    print(scale.Get(11, ScaleIntervals.Major))
