#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#http://www.chaco2008.com/theory/1-3_majorscale.html
#http://www.chaco2008.com/theory/2-3_minorscale.html
#メジャー・スケール=全,全,半,全,全,全,半
#マイナー・スケール=全,半,全,全,半,全,全
#全音=2, 半音=1
#CMajor=C,D,E,F,G,A,B
#Cminor=C,D,D#,F,G,G#,A#
#スペイン音階はフラメンコなどの音楽で多用される。
#フリジアン・スケールにMajor 3rdを加えたスケール
class SpainScale:
    def __init__(self):
        #1 b2 b3 3 4 5 b6 b7
        #C Db Eb E F G Ab Bb
        # 1  2  1 1 2 1  2
        self.__intervals = [1,2,1,1,2,1,2]
    @property
    def Intervals(self): return self.__intervals


if __name__ == '__main__':
    s = SpainScale()
    print('========== スペイン・スケール ==========')
    print('s.Intervals', s.Intervals)

