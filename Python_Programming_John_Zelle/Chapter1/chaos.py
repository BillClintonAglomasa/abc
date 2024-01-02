#File: chaos.py
#A simple program illustratin chaotic behaviour

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Please enter the first number: "))
    y = eval(input("Please enter the second number: "))
    print("input   0.25     0.26")

    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("     ", x, "                    ", y)

main()
