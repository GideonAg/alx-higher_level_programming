#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        print(number % 10)
    else:
        print(f"-{number % 10}")