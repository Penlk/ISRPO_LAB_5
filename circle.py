import math
import unittest


def area(r):
    '''Возвращает площадь окружности
       Возвращает -1 в случае, некорректных данных
            
            Параметры:
                    r (float): радиус окружности
            
            Возвращаемое значение:
                    square (float): площадь окружности с радиусом r'''
        
    if r < 0:
        return -1

    return math.pi * r * r


def perimeter(r):
    '''Возвращает периметер окружности
       Возвращает -1 в случае, некорректных данных
    
            Параметры:
                    r (float): радиус окружности
                    
            Возвращаемое значение:
                    perimeter (float): периметер окружности с радиусом r'''
        
    if r < 0:
        return -1

    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_radius_high_mul(self):
        res = area(10000000)
        self.assertEqual(res, math.pi * 10000000 * 10000000)
    def test_radius_float_mul(self):
        res = area(2.5)
        self.assertEqual(res, math.pi * 2.5 * 2.5)
    def test_radius_negative_mul(self):
        res = area(-1324)
        self.assertEqual(res, -1)
    def test_zero_per(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_radius_10_per(self):
        res = perimeter(10)
        self.assertEqual(res, math.pi * 20)
    def test_radius_20_per(self):
        res = perimeter(20)
        self.assertEqual(res, math.pi * 40)
    def test_radius_float_per(self):
        res = perimeter(2.5)
        self.assertEqual(res, math.pi * 5)
    def test_radius_negative_per(self):
        res = perimeter(-1324)
        self.assertEqual(res, -1)