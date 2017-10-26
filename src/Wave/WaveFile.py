#http://qiita.com/mzmttks/items/7a7c8c4b42007e13812a
import wave
from pydub import AudioSegment
import pathlib
class WaveFile:
    def __init__(self):
        self.__basepath = pathlib.PurePath('../res/')
#        self.__basepath = pathlib.PurePath('../res/scales')
        self.__base_extension = 'wav'
        self.__option_extensions = ['mp3', 'ogg', 'flac']
#        self.__create_dirs()
        pathlib.Path(self.__basepath).mkdir(parents=True, exist_ok=True)

    @property
    def BasePath(self): return self.__basepath
    @BasePath.setter
    def BasePath(self, v:pathlib.PurePath):
        if isinstance(v, pathlib.PurePath): self.__basepath = v; self.__create_dirs()
        elif isinstance(v, str): self.__basepath = pathlib.PurePath(v); self.__create_dirs()

    def Write(self, data, bit=16, fs=8000, channels=1, filename='output'):    
#        wf = wave.open(filename, "w")
        path = self.__get_path(filename, self.__base_extension)
        wf = wave.open(path, "w")
#        wf = wave.open(filename, "w")
#        wf.setnchannels(channels)
#        wf.setsampwidth(int(bit / 8))
#        wf.setframerate(fs)
        wf.setparams((
            channels,                 # channel
            int(bit / 8),             # byte width
            fs,                       # sampling rate
            len(data),                # number of frames
            "NONE", "not compressed"  # no compression
        ))
        wf.writeframes(data)
        wf.close()
        self.__convert(path, filename)

    def __create_dirs(self):
        pathlib.Path(self.__basepath).mkdir(parents=True, exist_ok=True)
        pathlib.Path(self.__basepath.joinpath(self.__base_extension)).mkdir(parents=True, exist_ok=True)
        for ext in self.__option_extensions:
            pathlib.Path(self.__basepath.joinpath(ext)).mkdir(parents=True, exist_ok=True)

    def __convert(self, wavpath, filename):
        for ext in self.__option_extensions:
            f = AudioSegment.from_file(wavpath)
            kwargs = {'format': ext, 'bitrate': '32k'}
            f.export(self.__get_path(filename, ext), **kwargs)

    def __get_path(self, filename, ext):
        return str(pathlib.Path(self.__basepath.joinpath(ext, filename + '.' + ext)).resolve())
    
"""
if __name__ == "__main__":
    import pathlib
    import Sampler
    import BaseWaveMaker
    import MusicTheory.EqualTemperament
    import MusicTheory.Scale
    import MusicTheory.tempo
    
    basepath = pathlib.PurePath('../res/scales/wav/')
    create_dirs(basepath)
    
    wm = BaseWaveMaker.BaseWaveMaker()
    sampler = Sampler.Sampler()
    scale = MusicTheory.Scale.Scale()
    timebase = MusicTheory.tempo.TimeBase()
    timebase.BPM = 120
    timebase.Metre=(4,4)
    nv = MusicTheory.tempo.NoteValue(timebase)
    maker = WaveFile()
    for key in ['C']:
#    for key in ['C','C+','D','D+','E','F','F+','G','G+','A','A+','B']:
        print(key, 'メジャー・スケール')
        scale.Major(key=key)
        waves = []
        for f0 in scale.Frequencies:
#            waves.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=f0, sec=nv.Get(4))))
#            p.Play(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=f0, sec=0.25)))
#            p.Play(sampler.Sampling(wm.Triangle(a=1, fs=8000, f0=f0, sec=0.25)))
        name = key.replace('+', 's') + 'Major'
        maker.Write(b''.join(waves), name)
#        WaveFile.Write(b''.join(waves), filename=str(pathlib.Path(basepath.joinpath(name + '.wav')).resolve()))
#        convert(name)
        
        print(key, 'マイナー・スケール')
        scale.Minor(key=key)
        waves = []
        for f0 in scale.Frequencies:
            waves.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=f0, sec=nv.Get(4))))
#        WaveFile.Write(b''.join(waves), filename=key.replace('+', 's') + 'Minor' + '.wav')
        name = key.replace('+', 's') + 'Minor'
        maker.Write(b''.join(waves), name)
#        WaveFile.Write(b''.join(waves), filename=str(pathlib.Path(basepath.joinpath(name + '.wav')).resolve()))
#        convert(name)
"""
