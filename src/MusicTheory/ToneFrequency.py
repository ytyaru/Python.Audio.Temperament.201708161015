#!python3.6
#https://ja.wikipedia.org/wiki/%E9%9F%B3%E5%BE%8B
#https://ja.wikipedia.org/wiki/%E5%B9%B3%E5%9D%87%E5%BE%8B#.E5.8D.81.E4.BA.8C.E5.B9.B3.E5.9D.87.E5.BE.8B
#https://ja.wikipedia.org/wiki/%E7%B4%94%E6%AD%A3%E5%BE%8B
#各音律の印象：平均律：薄くてキンキンする。ピタゴラス：1音1音が目立ってメロディアス。以外に良く一番好きかも。純正律：ズレている。音痴。中全音律：平均律の下位互換
#http://mvsica.sakura.ne.jp/eki/ekiinfo/tuning.html
#各音律の周波数を算出するにはセント値の算出が必要か。（1オクターブ=1200セント、1半音=100セント）
import math
import MusicTheory.EqualTemperament
import MusicTheory.ToneAccidentaler
#音高12値(0〜11)と音高(pitch。-1〜9)から周波数(440Hz等)を算出する。
class ToneFrequency:
    def __init__(self):
        self.__A4_PITCH = 440
        # 音律は十二平均律が最善と思われる。他の音律だとオクターブ音の算出や転調できないなどの問題がある
        self.__EqualTemperament = MusicTheory.EqualTemperament.EqualTemperament(self.__A4_PITCH)
        self.__ToneAccidentaler = MusicTheory.ToneAccidentaler.ToneAccidentaler()
    # tone: `C+++-1`の場合、`-1`の`-`部分が変化記号なのか音高なのか判別できない！
    #       `+`を`#`にすると、`-`を`b`にできる。しかし`b`は`B`の小文字である。`B`は音名`シ`に該当する。紛らわしい。
    #       MMLなら`V=-1`のようにして音高(pitch)を指定できるので`C+-1`(C#-1)のような指定はせずに済む。MIDIは`C#-1`なので`C+-1`とせずに済む。Pythonなら第一引数`C+`,第二引数`-1`にできるので区別可能。
    def ToFrequency(self, tone:str, pitch:int=4) -> int:
        keyId, _pitch = self.__ToneAccidentaler.ToValue(tone, pitch) # `C--4`を`(10, 3)`に変換する
        return self.__EqualTemperament.FromId(keyId, pitch), keyId, _pitch #周波数 `〜Hz`に変換する        
    def ToFrequencyFromKeyId(self, keyId:str, pitch:int=4) -> int:
        k, p = self.__ToneAccidentaler.CycleTone(keyId, pitch)
        return self.__EqualTemperament.FromId(k, p), k, p #周波数 `〜Hz`に変換する
        
    @property
    def EqualTemperament(self): return self.__EqualTemperament

