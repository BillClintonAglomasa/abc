#!/usr/bin/python3

#simple program to determine grade an individual
#should be admitted to depending on age

#accepting input
age = eval(input("Please type in your age: "))

if (age == 5):
    print('Go to Kindergarten')
elif (age >= 6) and (age <= 17):
    print('Designated to grades 1 through 12')
elif (age > 17):
    print('Go to college')
else:
    print('You are not qualified to be graded')
