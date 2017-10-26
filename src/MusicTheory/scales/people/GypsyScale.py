#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#http://www.chaco2008.com/theory/1-3_majorscale.html
#http://www.chaco2008.com/theory/2-3_minorscale.html
#メジャー・スケール=全,全,半,全,全,全,半
#マイナー・スケール=全,半,全,全,半,全,全
#全音=2, 半音=1
#CMajor=C,D,E,F,G,A,B
#Cminor=C,D,D#,F,G,G#,A#
#ジプシー音楽などで多用される。
#ハーモニック・マイナー・パーフェクト5th・ビロウ・スケールを♮7にしたスケール
class GypsyScale:
    def __init__(self):
        #1 b2 3 4 5 b6 7
        #C Db E F G Ab B
        # 1  3 1 2 1  3
        self.__intervals = [1,3,1,2,1,3]
    @property
    def Intervals(self): return self.__intervals


if __name__ == '__main__':
    s = GypsyScale()
    print('========== ジプシー・スケール ==========')
    print('s.Intervals', s.Intervals)

