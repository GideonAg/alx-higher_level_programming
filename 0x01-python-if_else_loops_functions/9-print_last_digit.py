#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        print(number % 10)
        return (number % 10)
    else:
        number = -number
        number = number % 10
        print(f"-{number}")
        return (-number)
