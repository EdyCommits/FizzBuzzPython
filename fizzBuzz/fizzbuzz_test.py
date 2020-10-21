import unittest
from fizz_buzz import FizzBuzz


class TestFizzBuzz(unittest.TestCase):
    def test_should_return_the_number(self):
        self.assertEqual(FizzBuzz(1), 1)
        self.assertEqual(FizzBuzz(2), 2)
        self.assertEqual(FizzBuzz(8), 8)

    def test_retruns_Fizz_when_number_is_devisable_by_3(self):
        self.assertEquals(FizzBuzz(3), 'Fizz') 
        self.assertEquals(FizzBuzz(6), 'Fizz')
        self.assertEquals(FizzBuzz(33), 'Fizz')  
   
    def test_returns_Buzz_when_number_is_devisable_by_5(self):
        self.assertEquals(FizzBuzz(5), 'Buzz') 
        self.assertEquals(FizzBuzz(10), 'Buzz')
        self.assertEquals(FizzBuzz(55), 'Buzz')
       
    def test_returns_FizzBuzz_when_number_is_devisable_by_5_and_3(self):
        self.assertEquals(FizzBuzz(15), 'FizzBuzz') 
        self.assertEquals(FizzBuzz(105), 'FizzBuzz')


if __name__ == '__main__':
	unittest.main()