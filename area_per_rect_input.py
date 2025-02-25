#!/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: Feb 24, 2025
# The codes takes the input of the person and uses it to calculate the Perimeter and Area of a rectangle


def main():
    # Get the input from the user
    length = int(input("Enter length of the rectangle (cm): "))
    width = int(input("Enter width of the rectangle (cm): "))

    # formulas and calculations
    area = length * width
    perimeter = 2 * (length + width)

    # Display the results
    print("The area of the rectangle is:", area)
    print("The perimeter of the rectangle is:", perimeter)


if __name__ == "__main__":
    main()
