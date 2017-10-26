#!python3.6
import pathlib

class TagMaker:
    def __init__(self):
        self.__basepath = pathlib.PurePath('res/scales')
        self.__username = 'ytyaru'
#        self.__repo_name = 'Python.Audio.Tempo.201708071726'
        self.__repo_name = 'Python.Audio.ToneFrequency.201708111015'
#    def __get_tag_audio(name, ext, dirs): return '<audio controls src={0}></audio>'.format(get_url(name, ext, dirs))
    def get_audios(self, scale, key, name, dirs=None):
        sources = ''
        for ext in ['wav','flac','ogg','mp3']: sources += f'<source src={self.__get_url(name, ext, dirs)}>'
        return f'<audio controls>{sources}</audio>\n'
    def get_audios_scales(self, scale, key, name): return self.get_audios(scale, key, name, 'res/scales')
    def get_audios_metres(self, scale, key, name): return self.get_audios(scale, key, name, 'res/metres')
    def get_audios_tones(self, octave): return self.get_audios(None, None, 'oct' + str(octave), 'res/tones')

    def __get_url(self, name, ext, dirs=None):
        if None is dirs: dirs = str(self.__basepath)
        return f'https://raw.githubusercontent.com/{self.__username}/{self.__repo_name}/master/{dirs}/{ext}/{name}.{ext}'


if __name__ == '__main__':
    tm = TagMaker()
    body = ''
    
    #スケール
    for scale in ['Major', 'Minor']:
        table_body = '''Scale|player
-----|------
'''
        for key in ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']:
            table_body += key + ' ' + scale + '|' + tm.get_audios_scales(scale, key, key.replace('#', 's')+scale)
        body += table_body + '\n'
    
    #拍子
    table_body = '''拍子|player
----|------
'''
    for metre in ['2-2(Sw)','2-2(wS)','3-2(Sww)','2-4(Sw)','2-4(wS)','3-4(Sww)','4-4(SwMw)','4-4(Swww)','5-4(Swwww)','5-4(SwMww)','5-4(SwwMw)','6-4(SwwMww)','7-4(Swwwwww)','7-4(SwwMwww)','7-4(SwwwMww)','7-4(SwMwMww)','7-4(SwwMwMw)','3-8(Sww)','6-8(SwwMww)','9-8(SwwMwwMww)','12-8(SwwmwwMwwmww)','12-8(Swwmwwmwwmww)']:
        table_body += metre.replace('-','/') + '|' + tm.get_audios_metres(scale, key, key.replace('#', 's')+scale)
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
    table_body = '# Major Scale' + '\n\n' + '''調(Key)|player
-------|------
'''
#    for octave in range(12):
    for octave in range(len(et.Ids)):
        table_body += str(octave) + '|' + tm.get_audios_tones(octave)
    body += table_body + '\n'
    
    print(body)

