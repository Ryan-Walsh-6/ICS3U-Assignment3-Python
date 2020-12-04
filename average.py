#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: December 2020
# this program calculates the average of three numbers between 1-100


def main():
    # this program checks if the number placed is negative or positive

    # input
    first_number = int(input("Enter the first number: "))
    print("")
    second_number = int(input("Enter the second number: "))
    print("")
    third_number = int(input("Enter the third number: "))
    print("")

    # process
    average = (first_number + second_number + third_number) / 3

    # output
    if (first_number <= 100 and first_number >= 0
       and second_number <= 100 and second_number >= 0
       and third_number <= 100 and third_number >= 0):
        print("The average of the three numbers is: {:,.2f}".format(average))
    else:
        print("These numbers are not all in between 0 and 100 and couldn't"
              " complete the function")


if __name__ == "__main__":
    main()
