import unittest

def area(a, b):
    '''Возвращает площадь прямоугольника
       Возвращает -1 в случае, некорректных данных
    
            Параметры:
                    a (float): Сторона a прямоугольника
                    b (float): Сторона b прямоугольника
            
            Возвращаемое значение:
                    square (float): Площадь прямоугольника со сторонами a и b'''
        
    if a < 0 or b < 0:
        return -1

    return a * b 

def perimeter(a, b): 
    ''' Возвращает периметер прямоугольника
        Возвращает -1 в случае, некорректных данных
    
            Параметры:
                    a (float): Сторона a прямоугольника
                    b (float): Сторона b прямоугольника
                    
            Возвращаемое значение:
                    perimeter (float): Периметер прямоугольника со сторонами a и b'''
        
    if a < 0 or b < 0:
        return -1

    return 2 * (a + b) 


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
    def test_rectangle_mul(self):
        res = area(11231231, 123452345)
        self.assertEqual(res, 123452345 * 11231231)
    def test_sides_float_mul(self):
        res = area(2.5, 5.3)
        self.assertEqual(res, 2.5 * 5.3)
    def test_sides_negative_mul(self):
        res = area(-1324, -141)
        self.assertEqual(res, -1)
    def test_zero_per(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
    def test_square_per(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
    def test_rectangle_per(self):
        res = perimeter(20123, 50523231)
        self.assertEqual(res, 50523231 + 50523231 + 20123 + 20123)
    def test_sides_float_per(self):
        res = perimeter(2.5, 5.3)
        self.assertEqual(res, 2 * (2.5 + 5.3))
    def test_sides_negative_mul(self):
        res = area(-1324, -52)
        self.assertEqual(res, -1)