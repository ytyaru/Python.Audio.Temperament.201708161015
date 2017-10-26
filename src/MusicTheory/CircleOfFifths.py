from MusicTheory.temperament.EqualTemperament import EqualTemperament
import MusicTheory.ToneAccidentaler
"""
五度圏表
音律12平均律(12音)における音階(Scale)を算出する。ただし長調(Major)・短調(Minor)のみ。
つまり、各音階ごとの各調における構成音と調号を算出する。(CMajor=C,D,E,F,G,A,B等)
また、右隣=五度、左隣=四度の関係であることから、コード進行の算出にも使える。
http://ytyaru.hatenablog.com/entry/2018/09/01/000000
"""
class CircleOfFifths:
    def __init__(self):
        self.__MAJOR_SCALE_INTERVALS = (2,2,1,2,2,2,1)
        self.__base_key = 0 # 0=C=ドの音
        self.__ToneAccidentaler = MusicTheory.ToneAccidentaler.ToneAccidentaler()
        self.__major_scales = []
    """
    引数:
      keyId:0〜11。C=0。
      isMinor:False/True。将来的にはintervalsに変更し、ハーモニック・マイナーや、ペンタトニック(5音)などの各種スケールにも対応したい。
    戻り値:
    """
    def GetScales(self, keyId=0, isMinor=False):
        for scales in self.__GetFifthKeysScales():
            if scales[0] == keyId: return scales
    """
    def Get(self, keyId=0, isMinor=False, pitch=4):
        scales = []
        scales.append(self.__ToneAccidentaler.CycleTone(keyId, pitch))#(keyId,pitch)のタプル
        l = [0]
        l.extend(self.__MAJOR_SCALE_INTERVALS)
        k = keyId
        for interval in l:
            k += interval
            scales.append(self.__ToneAccidentaler.CycleTone(k, pitch))#(keyId,pitch)のタプル
        return scales
    """
    
    # 完全5度ずつ移動したキーの配列を取得する。[C,G,D,A,E,B,F#,Db,Ab,Eb,Bb,F]
    def __GetFifthKeys(self):
        # C D E F G A B
        # 0 2 4 5 7 9 11
        keyId = 0
        for i in range(12):
            keyId += 7 #完全5度(半音7つ分)
            yield EqualTemperament.Cycle(keyId)[0]
    def __GetFifthKeysScales(self):
        for key in self.__GetFifthKeys(): yield self.__GetMajorScales(key)
    def __GetMajorScales(self, keyId=0, pitch=4):
        scales = []
        keyId = EqualTemperament.Cycle(keyId)[0]
        l = [0]; l.extend(self.__MAJOR_SCALE_INTERVALS);
        for interval in l:
            keyId += interval
            scales.append(EqualTemperament.Cycle(keyId)[0])
        return scales

