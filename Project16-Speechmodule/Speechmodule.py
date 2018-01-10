#!/usr/bin/env python
# coding:utf-8

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def check(number):
    result = []
    if number//100 != 0:
        result.append(FIRST_TEN[number//100-1])
        result.append(HUNDRED)
        number %= 100
    if 0 < number < 20:
        result.append((FIRST_TEN+SECOND_TEN)[number-1])
    elif number >= 20:
        result.append(OTHER_TENS[number//10-2])
        if number%10 != 0:
            result.append(FIRST_TEN[number%10-1])
    return ' '.join(result)


#大神解决方案
def check1(number):
    n = number // 100
    t = [FIRST_TEN[n-1], HUNDRED] if n > 0 else []

    n = (number // 10) % 10
    t += [OTHER_TENS[n-2]] if n > 1 else []

    n = number % (10 if n > 1 else 20)
    t += [(FIRST_TEN+SECOND_TEN)[n-1]] if n > 0 else []

    return ' '.join(t)


def check2(number):
    result = []
    if number >= 100:
        result.append(FIRST_TEN[number//100-1]+' {}'.format(HUNDRED))
    if (number%100)//10 > 1:
        result.append(OTHER_TENS[((number%100)//10)-2])
    if (number%100)//10 == 1:
        result.append(SECOND_TEN[number%10])
    elif (number%10) > 0:
        result.append(FIRST_TEN[number%10-1])
    return ' '.join(result)


if __name__ == '__main__':
    print(check(133))
    print(check1(133))
    print(check2(133))
