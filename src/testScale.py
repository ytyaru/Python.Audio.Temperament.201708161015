from MusicTheory.temperament.EqualTemperament import EqualTemperament
from MusicTheory.temperament.eq12scales.ScaleIntervals import ScaleIntervals
from MusicTheory.temperament.eq12scales.Scale import Scale
import Wave.Player
import Wave.Sampler
import Wave.BaseWaveMaker
import Wave.WaveFile
import pathlib

def GetToneName(keyId):
    return ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'][keyId]

class PlayAndMaker:
    #再生とファイル生成
    @staticmethod
    def Run(scaleKeyId, scaleTones):
        wm = Wave.BaseWaveMaker.BaseWaveMaker()
        sampler = Wave.Sampler.Sampler()
        wf = Wave.WaveFile.WaveFile()
#        p = Wave.Player.Player()
#        p.Open()

        #スケールの構成音生成
        wf.BasePath = pathlib.PurePath(f'../res/440/EqualTemperament/scales/')
        wav = []
        for f0 in scaleTones:
            wav.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=f0, sec=0.5)))
        wf.Write(b''.join(wav), filename=GetToneName(scaleKeyId).replace('#','+') + 'Major')
        wav.clear()
#        p.Close()

if __name__ == '__main__':
    et = EqualTemperament()
    et.Denominator = 12
    et.SetBaseKey(keyId=9, pitch=4, hz=440)
    scale = Scale(et)# scale.Temperament = et
    print(f'BaseKey: {GetToneName(et.BaseKeyId)}{et.BaseKeyPitch} {et.BaseFrequency}Hz')
    print(f'{et.Denominator}平均律')
    for scaleKeyId in range(et.Denominator):
        tones = scale.Get(scaleKeyId, ScaleIntervals.Major)
        for tone in tones: print('{:2}'.format(GetToneName(tone[0])), end=' ')
        print()
        PlayAndMaker.Run(scaleKeyId, [tone[2] for tone in tones])

