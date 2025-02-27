# Write a function to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example function call
#
# factorial(5)
#
# > 120
#

def factorial(n):
    # iterate from 1 up to the number passed in
    for i in range(1, n+1):
        j = i * i
        j *= i
    print(j)

factorial(5)
