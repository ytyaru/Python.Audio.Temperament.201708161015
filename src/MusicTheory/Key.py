import math
#C,D,E,F,G,A,B
#ド,レ,ミ,ファ,ソ,ラ,シ
#ハ,ニ,ホ,ヘ,ト,イ,ロ
#♭,♯
#b,# (bはBの小文字だから避けたほうが賢明か)
#-,+
#https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q1273209097
#「一つの音階に二つ同じアルファベットが並んでしまうような臨時記号のつけかたはしない」
#音を記号で表現する文脈は複数ある。
# A. スケール（音階）の構成音を表現する
# B. 楽譜の音符を表現する
# B1. MMLで楽譜の音符を表現する
# Aの場合、A#でなくB♭と表現したほうがわかりやすい。スケールでは第何音が♭であるかなどが決っている。また、キー(調)が何であるかを####や♭♭などで表現することがある。これらを考慮すると、同じ音でもA#でなくB♭として表記したほうがわかりやすい場合がある。のだと思われる。
# Bの場合、MMLなら#は+,♭は-と表記する。使える文字種や可読性などを考慮した結果。

from collections import OrderedDict
class NaturalTone:
    __Names = ('C','D','E','F','G','A','B')
    __Intervals = (0, 2, 2, 1, 2, 2, 2)
    __NameValues = {'C':0, 'D':2, 'E':4, 'F':5, 'G':7, 'A':9, 'B':11} #C-Bの表記名と相対値
    NAMES = OrderedDict(zip(__Names, __Intervals))
    NAMES['C'] = 0; NAMES['D'] = 2; NAMES['C'] = 0; NAMES['C'] = 0; NAMES['C'] = 0; NAMES['C'] = 0; NAMES['C'] = 0; 
    def __call__(self, value):
        
    def ToName(self, value):
        __NameValues.keys()
    def ToValue(self, name):
        __NaturalToneNames.find(name)
        [i for i,n in enumerate(self.__NaturalToneNames) if name == n]
        sum(*[for in __NaturalToneIntervals[:)

class Key:
#    Names = ['C':0, 'C+':1, 'D-':1, 'D':2, 'D+':3, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, ]
#    NaturalTone = ('C','D','E','F','G','A','B') #幹音(かんおん)
    __NaturalToneNames = ('C','D','E','F','G','A','B')
    __NaturalToneIntervals = (0, 2, 2, 1, 2, 2, 2)
    __Tone12 = ('C','C+','D','D+','E','F','F+','G','G+','A','A+','B')
    __ACCIDENTALS = ('-','+') #♭,♯
    """
    Keyの値を取得する。
    valueが文字列なら数値を返す。数値なら文字列を返す。
    数値: 0〜11
    文字列: 'C','C+','D','D+','E','F','F+','G','G+','A','A+','B'
    """
    def __call__(self, value, accidental=None):
        if isinstance(value, int):
            if value < 0 or 11 < value: raise Exception(f'valueは0〜{len(self.__TONES)}の整数値または{self.__TONES}の文字列にしてください。')
            return self.__Tone12[value]
        if isinstance(value, str): raise Exception(f'valueは0〜{len(self.__TONES)}の整数値または{self.__TONES}の文字列にしてください。')
            if value not in __TONES:
            return self.__Tones[]

    def ToName(self, value):
    def ToValue(self, name):
        __NaturalToneNames.find(name)
        [i for i,n in enumerate(self.__NaturalToneNames) if name == n]
        sum(*[for in __NaturalToneIntervals[:)
        

class Key:
#    Names = ['C':0, 'C+':1, 'D-':1, 'D':2, 'D+':3, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, 'C':0, ]
#    NaturalTone = ('C','D','E','F','G','A','B') #幹音(かんおん)
    __TONES = ('C','C+','D','D+','E','F','F+','G','G+','A','A+','B')
    __ACCIDENTALS = ('-','+') #♭,♯
    """
    Keyの値を取得する。
    valueが文字列なら数値を返す。数値なら文字列を返す。
    数値: 0〜11
    文字列: 'C','C+','D','D+','E','F','F+','G','G+','A','A+','B'
    """
    def __call__(self, value, accidental=None):
        if isinstance(value, int):
            if value < 0 or 11 < value: raise Exception(f'valueは0〜{len(self.__TONES)}の整数値または{self.__TONES}の文字列にしてください。')
            return self.__Tones[value]
        if isinstance(value, str): raise Exception(f'valueは0〜{len(self.__TONES)}の整数値または{self.__TONES}の文字列にしてください。')
            if value not in __TONES:
            return self.__Tones[]
            
class Key:
    """
    __NAMES = ('C','D','E','F','G','A','B') # 幹音（かんおん）Natural sign　音名（英語）
    __NAMES_IT = ('Do','Re','Mi','Fa','Sol','La','Si') # 音名（イタリア）
    __NAMES_ITJP = ('ド','レ','ミ','ﾌｧ','ソ','ラ','シ') # 音名（イタリア式を日本語表記）
    __NAMES_JP = ('ハ','ニ','ホ','ヘ','ト','イ','ロ') # 音名（日本）
    __NAMES_DE = ('C','D','E','F','G','A','H') # 音名（ドイツ）
    __NAMES_FR = ('Ut','Ré','Mi','Fa','Sol','La','Si') # 音名（フランス）
    """
    # 幹音（かんおん）Natural sign
    __NAMES = {'GB': ('C','D','E','F','G','A','B'),#イギリス・アメリカ・中国
                'IT': ('Do','Re','Mi','Fa','Sol','La','Si'),#イタリア
                'ITJP': ('ド','レ','ミ','ﾌｧ','ソ','ラ','シ'),#イタリア式を日本語表記
                'JP': ('ハ','ニ','ホ','ヘ','ト','イ','ロ'),#日本
                'DE': ('C','D','E','F','G','A','H'),#ドイツ
                'FR': ('Ut','Ré','Mi','Fa','Sol','La','Si'),#フランス
                'CN12': ('黄鐘','太簇','姑洗','仲呂','林鐘','南呂','応鐘'),#中国12律
                'JP12': ('神仙','壱越','平調','勝絶','双調','黄鐘','盤渉'),#日本12律
                }
    __NAMES_DEGREE = {'Arabic':(1,2,3,4,5,6,7), 'Roman':('Ⅰ','Ⅱ','Ⅲ','Ⅳ','Ⅴ','Ⅵ','Ⅶ')}
    __IDS = (0, 2, 4, 5, 7, 9, 11) # 度数算出用。C=0とした12音の相対値。
#    __ACCIDENTALS = ('-', '+') #https://ja.wikipedia.org/wiki/%E5%A4%89%E5%8C%96%E8%A8%98%E5%8F%B7
    __ACCIDENTALS = {'Filename':('-', '+'), 'Character':('b', 's'), 'HalfWidth':('b', '#'), 'FullWidth':('♭', '♯')}
    __NAMES12 = ('C','C+','D','D+','E','F','F+','G','G+','A','A+','B')
    __DIFFS = [-9,-7,-5,-4,-2,0,2] # 十二平均律（幹音）
    
    
    def ToName(self, value, accidentals=None):
        if not isinstance(value, int) or (value < 0 or 11 < value): raise Exception(f'valueは0〜{len(self.__TONES)}の整数値にしてください。')
#        if not (isinstance(value, int) and (0 <= value and  value <= 11)): raise Exception(f'valueは0〜{len(self.__TONES)}の整数値にしてください。')
#        a = '#' if None is accidentals else accidentals
#        self.__GetAccidentalsKeyAndIndex(a)
        key, idx = self.__GetAccidentalsKeyAndIndex('#' if None is accidentals else accidentals)
        __ACCIDENTALS[key][idx]
        if accidentals in 
        return __NAMES12[value]

    def __GetAccidentalsKeyAndIndex(self, accidentals):
        for k in __ACCIDENTALS.keys():
            for i,v in enumerate(__ACCIDENTALS[k]):
                if accidentals == v: return k,i
        raise Exception('指定した変化記号{accidentals}は存在しません。')





    def ToValue(self, name, typ='GB'):
        
    """
    C = 0
    Cs = 1
    D = 2
    Ds = 3
    E = 4
    F = 5
    Fs = 6
    G = 7
    Gs = 8
    A = 9
    As = 10
    B = 11
    """
    def __init__(self):
        self.__name = None
        self.__id = None
        self.__diff = None
        self.__frequency = None

    @classmethod
    def ValueToName(cls, value): return cls.__NAMES12[value]

    #音名
    @property
    def Names(self): return self.__NAMES
    #12音名
    @property
    def Names12(self): return self.__NAMES12

    #音のアルファベット表記名
    @property
    def Name(self): return self.__name
    #ド(C)音を0とした相対位置
    @property
    def Id(self): return self.__id
    #十二平均律の基準音440Hz(ラ,A)との差分
    @property
    def Diff(self): return self.__diff
    
    def Get(self, name):
        if not isinstance(name, str): raise Exception('引数nameはstr型にしてください。')
        if self.__validate_name(name):
            self.__name = name
            self.__id = self.__get_id(name)
            self.__diff = self.__get_diff(name)
            return self.__id
        return -1

    def __validate_name(self, name):
        if 1 == len(name): return name.upper() in self.__NAMES
        elif 2 == len(name):
            if name[0].upper() in self.__NAMES and name[1] in self.__ACCIDENTALS: return True
            else: return False
        else: raise Exception('引数nameは長さ1または2にしてください。')

    def __get_id(self, name):
        if 1 == len(name): return self.__NAMES12.index(name[0].upper())
        elif 2 == len(name):
            v = self.__IDS[self.__NAMES.index(name[0].upper())]
            if '+' == name[1]: v += 1
            elif '-' == name[1]: v -= 1
            if v < 0: v = len(self.__NAMES12)-1
            elif len(self.__NAMES12)-1 < v: v = 0
            return v
    
    def __get_diff(self, name):
        if 1 == len(name): return self.__DIFFS[self.__NAMES.index(name[0].upper())]
        elif 2 == len(name):
            v = self.__DIFFS[self.__NAMES.index(name[0].upper())]
            if '+' == name[1]: v += 1
            elif '-' == name[1]: v -= 1
            if v < self.__DIFFS[0]: v = self.__DIFFS[-1]
            elif self.__DIFFS[-1] < v: v = self.__DIFFS[0]
            return v

if __name__ == '__main__':
    # 12音は21*2=42通りの表現方法がある。
    k = Key()
    for n in ('C-','C','C+','D-','D','D+','E-','E','E+','F-','F','F+','G-','G','G+','A-','A','A+','B-','B','B+'):
        k.Get(n)
        print('{0:<2} {1:>2} {2:.1f}'.format(k.Name, k.Value, k.Frequency))
    for n in ('c-','c','c+','d-','d','d+','e-','e','e+','f-','f','f+','g-','g','g+','a-','a','a+','b-','b','b+'):
        k.Get(n)
        print('{0:<2} {1:>2} {2:.1f}'.format(k.Name, k.Value, k.Frequency))
        
