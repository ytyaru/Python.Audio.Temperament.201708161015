#!python3.6
#coding:utf-8
#https://ja.wikipedia.org/wiki/%E7%B4%94%E6%AD%A3%E5%BE%8B
#http://www.asahi-net.or.jp/~HB9T-KTD/music/Japan/Research/Genre/Tuning/tuning_just.html
#純正律(算出方法はメジャースケールの場合である)
class JustIntonation:
    def __init__(self):
        self.__DENOMINATOR = 7
        self.__BaseFrequency = 440 #基準となる音をA4(ラ)とし、周波数を440として算出する
        self.__BaseKeyId = 9 #A (1オクターブ12音なら0〜11の値。[C,C#,D,D#,E,F,F#,G,G#,A,A#,B]の12音とすると9=A)
        self.__BaseKeyPitch = 4 #-1〜9（A4=440Hz。A3は220Hzになるし、A5は880Hzになる）
        self.__Frequencies = [] #C,D,E,F,G,A,Bの7音の周波数
        self.__Rate = [1, 9/8, 5/4, 4/3, 3/2, 5/3, 15/8] #メジャースケールにおける7音の比率
        self.__calcFrequencies()
    @property
    def Denominator(self): return self.__DENOMINATOR
    @property
    def BaseKeyId(self): return self.__BaseKeyId
    @property
    def BaseKeyPitch(self): return self.__BaseKeyPitch
    def SetBaseKey(self, keyId, pitch, hz):
#        if not (isinstance(keyId, int) and -1 < keyId and keyId < self.Denominator): raise Exception(f'keyIdは0〜{self.Denominator-1}の整数値(int型)にしてください。')
#        if not isinstance(pitch, int): raise Exception('pitchはint型にしてください。')
#        if hz <= 0: raise Exception('hzは0より大きい数値にしてください。')
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
    def __calcFrequencies(self):
        self.Frequencies.clear()
        for rate in self.__Rate: self.Frequencies.append(self.__BaseFrequency * rate)

if __name__ == '__main__':
    ji = JustIntonation()
    print(ji.Frequencies)
    print('---------- 1オクターブ下 ----------')
    print([f/2 for f in ji.Frequencies])
    print('---------- 1オクターブ上 ----------')
    print([f*2 for f in ji.Frequencies])

    scaleKeyId = 9
    ji.SetBaseKey(scaleKeyId, 4, 432)
    keyName = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'][scaleKeyId]
    print(f"Key: {keyName}, Pitch: {ji.BaseKeyPitch}, Frequency: {ji.BaseFrequency}Hz")
    print(ji.Frequencies)
    
    scaleKeyId = 0
    ji.SetBaseKey(scaleKeyId, 3, 128)# C3=128Hz
    keyName = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'][scaleKeyId]
    print(f"Key: {keyName}, Pitch: {ji.BaseKeyPitch}, Frequency: {ji.BaseFrequency}Hz")
    print(ji.Frequencies)
    print([f*2 for f in ji.Frequencies])
    print([f*3 for f in ji.Frequencies])

