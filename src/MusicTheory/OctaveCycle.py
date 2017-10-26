class OctaveCycle:
    Length = 12# 1オクターブあたりのノート数
    def __init__(self, length=12):
        self.Length = length
#        self.__toneLength = length
    
    """
    1オクターブあたりの音に識別番号(0〜Length-1)を振る。
    """
    @classmethod
    def Cycle(cls, keyId, pitch):
        p = pitch + (keyId // 12)
        if 0 <= keyId:
            if 9 < p: raise Exception(f'pitchの最大値9を超えてしまいます。9以下になるようにしてください。')
            return keyId % 12, p
        elif keyId < 0:
            if p < -1: raise Exception(f'pitchの最小値-1を超えてしまいます。-1以上になるようにしてください。')
            return (12 + keyId) % 12, p

    """
    C-1を0番としたノート番号を返す。
    keyId: 1オクターブ12音なら0〜11の整数値。
    pitch: -1〜9までの整数値
    """
    @classmethod
    def NoteNumber(cls, keyId, pitch):
        return keyId + ((pitch + 1) * self.__denominator) # pitch=-1〜9

