import math
#音律
#https://ja.wikipedia.org/wiki/%E5%B9%B3%E5%9D%87%E5%BE%8B


from abc import ABCMeta, abstractmethod
# 音律クラス
class Temperament(metaclass=ABCMeta):
#    BaseFrequency = 444 #A4(444, 440, 432), C(128, 528(C5))
    def __init__(self):
        self.__Denominator = 12
        self.__BaseFrequency = 440 #A4(444, 440, 432), C(128, 528(C5))
        self.__BaseKeyId = 9 #A (1オクターブ12音なら0〜11の値。[C,C#,D,D#,E,F,F#,G,G#,A,A#,B]の12音とすると9=A)
        self.__BaseKeyPitch = 4 #-1〜9（A4=440Hz。A3は220Hzになるし、A5は880Hzになる）
        self.__Frequencies = []
#        self.__calcFrequencies()
    #1オクターブ上にあるKey値とオクターブ増減値を返す。: tuple(key,octave)
    @property
    def Cycle(self, value): return ((value % self.Denominator), (value // self.Denominator))

    @property
    def Denominator(self): return self.__Denominator
    @Denominator.setter
    def Denominator(self, v):
        if 0 < v:
            self.__Denominator = v
            self.__calcFrequencies()

    def SetBaseKey(self, keyId, pitch, hz):
        if not (isinstance(keyId, int) and -1 < keyId and keyId < self.Denominator): raise Exception(f'keyIdは0〜{self.Denominator-1}の整数値(int型)にしてください。')
        if not isinstance(pitch, int): raise Exception('pitchはint型にしてください。')
        if hz <= 0: raise Exception('hzは0より大きい数値にしてください。')
        self.__BaseKeyId = keyId
        self.__BaseKeyPitch = pitch
        self.BaseFrequency = hz
    @property
    def BaseFrequency(self): return self.__BaseFrequency
    @BaseFrequency.setter
    def BaseFrequency(self, v):
        if 0 < v:
            self.__BaseFrequency = v
            self.__calcFrequencies()
    @property
    def BaseKeyId(self): return self.__BaseKeyId
    @property
    def BaseKeyPitch(self): return self.__BaseKeyPitch

    @property
    def Frequencies(self): return self.__Frequencies
    def __calcFrequencies(self):
        self.Frequencies.clear()
        for rate in range(self.Denominator): self.Frequencies.append(self.__BaseFrequency * math.pow(2, rate * 1/self.Denominator))

    def GetFrequency(self, keyId, pitch):
        baseKeyNoteNumber = ((self.BaseKeyPitch + 1 + 1) * self.Denominator) - (self.Denominator - self.BaseKeyId)
        k, p = self.Cycle(keyId)
        noteNumber = k + ((pitch + p + 1) * self.Denominator) # pitch=-1〜9
        return self.BaseFrequency * math.pow(2, (noteNumber - baseKeyNoteNumber) / self.Denominator)
    
    """
    構成音の周波数を取得する。（スケールのキーが指定した値のときの）
    """
    def GetOctaveFrequencies(self, scaleKeyId, pitch=None):
        if pitch is None: pitch = self.BaseKeyPitch
        for tone in range(self.Denominator): yield self.GetFrequency(scaleKeyId + tone, pitch)
    """
    def GetOctaveFrequencies(self, scaleKeyId, pitch=None):
        if pitch is None: pitch = self.BaseKeyPitch
        baseKeyNoteNumber = ((self.BaseKeyPitch + 1 + 1) * self.Denominator) - (self.Denominator - self.BaseKeyId)
        for tone in range(self.Denominator):
            k, p = self.Cycle(scaleKeyId + tone)
            noteNumber = k + ((pitch + p + 1) * self.Denominator) # pitch=-1〜9
#            print(noteNumber, baseKeyNoteNumber)
            yield self.BaseFrequency * math.pow(2, (noteNumber - baseKeyNoteNumber) / self.Denominator)
#            yield self.BaseFrequency * math.pow(2, (baseKeyNoteNumber + tone - baseKeyNoteNumber) / self.Denominator)
#            yield self.BaseFrequency * math.pow(2, (scaleKeyId + tone - baseKeyNoteNumber) / self.Denominator)
    """
    """
    def GetOctaveFrequencies(self, scaleKeyId):
        for tone in range(self.Denominator):
#            yield self.BaseFrequency * math.pow(2, (tone + scaleKeyId - self.BaseKeyId) / self.Denominator)
#            yield self.BaseFrequency * math.pow(2, (self.Cycle(tone + scaleKeyId)[0] - self.BaseKeyId) / self.Denominator)
#            yield self.BaseFrequency * math.pow(2, (self.Cycle(tone + scaleKeyId - self.BaseKeyId)[0]) / self.Denominator)
            yield self.BaseFrequency * math.pow(2, (self.Cycle(tone + scaleKeyId - self.BaseKeyId)[0]) / self.Denominator)
    """
    """
    構成音IDとpitchを取得する。（スケールのキーが指定した値のときの）
    """
    def GetOctaveKeyIds(self, scaleKeyId):
        for tone in range(self.Denominator):
            yield self.Cycle(scaleKeyId + tone)


if __name__ == '__main__':
    """
    # 12平均律
    EqualTemperament.Denominator = 12
    print('EqualTemperament.Denominator:', EqualTemperament.Denominator)
    for v in range((EqualTemperament.Denominator*3*-1), (EqualTemperament.Denominator*3+1)):
        print(v, EqualTemperament.Cycle(v))
    
    # 53平均律
    print()
    EqualTemperament.Denominator = 53
    print('EqualTemperament.Denominator:', EqualTemperament.Denominator)
    for v in range((EqualTemperament.Denominator*3*-1), (EqualTemperament.Denominator*3+1)):
        print(v, EqualTemperament.Cycle(v))
    """
    et = EqualTemperament()
    for f in [432, 440, 444]:
        et.BaseFrequency = f
        print(et.Frequencies)

    print()
    et.BaseFrequency = 440
    for f in [12, 19, 24, 31, 53]:
        et.Denominator = f
        print(et.Frequencies)
    
    et.Denominator = 12
    et.SetBaseKey(0, 5, 528)
    print(f'et.BaseKeyId={et.BaseKeyId}')
    print(f'et.BaseKeyPitch={et.BaseKeyPitch}')
    print(f'et.BaseFrequency={et.BaseFrequency}')

    et.SetBaseKey(9, 4, 440)
    print(f'et.BaseKeyId={et.BaseKeyId}')
    print(f'et.BaseKeyPitch={et.BaseKeyPitch}')
    print(f'et.BaseFrequency={et.BaseFrequency}')

    keyName = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'][et.BaseKeyId]
    print(f"Key: {keyName}, Pitch: {et.BaseKeyPitch}, Frequency: {et.BaseFrequency}Hz")
    print(et.Cycle(12))
#    et.SetBaseKey(-1, -1, -1)

    scaleKeyId = 0
    keyName = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'][scaleKeyId]
    print(f"ScaleKey: {keyName}")
    print(list(et.GetOctaveKeyIds(scaleKeyId)))
    print(list(et.GetOctaveFrequencies(scaleKeyId)))

    scaleKeyId = 2
    keyName = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'][scaleKeyId]
    print(f"ScaleKey: {keyName}")
    print(list(et.GetOctaveKeyIds(scaleKeyId)))
    print(list(et.GetOctaveFrequencies(scaleKeyId)))

