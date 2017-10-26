#!python3.6
import Wave.Player
import Wave.Sampler
import Wave.BaseWaveMaker
import Wave.WaveFile
import MusicTheory.ToneFrequency
import pathlib
if __name__ == '__main__':
    tf = MusicTheory.ToneFrequency.ToneFrequency()
    for name in ('C','D','E','F','G','A','B'): print(name, tf.ToFrequency(name))
    print()
    for name in ('C+','D+','E+','F+','G+','A+','B+'): print(name, tf.ToFrequency(name))
    print()
    for name in ('C-','D-','E-','F-','G-','A-','B-'): print(name, tf.ToFrequency(name))
    print()
    for name in ['C'+'-'*n for n in range(25)]: print(name, tf.ToFrequency(name))
    print()
    for name in ['C'+'+'*n for n in range(25)]: print(name, tf.ToFrequency(name, -1))
    print()

    wm = Wave.BaseWaveMaker.BaseWaveMaker()
    sampler = Wave.Sampler.Sampler()
    wf = Wave.WaveFile.WaveFile()
    wf.BasePath = pathlib.PurePath('../res/tones/')

    p = Wave.Player.Player()
    p.Open()
    """
    for name in ('C','D','E','F','G','A','B'):
        print(name, tf.ToFrequency(name));
        p.Play(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=tf.ToFrequency(name), sec=0.5)))
    for name in ('C','C+','D','D+','E','F','G','G+','A','A+','B'):
        print(name, tf.ToFrequency(name));
        p.Play(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=tf.ToFrequency(name), sec=0.5)))
    for name in ('C+','D+','E+','F+','G+','A+','B+'):
        print(name, tf.ToFrequency(name));
        p.Play(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=tf.ToFrequency(name), sec=0.5)))
    for name in ('C-','D-','E-','F-','G-','A-','B-'):
        print(name, tf.ToFrequency(name));
        p.Play(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=tf.ToFrequency(name), sec=0.5)))
    """
    wav = []
    for pitch in range(-1, 10):
        print('-------pitch:', pitch)
        wav.clear()
        for name in ('C','C+','D','D+','E','F','G','G+','A','A+','B'):
#        for name in ('C','D','E','F','G','A','B'):
#            print(name, tf.ToFrequency(name));
            f0, keyId, pitch = tf.ToFrequency(name, pitch)
            print('{0:<2} {1:>2} {2:>3} {3:f}'.format(tf.EqualTemperament.Names[keyId], keyId, pitch, f0))
#            p.Play(sampler.Sampling(wm.Sin(a=1, fs=32000, f0=f0, sec=0.125)), rate=32000)
            wav.append(sampler.Sampling(wm.Sin(a=1, fs=32000, f0=f0, sec=0.125)))
#            p.Play(sampler.Sampling(wm.Sin(a=1, fs=16000, f0=f0, sec=0.125)), rate=16000)
#            p.Play(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=f0, sec=0.125)))
        wf.Write(b''.join(wav), filename=f'oct{pitch}')

    p.Close()
