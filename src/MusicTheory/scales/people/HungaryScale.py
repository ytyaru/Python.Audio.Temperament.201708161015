#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#http://www.chaco2008.com/theory/1-3_majorscale.html
#http://www.chaco2008.com/theory/2-3_minorscale.html
#メジャー・スケール=全,全,半,全,全,全,半
#マイナー・スケール=全,半,全,全,半,全,全
#全音=2, 半音=1
#CMajor=C,D,E,F,G,A,B
#Cminor=C,D,D#,F,G,G#,A#
#ハンガリーなどの民謡で使われるスケール。
#メロディック・マイナーを♯4にしたスケール
class HungaryScale:
    def __init__(self):
        #1 2 b3 #4 5 6 7
        #C D Eb F# G A B
        # 2 1  3  1 2 2
        self.__intervals = [2,1,3,1,2,2]
    @property
    def Intervals(self): return self.__intervals


if __name__ == '__main__':
    s = HungaryScale()
    print('========== ハンガリー・スケール ==========')
    print('s.Intervals', s.Intervals)

