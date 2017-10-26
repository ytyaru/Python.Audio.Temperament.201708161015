#!python3.6
#coding:utf-8
import time
import Wave.Player
import Wave.Sampler
import Wave.BaseWaveMaker
import Wave.WaveFile
#import MusicTheory.EqualTemperament
import MusicTheory.temperament.JustIntonation
import pathlib
import numpy

#波形の加算とクリッピング
def Addition(src):
    res = numpy.array([0] * len(src[0])) #ダミーの空配列
    for s in src:
        res = res + s
        res *= 0.5
    return res

#パワーコード（基音＋完全5度）
def PowerChord(wm:Wave.BaseWaveMaker.BaseWaveMaker, ji:MusicTheory.temperament.JustIntonation):
    src = []
    src.append(wm.Sin(a=1, fs=8000, f0=ji.Frequencies[0], sec=4))
    src.append(wm.Sin(a=1, fs=8000, f0=ji.Frequencies[4], sec=4))
    res = numpy.array([0] * len(src[0])) #ダミーの空配列
    return Addition(src)

#長三和音（基音＋長3度＋完全5度）
def MajorTriadChord(wm:Wave.BaseWaveMaker.BaseWaveMaker, ji:MusicTheory.temperament.JustIntonation):
    src = []
    src.append(wm.Sin(a=1, fs=8000, f0=ji.Frequencies[0], sec=4))
    src.append(wm.Sin(a=1, fs=8000, f0=ji.Frequencies[2], sec=4))
    src.append(wm.Sin(a=1, fs=8000, f0=ji.Frequencies[4], sec=4))
    res = numpy.array([0] * len(src[0])) #ダミーの空配列
    return Addition(src)

#四和音以上は平均律のときに有効な和音らしい。純正律は三和音が最も美しく響く音律らしい。

#再生とファイル生成
def PlayAndMake(BaseFrequency=440, pattern=None):
    PATTERNS = {'power': PowerChord, 'major': MajorTriadChord}
    if pattern not in PATTERNS: raise Exception(f'{pattern}は無効値です。patternは次のいずれかにして下さい: {PATTERNS.keys()}')
    
    wm = Wave.BaseWaveMaker.BaseWaveMaker()
    sampler = Wave.Sampler.Sampler()
    ji = MusicTheory.temperament.JustIntonation.JustIntonation()
    wf = Wave.WaveFile.WaveFile()
    wf.BasePath = pathlib.PurePath(f'../res/chords/{pattern}/JustIntonation/')
    p = Wave.Player.Player()
    p.Open()

    ji.BaseFrequency = BaseFrequency
    print(f'BaseFrequency: {ji.BaseFrequency} Hz')
    print(ji.Frequencies)

    p.Play(sampler.Sampling(PATTERNS[pattern](wm, ji)))
    wf.Write(sampler.Sampling(PATTERNS[pattern](wm, ji)), filename=str(BaseFrequency))
    
    p.Close()
    
for p in ['power', 'major']:
    PlayAndMake(432, p) #宇宙の規則性と数学的に一貫している http://tabi-labo.com/156689/music-a432
    PlayAndMake(440, p) #デビルトーン(世界基準。陰謀論。)
    PlayAndMake(528, p) #ソルフェジオ周波数
