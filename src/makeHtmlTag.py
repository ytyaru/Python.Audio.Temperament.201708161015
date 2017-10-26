#!python3.6
#import MusicTheory.EqualTemperament
#import MusicTheory.Scale
#import MusicTheory.scales.MajorScales
import MusicTheory.temperament.EqualTemperament
import MusicTheory.temperament.JustIntonation
import MusicTheory.temperament.PythagoreanTuning
from MusicTheory.temperament.eq12scales.ScaleIntervals import ScaleIntervals
from MusicTheory.temperament.eq12scales.Scale import Scale
import pathlib

"""所定の音声ファイルを再生させるためのHTML5<audio>タグを生成するスクリプト。"""

def GetToneName(keyId):
    return ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'][keyId]

class TagMaker:
    def __init__(self):
        self.__basepath = pathlib.PurePath('res/scales')
        self.__username = 'ytyaru'
#        self.__repo_name = 'Python.Audio.Tempo.201708071726'
#        self.__repo_name = 'Python.Audio.ToneFrequency.201708111015'
#        self.__repo_name = 'Python.Audio.Scale.201708111722'
#        self.__repo_name = 'Python.Audio. JustIntonation.201708131311'
#        self.__repo_name = 'Python.Audio.Chord.2017081743'
#        self.__repo_name = 'Python.Audio.Temperament.201708141517'
        self.__repo_name = 'Python.Audio.Temperament.201708150947'
#    def __get_tag_audio(name, ext, dirs): return '<audio controls src={0}></audio>'.format(get_url(name, ext, dirs))
    def get_audios(self, name, dirs=None):
        sources = ''
        for ext in ['wav','flac','ogg','mp3']: sources += f'<source src={self.__get_url(name, ext, dirs)}>'
#        return f'<audio controls>{sources}</audio>\n'
        return f'<audio controls>{sources}</audio>'
    """
    def get_audios_scales(self, name): return self.get_audios(name, 'res/scales')
    def get_audios_metres(self, name): return self.get_audios(name, 'res/metres')
    def get_audios_tones(self, octave): return self.get_audios('oct' + str(octave), 'res/tones')
    def get_audios_MajorScales(self, name): return self.get_audios(name, 'res/scales/Major')
    def get_audios_JustIntonation(self, name): return self.get_audios(name, 'res/temperaments/JustIntonation')
    def get_audios_chords_JustIntonation(self, name, pattern): return self.get_audios(name, f'res/chords/{pattern}/JustIntonation')
    """
    def get_audios_TemperamentScales(self, temperament, hz): return self.get_audios(str(hz), f'res/scales/{temperament.__class__.__name__}')
    def get_audios_TemperamentChords(self, temperament, hz, chord): return self.get_audios(str(hz), f'res/chords/{chord}/{temperament.__class__.__name__}')
    
    def __get_url(self, name, ext, dirs=None):
        if None is dirs: dirs = str(self.__basepath)
        return f'https://raw.githubusercontent.com/{self.__username}/{self.__repo_name}/master/{dirs}/{ext}/{name}.{ext}'
    def get_audios_12EqScales(self, name): return self.get_audios(name, 'res/440/EqualTemperament/scales/')


