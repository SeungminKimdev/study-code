for i in range(3):
    string = input().rstrip()
    if string not in ['FizzBuzz','Fizz','Buzz']:
        n = int(string) + (3-i)
        break

if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
elif n % 3 == 0:
    print('Fizz')
elif n % 5 == 0:
    print('Buzz')
else:
    print(n)