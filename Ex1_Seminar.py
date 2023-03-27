from sympy import isprime

n = int(input('Введите число: '))

def numb(n):
    if isprime(n) == True:
        print('число простое')
    else:
        print('Число не простое')

numb(n)