if __name__ == '__main__':
    tm = TagMaker()
    body = ''
    """
    #スケール
    for scale in ['Major', 'Minor']:
        table_body = '''Scale|player
-----|------
'''
        for key in ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']:
            table_body += key + ' ' + scale + '|' + tm.get_audios_scales(key.replace('#', 's')+scale)
        body += table_body + '\n'
    
    #拍子
    table_body = '''拍子|player
----|------
'''
    for metre in ['2-2(Sw)','2-2(wS)','3-2(Sww)','2-4(Sw)','2-4(wS)','3-4(Sww)','4-4(SwMw)','4-4(Swww)','5-4(Swwww)','5-4(SwMww)','5-4(SwwMw)','6-4(SwwMww)','7-4(Swwwwww)','7-4(SwwMwww)','7-4(SwwwMww)','7-4(SwMwMww)','7-4(SwwMwMw)','3-8(Sww)','6-8(SwwMww)','9-8(SwwMwwMww)','12-8(SwwmwwMwwmww)','12-8(Swwmwwmwwmww)']:
        table_body += metre.replace('-','/') + '|' + tm.get_audios_metres(key.replace('#', 's')+scale)
    body += table_body + '\n'    
    
    #音(Tone)
    table_body = '''オクターブ|player
----------|------
'''
    for octave in range(-1, 10):
        table_body += str(octave) + '|' + tm.get_audios_tones(octave)
    body += table_body + '\n'
    
    #音階(メジャースケール)
    et = MusicTheory.EqualTemperament.EqualTemperament()
    scale = MusicTheory.Scale.Scale()
    scale.Scale = MusicTheory.scales.MajorScales.MajorScales()
    table_body = '# Major Scale' + '\n\n' + '''調(Key)|構成音|player
-------|------|------
'''
#    for octave in range(12):
    for keyId in range(len(et.Ids)):
        scale.KeyId = keyId
        print(keyId, scale.Scales, et.Names[keyId], [et.Names[k] for k in scale.Scales])
        table_body += et.Names[keyId] + '|' + ' '.join([et.Names[k] for k in scale.Scales]) + '|' + tm.get_audios_MajorScales(et.Names[keyId].replace('#', '+')+'MajorScale')
    body += table_body + '\n'

    #音律(純正律)
    et = MusicTheory.EqualTemperament.EqualTemperament()
    scale = MusicTheory.Scale.Scale()
    scale.Scale = MusicTheory.scales.MajorScales.MajorScales()
    data = ((432, '命、自然、癒やし、宇宙の真理の周波数。'), (440, 'デビルトーン。人を攻撃的にする。世界基準の音。陰謀により世界基準になったという説がある。'), (442, '現代日本でのピアノ調律の基準音。440Hzより高めの音が現代風らしい。'), (528, 'ソルフェジオ周波数。理想への変換、奇跡、DNAの回復の効果が得られるらしい。'))
    table_body = '# 音律' + '\n\n' + '## 純正律' + '\n\n' + '''基音(Hz)|説明|player
-------|------|------
'''
    for d in data:
        table_body += str(d[0]) + '|' + d[1] + '|' + tm.get_audios_JustIntonation(str(d[0]))
        table_body += str(d[0])+'-1octave' + '|' + '' + '|' + tm.get_audios_JustIntonation(str(d[0])+'-1octave')
    body += table_body + '\n'

    #和音(純正律におけるパワーコードとメジャーコード)
    table_body = '# 和音（純正律におけるパワーコードとメジャーコード）' + '\n\n' + '''基音(Hz)|player
--------|------
'''
    for pattern in ['power', 'major']:
        for hz in [432, 440, 528]:
            table_body += str(hz) + '|' + tm.get_audios_chords_JustIntonation(str(hz), pattern)
    body += table_body + '\n'            
    """
    table_body = ''
    #各音律における構成音と和音
    for hz in [432, 440, 444]:
        table_body += f'## {hz}Hz' + '\n\n' + '音律|構成音|パワーコード|メジャーコード' + '\n' + '----|------|------------|--------------' + '\n'
        for temperament, name in [
            (MusicTheory.temperament.EqualTemperament.EqualTemperament(), '平均律'), 
            (MusicTheory.temperament.JustIntonation.JustIntonation(), '純正律'), 
            (MusicTheory.temperament.PythagoreanTuning.PythagoreanTuning(), 'ピタゴラス音律')]:
#            name = ''
#            if isinstance (temperament, MusicTheory.temperament.EqualTemperament.EqualTemperament): name = '平均律'
#            elif isinstance (temperament, MusicTheory.temperament.JustIntonation.JustIntonation): name = '純正律'
#            elif isinstance (temperament, MusicTheory.temperament.PythagoreanTuning.PythagoreanTuning): name = 'ピタゴラス音律'
            table_body += name + '|' + tm.get_audios_TemperamentScales(temperament, hz) + '|' + tm.get_audios_TemperamentChords(temperament, hz, 'power') + '|' + tm.get_audios_TemperamentChords(temperament, hz, 'major') + '\n'
        
        table_body += '\n'
    body += table_body + '\n'

    #12平均律の各調におけるメジャースケール構成音
    et = MusicTheory.temperament.EqualTemperament.EqualTemperament()
    et.Denominator = 12
    et.SetBaseKey(keyId=9, pitch=4, hz=440)
    scale = Scale(et)# scale.Temperament = et
    table_body = '# Major Scale 構成音' + '\n\n' + f'* 基音: {GetToneName(et.BaseKeyId)}{et.BaseKeyPitch} {et.BaseFrequency}Hz, 音律: {et.Denominator}平均律' + '\n\n' + '調(Key)|構成音|player' + '\n' + '----|------|------|' + '\n'
    for scaleKeyId in range(et.Denominator):
        tones = scale.Get(scaleKeyId, ScaleIntervals.Major)
        table_body += GetToneName(scaleKeyId) + '|' + ' '.join(['{:2}'.format(GetToneName(tone[0])) for tone in tones]).strip() + '|' + tm.get_audios_12EqScales(GetToneName(scaleKeyId).replace('#','+')+'Major') + '\n'
    body += table_body + '\n'

    print(body)

