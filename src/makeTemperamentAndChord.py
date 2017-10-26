#!python3.6
#coding:utf-8
import time
import Wave.Player
import Wave.Sampler
import Wave.BaseWaveMaker
import Wave.WaveFile
import MusicTheory.temperament.EqualTemperament
import MusicTheory.temperament.JustIntonation
import MusicTheory.temperament.PythagoreanTuning
import pathlib
import numpy

#音律の構成音データ生成
class ScaleMaker:
    def __init__(self, wm:Wave.BaseWaveMaker.BaseWaveMaker):
        self.__wm = wm

    def Scales(self, temperament):
        for f0 in temperament.Frequencies:
            yield self.__wm.Sin(a=1, fs=8000, f0=f0, sec=0.5)

#和音データ生成
class ChordMaker:
    def __init__(self, wm:Wave.BaseWaveMaker.BaseWaveMaker):
        self.__wm = wm

    #パワーコード（基音＋完全5度）
    def PowerChord(self, temperament):
        src = []
        src.append(self.__wm.Sin(a=1, fs=8000, f0=temperament.Frequencies[0], sec=4))
        src.append(self.__wm.Sin(a=1, fs=8000, f0=temperament.Frequencies[4], sec=4))
        res = numpy.array([0] * len(src[0])) #ダミーの空配列
        return self.__Addition(src)

    #長三和音（基音＋長3度＋完全5度）
    def MajorTriadChord(self, temperament):
        src = []
        src.append(self.__wm.Sin(a=1, fs=8000, f0=temperament.Frequencies[0], sec=4))
        src.append(self.__wm.Sin(a=1, fs=8000, f0=temperament.Frequencies[2], sec=4))
        src.append(self.__wm.Sin(a=1, fs=8000, f0=temperament.Frequencies[4], sec=4))
        res = numpy.array([0] * len(src[0])) #ダミーの空配列
        return self.__Addition(src)
        
    #波形の加算とクリッピング
    def __Addition(self, src):
        res = numpy.array([0] * len(src[0])) #ダミーの空配列
        for s in src:
            res = res + s
            res *= 0.5
        return res

    #四和音以上は平均律のときに有効な和音らしい。純正律は三和音が最も美しく響く音律らしい。

class PlayAndMaker:
    #再生とファイル生成
    @staticmethod
    def Run(temperament):
        wm = Wave.BaseWaveMaker.BaseWaveMaker()
        sampler = Wave.Sampler.Sampler()
        ji = MusicTheory.temperament.JustIntonation.JustIntonation()
        wf = Wave.WaveFile.WaveFile()
        p = Wave.Player.Player()
        p.Open()

        print(f'BaseFrequency: {temperament.BaseFrequency} Hz')
        print(temperament.Frequencies)
        
        #コード生成
#        p.Play(sampler.Sampling(PATTERNS[pattern](wm, ji)))
        cm = ChordMaker(wm)
        wf.BasePath = pathlib.PurePath(f'../res/chords/power/{temperament.__class__.__name__}/')
        wf.Write(sampler.Sampling(cm.PowerChord(temperament)), filename=f'{temperament.BaseFrequency}')
        wf.BasePath = pathlib.PurePath(f'../res/chords/major/{temperament.__class__.__name__}/')
        wf.Write(sampler.Sampling(cm.PowerChord(temperament)), filename=f'{temperament.BaseFrequency}')

        #スケールの構成音生成
        sm = ScaleMaker(wm)
        wf.BasePath = pathlib.PurePath(f'../res/scales/{temperament.__class__.__name__}/')
        wf.Write(b''.join([sampler.Sampling(f) for f in sm.Scales(temperament)]), filename=f'{temperament.BaseFrequency}')
        
        p.Close()


for temperament in [
    MusicTheory.temperament.EqualTemperament.EqualTemperament(), 
    MusicTheory.temperament.JustIntonation.JustIntonation(), 
    MusicTheory.temperament.PythagoreanTuning.PythagoreanTuning()]:
    print('---------- ' + temperament.__class__.__name__ + ' ----------')
    for baseF in [432, 440, 444]:
        temperament.BaseFrequency = baseF
        PlayAndMaker.Run(temperament)
