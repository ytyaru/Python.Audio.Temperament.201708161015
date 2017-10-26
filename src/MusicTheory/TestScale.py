import unittest
class TestScale(unittest.TestCase):
    def test_Major_C(self):
        s = Scale()
        s.Major(key='C')
        for i in range(1, 8):
            abs(s.Scales[i] - s.Scales[i-1])
        
        print(s.Major(key='C'))
        print(','.join([Key.Key.ValueToName(k) for k in s.Scales]))

