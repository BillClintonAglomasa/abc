#!/usr/bin/python3

#Determine if an int is odd or even

#input
#num = eval(input('Enter number'))
for i in range(1,21):
    if ((i % 2) == 0):
        print(f'{i} is an even number')
    else:
        print(f'{i} is an odd number')
