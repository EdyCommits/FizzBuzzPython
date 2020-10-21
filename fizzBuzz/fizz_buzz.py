def FizzBuzz(num):
    if num % 15 == 0:
        print('FizzBuzz')
        return 'FizzBuzz'
    elif num % 3 == 0:
        print('Fizz')
        return 'Fizz'
    elif num % 5 == 0:
        print('Buzz')
        return 'Buzz'
    else:
        print(num) 
        return num
    
    