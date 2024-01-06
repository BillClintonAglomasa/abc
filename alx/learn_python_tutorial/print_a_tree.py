#!/usr/bin/python3

Height_tree = eval(input('How tall is the tree: '))

harsh = '#'
width = Height_tree

for j in range(Height_tree):
    print(f'{harsh * j:^{width}} \n')

print(f'{harsh:^{width}}')
