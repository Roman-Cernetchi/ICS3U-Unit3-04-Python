#!/usr/bin/env python
#
# Created by: Roman Cernetchi
# Created on: December 2020
# This program checks if a number is positive, negative, or neither

import math


def main():
    # This function checks if the number is positive, negative, or 0

    # Input

    chosen_number = int(input("Enter the number you have chosen: "))
    print("")

    # process
    if chosen_number > 0:
        # Output
        print("The number is positive")

    elif chosen_number < 0:
        # Output
        print("The number is negative")

    else:
        print("This number is a 0")


if __name__ == "__main__":
    main()
