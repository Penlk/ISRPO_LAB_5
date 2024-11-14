import unittest


def area(a):
    '''Возвращает площадь квадрата
       Возвращает -1 в случае, некорректных данных
    
            Параметры:
                    a (float): Сторона квадрата
            
            Возвращаемое значение:
                    square (float): Площадь квадрата со стороной a'''
    
    if a < 0:
        return -1

    return a * a


def perimeter(a):
    '''Возвращает периметер квадрата
       Возвращает -1 в случае, некорректных данных
            
            Параметры:
                    a (float): Сторона квадрата
            
            Возвращаемое значение:
                    perimeter (float): Периметер квадрата со стороной a'''
    
    if a < 0:
        return -1

    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_side_10_mul(self):
        res = area(10)
        self.assertEqual(res, 100)
    def test_side_high_mul(self):
        res = area(11231231)
        self.assertEqual(res, 11231231 * 11231231)
    def test_side_float_mul(self):
        res = area(2.5)
        self.assertEqual(res, 2.5 * 2.5)
    def test_side_negative_mul(self):
        res = area(-1324)
        self.assertEqual(res, -1)
    def test_zero_per(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_side_10_per(self):
        res = perimeter(10)
        self.assertEqual(res, 40)
    def test_side_high_per(self):
        res = perimeter(11231231)
        self.assertEqual(res, 11231231 * 4)
    def test_side_float_per(self):
        res = perimeter(2.3)
        self.assertEqual(res, 2.3 * 4)
    def test_side_negative_per(self):
        res = perimeter(-1324)
        self.assertEqual(res, -1)