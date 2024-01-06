#!/usr/bin/python3

#example of using a for statement

words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))

users = {'Hans': 'active', 'Sasm': 'inactive', 'Jone': 'active'}

for user, status in users.copy.item():
    if user == 'active':
        del users[user]

active_users = {}
for use, status in users.item():
    if status == 'active':
        active_users[user] = status
