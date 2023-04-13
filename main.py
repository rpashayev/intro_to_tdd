import unittest

def reverse_list(arr):
    for i in range(int(len(arr)/2)):
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    return arr

class Reverse_list_test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])
    
    def test_two(self):
        self.assertEqual(reverse_list([8, 1, 2, 3]), [3, 2, 1, 8])
    
    def test_three(self):
        self.assertEqual(reverse_list([125, 1, 6, 19, 14]), [14, 19, 6, 1, 125])
    
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")
        

def is_palindrome(str):
    return str == str[::-1]
    
class Is_palindrome_test(unittest.TestCase):
    def test_one(self):
        self.assertTrue(is_palindrome('racecar'))
    
    def test_two(self):
        self.assertTrue(is_palindrome('kayak'))
    
    def test_three(self):
        self.assertTrue(is_palindrome('rotator'))
    
    def test_four(self):
        self.assertTrue(is_palindrome('noon'))
    
    def test_five(self):
        self.assertTrue(is_palindrome('wow'))
    
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")

def coin(x):
    change = []
    quarters = x // 25
    dimes = (x - 25 * quarters ) // 10
    nickels = (x - 25 * quarters - 10 * dimes) // 5
    pennies = x - (25 * quarters + 10 * dimes + 5 * nickels)
    change = [quarters, dimes, nickels, pennies]
    return change


class coin_test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(coin(87), [3, 1, 0, 2])
    
    def test_two(self):
        self.assertEqual(coin(75), [3, 0, 0, 0])
    
    def test_three(self):
        self.assertEqual(coin(99), [3, 2, 0, 4])
    
    def test_four(self):
        self.assertEqual(coin(101), [4, 0, 0, 1])
    
    def test_five(self):
        self.assertEqual(coin(55), [2, 0, 1, 0])
    
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    
    def tearDown(self):
        # add the tearDown tasks,
        print("running tearDown tasks")


def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)

class factorial_test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(factorial(5), 120)
    
    def test_two(self):
        self.assertEqual(factorial(6), 720)
    
    def test_three(self):
        self.assertEqual(factorial(10), 3628800)
    
    def test_four(self):
        self.assertEqual(factorial(8), 40320)
    
    def test_five(self):
        self.assertEqual(factorial(0), 1)
    
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    
    def tearDown(self):
        # add the tearDown tasks,
        print("running tearDown tasks")


def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return fibonacci(x-2) + fibonacci(x-1)

class Fibonacci_test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(fibonacci(0), 0)
    
    def test_two(self):
        self.assertEqual(fibonacci(1), 1)
    
    def test_three(self):
        self.assertEqual(fibonacci(12), 144)
    
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main()
