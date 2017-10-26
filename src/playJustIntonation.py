#!python3.6
#coding:utf-8
import time
import Wave.Player
import Wave.Sampler
import Wave.BaseWaveMaker
import Wave.WaveFile
#import MusicTheory.EqualTemperament
import MusicTheory.temperament.JustIntonation
#import MusicTheory.Scale
#import MusicTheory.tempo
import pathlib

def PlayAndMake(BaseFrequency=440, filename=None):
    wm = Wave.BaseWaveMaker.BaseWaveMaker()
    sampler = Wave.Sampler.Sampler()
    ji = MusicTheory.temperament.JustIntonation.JustIntonation()
    wf = Wave.WaveFile.WaveFile()
    wf.BasePath = pathlib.PurePath('../res/temperaments/JustIntonation/')
    p = Wave.Player.Player()
    p.Open()

    ji.BaseFrequency = BaseFrequency
    print(f'BaseFrequency: {ji.BaseFrequency} Hz')
    #    timebase.Metre=(2,4)
    #    print(f'拍子={timebase.Metre}')
    print(ji.Frequencies)
    for f0 in ji.Frequencies:
        p.Play(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=f0, sec=0.5)))
    wav = []
    for f0 in ji.Frequencies:
        wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=f0, sec=0.5)))
    if not filename: filename = str(BaseFrequency)
    wf.Write(b''.join(wav), filename=filename)

    p.Close()


PlayAndMake(440) #デビルトーン(世界基準。陰謀論。)
PlayAndMake(528) #ソルフェジオ周波数
PlayAndMake((440/2), '440-1octave') #デビルトーン -1オクターブ
PlayAndMake((528/2), '528-1octave') #ソルフェジオ周波数 -1オクターブ
PlayAndMake(442) #現代日本
PlayAndMake((442/2), '442-1octave') #現代日本
PlayAndMake(432) #本来の基準(宇宙の真理) http://karapaia.com/archives/52242150.html
PlayAndMake((432/2), '432-1octave') #本来の基準(宇宙の真理) -1オクターブ

# A4(ラの音)を440Hzとすると、528基準で純正律したときにA5(880Hz)がある。
# すごく胡散臭い。
# http://unhp.blog.fc2.com/blog-entry-162.html
# 440Hzは人を興奮状態にして攻撃的にさせるらしい。

# 現代では440Hzより高い音を基準とすることが多いらしい。
# 周波数を高くすると華やかになるらしい。
# 興奮状態といったり、華やかといったり、よくわからない。
