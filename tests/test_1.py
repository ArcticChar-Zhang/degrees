import unittest
from math import ceil, floor
from math import degrees as degs
import pickle
from warnings import filterwarnings
import degrees

class TestProject(unittest.TestCase):
    def test_init_and_str(self):
        d1 = degrees.Degree(1, 2, 3)
        d2 = degrees.Degree(-4, 5, 6)
        d3 = degrees.Degree(d2)
        d4 = degrees.Degree(0, 1, 2)
        d5 = degrees.Degree(0, 0, 1)
        d6 = degrees.Degree()
        d7 = degrees.Degree(61, 61, 61)
        d8 = degrees.Degree(-61, 61, 61)
        d9 = degrees.Degree(1)
        with self.assertRaises(TypeError):
            degrees.Degree('')
        with self.assertRaises(ValueError):
            degrees.Degree(degrees.Degree(1, 2, 3), 1)
        with self.assertRaises(ValueError):
            degrees.Degree(1, -1)
        with self.assertRaises(ValueError):
            degrees.Degree(0, -2, -6)
        with self.assertRaises(TypeError):
            degrees.Degree(0.0, 0.0, 0.0)
        with self.assertRaises(TypeError):
            degrees.Degree(-1.5, 1, 1)
        self.assertEqual(repr(d1), 'Degree(1, 2, 3)')
        self.assertEqual(repr(-d1), 'Degree(-1, 2, 3)')
        self.assertEqual(str(d1), '1°2′3″')
        self.assertEqual(str(d2), '-4°5′6″')
        self.assertEqual(str(d3), '-4°5′6″')
        self.assertEqual(str(d4), '1′2″')
        self.assertEqual(str(d5), '1″')
        self.assertEqual(str(d6), '0°')
        self.assertEqual(str(d7), '62°2′1″')
        self.assertEqual(str(d8), '-62°2′1″')
        self.assertEqual(str(d9), '1°')
        print(1)

    def test_abs(self):
        self.assertEqual(abs(degrees.Degree(1, 2, 3)), degrees.Degree(1, 2, 3))
        print(2)
    
    def test_pos_and_neg(self):
        d1 = +degrees.Degree(1, 2, 3)
        d2 = -degrees.Degree(-4, 5, 6)
        d3 = -degrees.Degree(0, 5, 6)
        d4 = -degrees.Degree(0, 0, 6)
        self.assertEqual(d1, degrees.Degree(1, 2, 3))
        self.assertEqual(d2, degrees.Degree(4, 5, 6))
        self.assertEqual(d3, degrees.Degree(0, -5, 6))
        self.assertEqual(d4, degrees.Degree(0, 0, -6))
        print(3)

    def test_ceil_and_floor(self):
        d1 = degrees.Degree(1, 2, 3)
        d2 = degrees.Degree(-4, 5, 6)
        d3 = degrees.Degree()
        d4 = degrees.Degree(1)
        self.assertEqual(ceil(d1), 2)
        self.assertEqual(floor(d1), 1)
        self.assertEqual(ceil(d2), -4)
        self.assertEqual(floor(d2), -5)
        self.assertEqual(ceil(d3), 0)
        self.assertEqual(floor(d3), 0)
        self.assertEqual(ceil(d4), 1)
        self.assertEqual(floor(-d4), -1)
        print(4)

    def test_float(self):
        d1 = degrees.Degree(1, 2, 3)
        self.assertAlmostEqual(float(d1), 1241 / 1200)
        print(5)

    def test_bool(self):
        d1 = degrees.Degree(1, 2, 3)
        d2 = degrees.Degree()
        self.assertEqual(bool(d1), True)
        self.assertEqual(bool(d2), False)
        print(6)

    def test_comps(self):
        d1 = degrees.Degree(1, 2, 3)
        d2 = degrees.Degree(4, 5, 6)
        self.assertLess(d1, d2)
        self.assertLessEqual(d1, d2)
        self.assertNotEqual(d1, d2)
        self.assertGreater(d2, d1)
        d3 = degrees.Degree(-1)
        d4 = degrees.Degree(-4, 5, 6)
        self.assertEqual(d3, -1)
        self.assertEqual(d1, 1.0341666666666667)
        self.assertGreater(d3, d4)
        self.assertLessEqual(d4, d3)
        d5 = degrees.Degree(0, 2)
        d6 = degrees.Degree(0, 3)
        self.assertLess(d5, d6)
        self.assertGreater(d6, d5)
        d7 = degrees.Degree(0, -2)
        d8 = degrees.Degree(0, -3)
        self.assertGreater(d7, d8)
        self.assertLess(d8, d7)
        d9 = degrees.Degree(second=1)
        d10 = degrees.Degree(second=2)
        self.assertLess(d9, d10)
        self.assertGreater(-d9, -d10)
        self.assertLess(d10, 6.1)
        self.assertGreater(degrees.Degree(0), -1)
        self.assertGreater(degrees.Degree(11, 1), 11)
        self.assertLessEqual(degrees.Degree(11, 1), degrees.Degree(11, 1))
        with self.assertRaises(AssertionError):
            self.assertGreater(degrees.Degree(11, 1), 12)
        with self.assertRaises(TypeError):
            degrees.Degree() > ''
        print(7)

    def test_calc(self):
        filterwarnings('ignore', category=DeprecationWarning)
        d1 = degrees.Degree(0)
        d2 = 0
        self.assertEqual(d2 + d1, d1)
        self.assertEqual(d1 - d2, d1)
        self.assertEqual(d2 - d1, -d1)
        self.assertEqual(d1 * d2, degrees.Degree())
        self.assertEqual(d2 * d1, degrees.Degree())
        self.assertEqual(d1 * d1, degrees.Degree())
        d1 * 0.5
        with self.assertRaises(Exception):
            d1 * ''
        print(8)

    def test_div(self):
        d1 = degrees.Degree(0)
        d2 = degrees.Degree(1, 2, 3)
        d3 = degrees.Degree(2, 4, 6)
        d4 = 2
        with self.assertRaises(ZeroDivisionError):
            d2 / d1
        with self.assertRaises(ZeroDivisionError):
            d2 % d1
        with self.assertRaises(ZeroDivisionError):
            d2 // d1
        self.assertAlmostEqual(d3 / d2, 2.0)
        self.assertEqual(d3 / d4, d2)
        self.assertEqual(d3 // d2, 2)
        self.assertEqual(d3 // d4, 1)
        self.assertEqual(d3 % d2, 0)
        print(9)

    def test_hash(self):
        d = degrees.Degree(1, 2, 3)
        self.assertEqual(hash(d), hash((d.deg, d.min, d.sec, d.sign)))
        print(10)

    def test_attr(self):
        d1 = degrees.Degree()
        self.assertEqual(d1.sign, 0)
        with self.assertRaises(AttributeError):
            d1.c
        with self.assertRaises(AttributeError):
            d1._Degree__set_

        with self.assertRaises(AttributeError):
            d1.c = 0
        print(11)

    def test_funcs(self):
        r = 1
        self.assertEqual(int(degrees.radian2degree(r)), int(degs(r)))
        d1 = degrees.Degree(361)
        self.assertEqual(degrees.normalize(d1), degrees.Degree(1))
        print(12)

    def test_fromstr(self):
        s1 = "1°2'3\""
        self.assertEqual(degrees.Degree.from_str(s1), degrees.Degree(1, 2, 3))
        self.assertEqual(degrees.Degree.from_str('0'), degrees.Degree())
        with self.assertRaises(ValueError):
            degrees.Degree.from_str('1]')
        with self.assertRaises(ValueError):
            degrees.Degree.from_str('1°2\'3"3"')
        with self.assertRaises(ValueError):
            degrees.Degree.from_str('1°3"')
        with self.assertRaises(ValueError):
            degrees.Degree.from_str('1"3°')
        print(13)

    def test_fromiter(self):
        i1 = (1, 2, 3)
        i2 = (1, 2, 3, 4)
        i3 = (1, 2, 3, -4)
        i4 = (1, 2, 3, 0)
        i5 = ()
        self.assertEqual(degrees.Degree.from_iter(i1), degrees.Degree(1, 2, 3))
        self.assertEqual(degrees.Degree.from_iter(i2), degrees.Degree(1, 2, 3))
        self.assertEqual(degrees.Degree.from_iter(i3), degrees.Degree(-1, 2, 3))
        with self.assertRaises(ValueError):
            degrees.Degree.from_iter(i4)
        with self.assertRaises(ValueError):
            degrees.Degree.from_iter(i5)
        print(14)

    def test_version(self):
        self.assertGreaterEqual(degrees.version_info, (0, 1))
        self.assertEqual(str(degrees.version_info), str(degrees.version_info))
        print(15)

    def test_dms(self):
        s1 = degrees.Degree(-1, 2, 3)
        s2 = degrees.Degree(0, -4, 6)
        s3 = degrees.Degree(0, 0, -3)
        s4 = degrees.Degree(1, 2, 3)
        self.assertEqual(s1.dms, (-1, 2, 3))
        self.assertEqual(s2.dms, (0, -4, 6))
        self.assertEqual(s3.dms, (0, 0, -3))
        self.assertEqual(s4.dms, (1, 2, 3))
        print(16)

    def test_fromustr(self):
        s1 = "1°2′3″"
        self.assertEqual(degrees.Degree.from_unicode(s1), degrees.Degree(1, 2, 3))
        self.assertEqual(degrees.Degree.from_unicode('0'), degrees.Degree())
        with self.assertRaises(ValueError):
            degrees.Degree.from_unicode('1]')
        with self.assertRaises(ValueError):
            degrees.Degree.from_unicode('1°2′3″3″')
        with self.assertRaises(ValueError):
            degrees.Degree.from_unicode('1°3″')
        with self.assertRaises(ValueError):
            degrees.Degree.from_unicode('1″3°')
        print(17)

    def test_pickle(self):
        d = degrees.Degree()
        a = pickle.dumps(d)
        b = pickle.loads(a)
        self.assertEqual(d, b)
        print(18)

    def test_complex(self):
        d = degrees.Degree(45)
        self.assertAlmostEqual(d.to_complex(2 ** 0.5), 1+1j)
        with self.assertRaises(ValueError):
            d.to_complex(-1)
        print(19)
    
    def test_duck_types(self):
        d1 = degrees.Degree(1, 2, 3)
        self.assertEqual(d1.as_integer_ratio(), (1241, 1200))
        self.assertEqual(degrees.Degree().as_integer_ratio(), (0, 1))
        self.assertFalse(d1.is_integer())
        print(20)
