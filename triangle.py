import unittest


def area(a, h):
    '''Возвращает площадь треугольника
       Возвращает -1 в случае, некорректных данных

            Параметры:
                    a (float): Основание треугольника
                    h (float): Высота, проведенная к основанию a
                    
            Возвращаемое значение:
                    square (float): Площадь треугольника с основанием a и высотой h'''
        
    if a < 0 or h < 0:
        return -1

    return a * h / 2 

def perimeter(a, b, c):
    '''Возвращает периметер треугольника
       Возвращает -1 в случае, некорректных данных
    
            Параметры:
                    a (float): Сторона a треугольника
                    b (float): Сторона b треугольника
                    c (float): Сторона c треугольника
            
            Возвращаемое значение:
                    perimeter (float): Периметер треугольника со сторонами a, b, c'''
    
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    
    if a < 0 or b < 0 or c < 0:
        return -1

    return a + b + c 


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    def test_height_equal_side_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 50)
    def test_height_not_equal_side_mul(self):
        res = area(11, 15)
        self.assertEqual(res, 82.5)
    def test_sides_high_mul(self):
        res = area(11231231, 131231233265)
        self.assertEqual(res, 11231231 * 131231233265 / 2)
    def test_sides_float_mul(self):
        res = area(2.5, 6.1)
        self.assertEqual(res, 2.5 * 6.1 / 2)
    def test_sides_negative_mul(self):
        res = area(-1324, -5)
        self.assertEqual(res, -1)
    def test_equal_sides_per(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)
    def test_2_sides_equal_per(self):
        res = perimeter(30, 50, 30)
        self.assertEqual(res, 110)
    def test_no_one_equal_sides_per(self):
        res = perimeter(11, 20, 30)
        self.assertEqual(res, 61)
    def test_sides_high_per(self):
        res = perimeter(11231231, 12353314, 8987565)
        self.assertEqual(res, 11231231 + 8987565 + 12353314)
    def test_sides_float_per(self):
        res = perimeter(2.5, 5.1, 6.4)
        self.assertEqual(res, 2.5 + 5.1 + 6.4)
    def test_sides_negative_per(self):
        res = perimeter(-1324, -1235, -1352)
        self.assertEqual(res, -1)
    def test_sides_rule_triangle_per(self):
        res = perimeter(10, 20, 51324523)
        self.assertEqual(res, -1)