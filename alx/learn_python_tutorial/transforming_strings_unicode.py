#!/usr/bin/python3

#taking in input
str_entered = input('Please enter string in uppercase: ')

#creating an empty string and saving the unicode values
str_unicode = ''
for i in str_entered:
    #convert to unicode
    str_unicode += str(ord(i))
print('Encoded message is ', str_unicode)

#converting the unicode back to characters
new_str = ''
i = 0
while (i < len(str_unicode)):
    new_str += chr(int(str_unicode[i:i+2]))
    i += 2

#different implementation for assigning to new_str using for loop
other_str = ''
len_str = len(str_unicode) - 1
for i in range(0, len_str, 2):
    char = str_unicode[i] + str_unicode[i + 1]
    other_str += chr(int(char))

print('Original message', new_str)
print('Other message ', other_str)
