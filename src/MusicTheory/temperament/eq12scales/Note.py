#音律 = EqualTemperament
#基音Hz = 440Hz
#基音Id = A
#基音Pitch = 4
#Scale = Major
#ScaleKey = C
#



import MusicTheory.temperament.EqualTemperament
#12平均律における12音の名前指定で周波数を取得する
#音名(key),音高(pitch)から周波数を返す
class Frequency:
    def __init__(self):
        self.__EqualTemperament = MusicTheory.temperament.EqualTemperament.EqualTemperament()
    def Get(self): pass
    @staticmethod
    def Get(): pass
    """
    keyId: 12平均律ならkeyIdは0〜11。超過したらループして0〜11の値にする。
    """
    @classmethod
    def Get(cls, keyId, pitch):
        
        self.__EqualTemperament.Frequencies

