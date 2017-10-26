#!python3.6
import math
import MusicTheory.NaturalTone
import MusicTheory.Accidental
#NaturalToneに変化記号+,-を付与した値や名前を返す
class ToneAccidentaler:
    def __init__(self):
        self.__NatulasTone = MusicTheory.NaturalTone.NaturalTone()
        self.__Accidental = MusicTheory.Accidental.Accidental()
    # tone: C+,B-のような形式。G++など複数の変化記号も付与できる。
    #   1文字目: NaturalTone
    #   2文字目以降: 任意。Accidentalの文字。3文字目以降は2文字目が連続したもの
    # pitch: 音高。-1〜9の整数値。
    def ToValue(self, tone:str, pitch:int=4) -> int:
        if pitch < -1 or 9 < pitch: raise Exception(f'pitchは-1〜9までの整数値にしてください。: {pitch}')
        return self.CycleTone(
            self.__NatulasTone.ToValue(tone[0]) + sum([self.__Accidental.ToValue(a) for a in tone[1:]]),
            pitch)
    
    # ToneとPitchの算出
    # Toneが0〜11の範囲を超えたとき、Pitchを変化させてToneは0〜11にする。
    def CycleTone(self, toneValue, pitch):
        # value: tone, pitch, pitchName
        # -12   0, -2  B2
        # -11   1, -1  C3
        # - 2: 10, -1  A#3
        # - 1: 11, -1  B3
        #   0:  0,  0  C4
        #   1:  1,  0  C#4
        #  11: 11,  0  B4
        #  12:  0, +1  C5
#        if 0 <= toneValue: return toneValue % 12, pitch + (toneValue // 12)
#        elif toneValue < 0: return (12 + toneValue) % 12, pitch + (toneValue // 12)
        p = pitch + (toneValue // 12)
        if 0 <= toneValue:
            if 9 < p: raise Exception(f'pitchの最大値9を超えてしまいます。9以下になるようにしてください。')
            return toneValue % 12, p
        elif toneValue < 0:
            if p < -1: raise Exception(f'pitchの最小値-1を超えてしまいます。-1以上になるようにしてください。')
            return (12 + toneValue) % 12, p

