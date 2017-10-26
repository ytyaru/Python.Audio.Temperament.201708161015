#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#https://ja.wikipedia.org/wiki/%E3%83%9E%E3%82%AB%E3%83%BC%E3%83%A0
#アラブの音階(マカーム)
#西洋音楽の音階と比べると、中立音程（3/4音など)の使用が特徴的である。
class SpainScale:
    def __init__(self):
        #1 2 q3 4 5 6 7   (q=1/4音下げる)
        #C D Eq F G A Bq
        # 2 2q 1 2 2 2q
        self.__intervals = [1,2,1,1,2,1,2] # (1/4音さげるのを表現できない)
    @property
    def Intervals(self): return self.__intervals


if __name__ == '__main__':
    s = SpainScale()
    print('========== スペイン・スケール ==========')
    print('s.Intervals', s.Intervals)

