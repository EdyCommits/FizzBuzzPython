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
   

     


if __name__ == '__main__':
	unittest.main()