"""
File: rocket.py
Name:
-----------------------
This program implements a console-based application that
draws an ASCII art rocket.

The size of the rocket is determined by a constant named
SIZE, which is defined at the top of the file. The output
format should match the sample run shown in the Assignment 3 handout.
"""

# This constant determines rocket size.
SIZE = 3


def main():
    head()
    belt()
    upper()
    lower()
    belt()
    head()

def head():
    for i in range(SIZE):
        for j in range(SIZE - i):
            print(" ", end="") #空格數量等於SIZE-i數量

        print("/", end="")

        for j in range(2 * i):
            print(" ", end="")

        print("\\") #右邊的斜線

def belt():
    print("+", end="")

    for i in range(SIZE * 2):
        print("=", end="")

    print("+")

def upper():
    for i in range(SIZE):
        print("|", end="")

        for j in range(SIZE - 1 - i):
            print(".", end="")

        for j in range(i + 1):
            print("/", end="")
            print("\\", end="")

        for j in range(SIZE - 1 - i):
            print(".", end="")

        print("|")

def lower():
    for i in range(SIZE):
        print("|", end="")

        for j in range(i):
            print(".", end="")

        for j in range(SIZE - i):
            print("/", end="")
            print("\\", end="")

        for j in range(i):
            print(".", end="")

        print("|")




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
