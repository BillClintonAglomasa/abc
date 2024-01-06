#!/usr/bin/python3

#take in two integers and split and work with them
num1, num2 = input('Please enter two integers: ').split()

#convert string
num1 = int(num1)
num2 = int(num2)

#sum
sum = num1 + num2

#difference
difference = num1 - num2

#remainder
remainder = num1 % num2

#floor_division
floor_division = num1 / num2

#product
product = num1 * num2
print('\n About to print the output \n')
print(f'{num1} + {num2} = {sum}')
print(f'{num1} - {num2} = {difference}')
print(f'{num1} % {num2} = {remainder}')
print(f'{num1} / {num2} = {floor_division}')
print(f'{num1} * {num2} = {product}')
