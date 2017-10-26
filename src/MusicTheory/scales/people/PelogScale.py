#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#https://ja.wikipedia.org/wiki/%E3%83%9E%E3%82%AB%E3%83%BC%E3%83%A0
#インドネシアの音階(ペロッグ)
#本来はおおざっぱに1オクターブを5つに不等分したもの。「広い音程」と「狭い音程」の2種の音程がある。狭い音程+狭い音程+広い音程+狭い音程+広い音程。C#, D, E, G#, A, C#もしくはC#, D, E, G, A, C#程度の感じ。
class PelogScale:
    def __init__(self):
        #C Db Eb G Ab
        # 1  2  4 1
        self.__intervals = [[1,2,4,1]] #(1/4音さげるのを表現できない)
        self.__names = ['ヨナ抜き長音階', 'ヨナ抜き短音階', 'ニロ抜き短音階', 'ニロ抜き長音階', '雲井音階', '岩戸音階']
    
    @property
    def Intervals(self): return self.__intervals


if __name__ == '__main__':
    s = PelogScale()
    print('========== インドネシアの音階(ペロッグ)・スケール ==========')
    print('s.Intervals', s.Intervals)
