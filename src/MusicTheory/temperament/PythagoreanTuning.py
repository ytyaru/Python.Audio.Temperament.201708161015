#https://ja.wikipedia.org/wiki/%E3%83%94%E3%82%BF%E3%82%B4%E3%83%A9%E3%82%B9%E9%9F%B3%E5%BE%8B
#ピタゴラス音律
#減5度と増4度は平均律では同一音だが、ピタゴラス音律では約23.46セント≒1/4半音の差が生じる。この差をピタゴラスコンマと呼ぶ。
#この音程の外れた五度による和音は、顕著なうなりを生じるため、狼の吠声に例えてウルフの五度と呼ばれる。
#結果、ピタゴラス音律では演奏可能な調は制限される。
class PythagoreanTuning:
    def __init__(self):
        self.__DENOMINATOR = 12
        self.__BaseFrequency = 440 #基準となる音をA4(ラ)とし、周波数を440として算出する
        self.__BaseKeyId = 9 #A (1オクターブ12音なら0〜11の値。[C,C#,D,D#,E,F,F#,G,G#,A,A#,B]の12音とすると9=A)
        self.__BaseKeyPitch = 4 #-1〜9（A4=440Hz。A3は220Hzになるし、A5は880Hzになる）
        self.__Frequencies = []
        # 減5, 短2, 短6, 短3, 短7, 4, 1, 5, 長2, 長6, 長3, 長7, 増4
        self.__calcFrequencies()
    
    def __calcFrequencies(self):
        self.__Frequencies.clear()
        self.__Frequencies.extend([f for f in self.__calcMinusInOctave()])
        self.__Frequencies.extend([f for f in self.__calcPlusInOctave()])
        self.__Frequencies.sort()
    
    # return: [4, 短7, 短3, 短6, 短2] 減5は増4と同じはずだがピタゴラス音律においては別の音になってしまう（ピタゴラスコンマ）ので省く
    def __calcMinusInOctave(self):
        for x, y in ((1,1), (2,2), (3,2), (4,3), (5,3)):
            yield (((2/3)**x) * (2**y)) * self.__BaseFrequency
    
    # return: [1, 5, 長2, 長6, 長3, 長7, 増4]
    def __calcPlusInOctave(self):
        yield self.__BaseFrequency #1度
        yield 3/2 * self.__BaseFrequency #5度
        for x, y in ((2,1), (3,1), (4,2), (5,2), (6,3)):
            yield (((3/2)**x) * (1/2**y)) * self.__BaseFrequency

    @property
    def Denominator(self): return self.__DENOMINATOR
    @property
    def BaseKeyId(self): return self.__BaseKeyId
    @property
    def BaseKeyPitch(self): return self.__BaseKeyPitch
    def SetBaseKey(self, keyId, pitch, hz):
        if not (isinstance(keyId, int) and -1 < keyId and keyId < self.__DENOMINATOR): raise Exception(f'keyIdは0〜{self.Denominator-1}の整数値(int型)にしてください。')
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
    def Frequencies(self): return self.__Frequencies

    """
    同一オクターブにあるKey値とオクターブ増減値を返す。: tuple(key,octave)
    引数|返却
    ----|----
    -1|(11, -1)
     0|(0, 0)
     1|(1, 0)
    11|(11, 0)
    12|(0, 1)
    """
    def Cycle(self, value): return ((value % self.Denominator), (value // self.Denominator))
    def GetFrequency(self, keyId, pitch):
        k,p = self.Cycle(self.__DENOMINATOR - self.__BaseKeyId + keyId)
#        return self.Frequencies[k] * (2**p)#p=0,1,2,3,4,...-1,-2,-3
        return self.Frequencies[k] * (2 ** (pitch + p - 1 - self.__BaseKeyPitch))
        """
        if p <= 0: return self.Frequencies[k] * (p+1)
        else: return self.Frequencies[k] / (abs(p)+1)
        2**(n)
        if p == 0: self.Frequencies[k]
        elif p < 0: self.Frequencies[k] * ((self.__BaseKeyPitch+p+1) - self.__BaseKeyPitch)
        elif 0 < p: 
        return self.Frequencies[k] * (2 * (self.__BaseKeyPitch + p))

        self.__Frequencies[]#__FrequenciesはBaseKeyId(A音)を0とした値に対してkeyIdはC音を0としている。
        #base=A
        #A,A#,B,C,C#,D,D#,E,F,F#,G,G#
        #
        baseKeyNoteNumber = ((self.BaseKeyPitch + 1 + 1) * self.Denominator) - (self.Denominator - self.BaseKeyId)
        k, p = self.Cycle(keyId)
        noteNumber = k + ((pitch + p + 1) * self.Denominator) # pitch=-1〜9
        return self.BaseFrequency * math.pow(2, (noteNumber - baseKeyNoteNumber) / self.Denominator)
        """


if __name__ == '__main__':
    def GetKeyName(keyId): return ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'][keyId]
    
    pt = PythagoreanTuning()
    """
    print(pt.Frequencies)
    print('---------- 1オクターブ下 ----------')
    print([f/2 for f in pt.Frequencies])
    print('---------- 1オクターブ上 ----------')
    print([f*2 for f in pt.Frequencies])

    baseKeyId = 9
    pt.SetBaseKey(baseKeyId, 4, 432)
    keyName = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'][baseKeyId]
    print(f"Key: {keyName}, Pitch: {pt.BaseKeyPitch}, Frequency: {pt.BaseFrequency}Hz")
    print(pt.Frequencies)
    
    baseKeyId = 0
    pt.SetBaseKey(baseKeyId, 3, 128)# C3=128Hz
    keyName = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'][baseKeyId]
    print(f"Key: {keyName}, Pitch: {pt.BaseKeyPitch}, Frequency: {pt.BaseFrequency}Hz")
    print(pt.Frequencies)
    print([f*2 for f in pt.Frequencies])
    print([f*3 for f in pt.Frequencies])
    """
    baseKeyId = 9
    pt.SetBaseKey(baseKeyId, 4, 440)
    print(f"Key: {GetKeyName(baseKeyId)}, Pitch: {pt.BaseKeyPitch}, Frequency: {pt.BaseFrequency}Hz")
    print(pt.Frequencies)
    for pitch in range(-1, 10):
        print(f'----- pitch = {pitch} -----')
        for keyId in range(pt.Denominator):
            print('{0:2}: {1}'.format(GetKeyName(keyId), pt.GetFrequency(keyId, pitch)))
            
