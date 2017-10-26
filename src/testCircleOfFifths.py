import MusicTheory.ToneAccidentaler
import MusicTheory.CircleOfFifths
cof = MusicTheory.CircleOfFifths.CircleOfFifths()
#print('---------- Major ----------')
#for k in range(12): print(cof.Get(k))
#print('---------- Minor ----------')
#for k in range(12): print(cof.Get(k, True))

print('---------- Major ----------')
for k in range(12): print(cof.GetScales(k))

