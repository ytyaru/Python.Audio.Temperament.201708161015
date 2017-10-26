# このソフトウェアについて

ピタゴラス音律でkeyIdとpitchを指定して周波数を取得できるようにした。

# 対象ファイル名

ファイル名|説明
----------|----
MusicTheory/temperament/PythagoreanTuning.py|ピタゴラス音律

# 実行

```sh
$ python '/tmp/Python.Audio.Temperament.201708161015/src/MusicTheory/temperament/PythagoreanTuning.py' 
Key: A, Pitch: 4, Frequency: 440Hz
[440, 463.5390946502056, 495.0, 521.4814814814814, 556.875, 586.6666666666666, 626.484375, 660.0, 695.3086419753085, 742.5, 782.2222222222222, 835.3125]
----- pitch = -1 -----
C : 8.148148148148147
C#: 8.701171875
D : 9.166666666666666
D#: 9.788818359375
E : 10.3125
F : 10.864197530864196
F#: 11.6015625
G : 12.222222222222221
G#: 13.0517578125
A : 13.75
A#: 14.485596707818925
B : 15.46875
----- pitch = 0 -----
C : 16.296296296296294
C#: 17.40234375
D : 18.333333333333332
D#: 19.57763671875
E : 20.625
F : 21.728395061728392
F#: 23.203125
G : 24.444444444444443
G#: 26.103515625
A : 27.5
A#: 28.97119341563785
B : 30.9375
----- pitch = 1 -----
C : 32.59259259259259
C#: 34.8046875
D : 36.666666666666664
D#: 39.1552734375
E : 41.25
F : 43.456790123456784
F#: 46.40625
G : 48.888888888888886
G#: 52.20703125
A : 55.0
A#: 57.9423868312757
B : 61.875
----- pitch = 2 -----
C : 65.18518518518518
C#: 69.609375
D : 73.33333333333333
D#: 78.310546875
E : 82.5
F : 86.91358024691357
F#: 92.8125
G : 97.77777777777777
G#: 104.4140625
A : 110.0
A#: 115.8847736625514
B : 123.75
----- pitch = 3 -----
C : 130.37037037037035
C#: 139.21875
D : 146.66666666666666
D#: 156.62109375
E : 165.0
F : 173.82716049382714
F#: 185.625
G : 195.55555555555554
G#: 208.828125
A : 220.0
A#: 231.7695473251028
B : 247.5
----- pitch = 4 -----
C : 260.7407407407407
C#: 278.4375
D : 293.3333333333333
D#: 313.2421875
E : 330.0
F : 347.6543209876543
F#: 371.25
G : 391.1111111111111
G#: 417.65625
A : 440
A#: 463.5390946502056
B : 495.0
----- pitch = 5 -----
C : 521.4814814814814
C#: 556.875
D : 586.6666666666666
D#: 626.484375
E : 660.0
F : 695.3086419753085
F#: 742.5
G : 782.2222222222222
G#: 835.3125
A : 880
A#: 927.0781893004112
B : 990.0
----- pitch = 6 -----
C : 1042.9629629629628
C#: 1113.75
D : 1173.3333333333333
D#: 1252.96875
E : 1320.0
F : 1390.617283950617
F#: 1485.0
G : 1564.4444444444443
G#: 1670.625
A : 1760
A#: 1854.1563786008223
B : 1980.0
----- pitch = 7 -----
C : 2085.9259259259256
C#: 2227.5
D : 2346.6666666666665
D#: 2505.9375
E : 2640.0
F : 2781.234567901234
F#: 2970.0
G : 3128.8888888888887
G#: 3341.25
A : 3520
A#: 3708.3127572016447
B : 3960.0
----- pitch = 8 -----
C : 4171.851851851851
C#: 4455.0
D : 4693.333333333333
D#: 5011.875
E : 5280.0
F : 5562.469135802468
F#: 5940.0
G : 6257.777777777777
G#: 6682.5
A : 7040
A#: 7416.625514403289
B : 7920.0
----- pitch = 9 -----
C : 8343.703703703703
C#: 8910.0
D : 9386.666666666666
D#: 10023.75
E : 10560.0
F : 11124.938271604937
F#: 11880.0
G : 12515.555555555555
G#: 13365.0
A : 14080
A#: 14833.251028806579
B : 15840.0
```

# 課題

* ピタゴラス音律で音階(スケール)を算出したい
* ソースコードが整理できていない
    * 音楽理論がわからず、どうまとめていいのかもわからない
* 12平均律以外の音律でも構成音を算出したいが……
    * 純正律における中間の5音も算出したい。計算方法がよくわからない
    * ピタゴラス音律はピタゴラスコンマによって減5度と増4度が同一音にならないので、ある組合せでうなりを生じる

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [libav](http://ytyaru.hatenablog.com/entry/2018/08/24/000000)
    * [各コーデック](http://ytyaru.hatenablog.com/entry/2018/08/23/000000)
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1
        * [pydub](http://ytyaru.hatenablog.com/entry/2018/08/25/000000)
        * [PyAudio](http://ytyaru.hatenablog.com/entry/2018/07/27/000000) 0.2.11
            * [ALSA lib pcm_dmix.c:1022:(snd_pcm_dmix_open) unable to open slave](http://ytyaru.hatenablog.com/entry/2018/07/29/000000)
        * [matplotlib](http://ytyaru.hatenablog.com/entry/2018/07/22/000000)
            * [matplotlibでのグラフ表示を諦めた](http://ytyaru.hatenablog.com/entry/2018/08/05/000000)

# 参考

感謝。

## 440Hz, 432Hz

* http://tabi-labo.com/156689/music-a432

## 和音の生成

* http://ism1000ch.hatenablog.com/entry/2013/11/15/182442
* https://ja.wikipedia.org/wiki/%E4%B8%89%E5%92%8C%E9%9F%B3
* https://ja.wikipedia.org/wiki/%E3%83%91%E3%83%AF%E3%83%BC%E3%82%B3%E3%83%BC%E3%83%89

## 音名

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E5%90%8D%E3%83%BB%E9%9A%8E%E5%90%8D%E8%A1%A8%E8%A8%98

## 音階

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E

### 五度圏

* http://dn-voice.info/music-theory/godoken/

## 音高の算出

* http://www.asahi-net.or.jp/~HB9T-KTD/music/Japan/Research/DTM/freq_map.html
* http://www.nihongo.com/aaa/chigaku/suugaku/pythagoras.htm

## サイン波のスピーカ再生

* http://www.non-fiction.jp/2015/08/17/sin_wave/
* http://aidiary.hatenablog.com/entry/20110607/1307449007
* http://ism1000ch.hatenablog.com/entry/2013/11/15/182442

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[pydub](https://github.com/jiaaro/pydub)|[MIT](https://github.com/jiaaro/pydub/blob/master/LICENSE)|[Copyright (c) 2011 James Robert, http://jiaaro.com](https://github.com/jiaaro/pydub/blob/master/LICENSE)
[pygame](http://www.pygame.org/)|[LGPL](https://www.pygame.org/docs/)|[pygame](http://www.pygame.org/)

