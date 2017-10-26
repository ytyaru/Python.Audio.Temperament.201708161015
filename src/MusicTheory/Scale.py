#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
import MusicTheory.EqualTemperament
#import MusicTheory.Key
import MusicTheory.ToneAccidentaler
import MusicTheory.ToneFrequency
import MusicTheory.scales.MajorScales
"""
根音を基準に異なるキーのスケールを作ろうとしていた。が、これはメジャー、マイナースケールにのみ通じる手法だった。
Scale関係は現在、完全に使い物にならない状況。
五度圏表クラスを作成し、そこから各スケールの構成音を生成したほうがいいかもしれない。コード進行などにも応用できそうだから。
ただ、実装が大変になる。
"""
#Scale,Key,KeyPitchの3つを指定して周波数の絶対値を算出する。（12平均律）
class Scale:
    def __init__(self):
        self.__scales = []
        self.__scale = MusicTheory.scales.MajorScales.MajorScales()
        self.__frequencies = []
        self.__keyId = 0 # 0=C音。
        self.__key_pitch = 4 # キーの音の高さ(C4等)
        self.__et = MusicTheory.EqualTemperament.EqualTemperament()

    @property
    def Scales(self): return self.__scales
    @property
    def Scale(self): return self.__scale
    @Scale.setter
    def Scale(self, v):
        if hasattr(v, 'Intervals') and isinstance(v.Intervals, (tuple,list)):
            self.__scale = v
            self.__SetIntervals()
    @property
    def KeyId(self): return self.__keyId
    @KeyId.setter
    def KeyId(self, v):
        if v < len(self.__et.Ids): self.__keyId = v; self.__SetIntervals();
    @property
    def KeyPitch(self): return self.__key_pitch
    @property
    def Frequencies(self): return self.__frequencies

    def __SetIntervals(self):
        self.Scales.clear()
        self.Frequencies.clear()        
        ta = MusicTheory.ToneAccidentaler.ToneAccidentaler()
        self.__scales.append(self.__keyId)
        tf = MusicTheory.ToneFrequency.ToneFrequency()
        self.__frequencies.append(tf.ToFrequencyFromKeyId(self.__keyId, self.__key_pitch)[0]); 
        keyId = self.__keyId
        pitch = self.__key_pitch
        for interval in self.__scale.Intervals:
            keyId += interval
            keyId, pitch = ta.CycleTone(keyId, pitch)
            self.__scales.append(keyId)
            self.__frequencies.append(tf.ToFrequencyFromKeyId(keyId, pitch)[0]); 

