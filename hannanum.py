#!/usr/bin/env python3

#check if a number is a Hanna-number
# Hanna-numbers are numbers that can be expressed as the sum of their digits raised to the power of the sum of one of their digits.
def is_h_num(num):
    digitz = []
    n = num
    while n > 0:
        digitz.append(n%10)
        n //= 10
    digitz.sort()
    the_sum = sum(digitz)
    for digit in digitz:
        n = digit ** the_sum
        if n > num:
            break
        if n == num:
            print(digit, the_sum, num)

# check if a number is a reverse-Hanna-number
# reverse-Hanna-numbers are numbers that can be expressed as the sum of their digits raised to the power of the sum of one of their digits.
def is_h_num_reverse(num):
    digitz = []
    n = num
    while n > 0:
        digitz.append(n%10)
        n //= 10
    digitz.sort()
    the_sum = sum(digitz)
    for digit in digitz:
        n = the_sum ** digit
        if n > num:
            break
        if n == num:
            print(digit, the_sum, num)

# finds Hanna-numbers and reverse-Hanna-numbers in a given range
def h_num_finder(max_num, is_reverse=False):
    if is_reverse:
        for i in range(max_num + 1):
            is_h_num_reverse(i)
    else:
        for i in range(max_num + 1):
            is_h_num(i)

def main():
    h_num_finder(10 ** 6)


if __name__ == '__main__':
    main()