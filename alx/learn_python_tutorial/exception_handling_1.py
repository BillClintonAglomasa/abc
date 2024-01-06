#!/usr/bin/python3

while 1:
    try:
        number = int(input('Please enter a number: '))
        break

    except ValueError:
        print('You did not enter a number')

    except:
        print('An unknown error occured')

print('Thank you for entering a number')
