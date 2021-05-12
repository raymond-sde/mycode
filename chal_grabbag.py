#!/usr/bin/env python3
import math

# Function Grab Bag!
# 1. Write a Python function to find the Max of three numbers.
def find_max(num1, num2, num3):
    result = -math.inf

    if num1 > result:
        result = num1
    if num2 > result:
        result = num2
    if num3 > result:
        result = num3

    return result


# 2. Write a Python function to sum all the numbers in a list.
def get_sum(list):
    result = 0

    for num in list:
        result += num

    return result


# 3. Write a Python function to multiply all the numbers in a list.
def get_product(list):
    result = 1

    for num in list:
        result *= num

    return result


# 4. Write a Python program to reverse a string.
def reverse_str(str):
    result = ""

    for char in reversed(str):
        result += char

    return result


# 5. Write a Python function to check whether a number is in a given range.
def is_in_range(num, range):
    return num >= range[0] and num <= range[1]


# 6. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def count_case(str):
    lower = 0
    upper = 0

    for char in str:
        if char.isalpha():
            if char.islower():
                lower += 1
            else:
                upper += 1

    print(f"No. of Lower case characters : {lower}")
    print(f"No. of Upper case characters : {upper}")


# 7. Write a Python function that takes a list and returns a new list with unique elements of the first list.
def remove_duplicates(list):
    newlist = []

    for item in list:
        if item not in newlist:
            newlist.append(item)

    return newlist


# 9. Write a Python program to print the even numbers from a given list.
def is_even(list):
    for num in list:
        if num % 2 == 0:
            print(num)


# 10. Write a Python function that checks whether a passed string is palindrome or not.
def is_palindrome(str):
    return str == reverse_str(str)


# 12. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
def alphabetize_words(str):
    str = str.split("-")
    str.sort()
    print("-".join(str))
