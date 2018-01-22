#!/usr/bin/env python
# coding:utf-8

def check1(time):
    hour, minute = time.split(':')
    hour = int(hour) + int(minute) * 1.0 / 60
    if hour > 12:
        hour -= 12
    angel_hour = hour/12*360
    angel_minute = int(minute) / 60.0 * 360
    if angel_minute > angel_hour:
        clock_angle = round(abs(angel_minute-angel_hour), 1)
    else:
        clock_angle = round(abs(angel_hour-angel_minute), 1)
    if clock_angle <= 180:
        return clock_angle
    else:
        return 360 - clock_angle


def check2(time):
    '''
abs(360/12 * (hour%12 + minutes/60) - 360/12 * minutes/5)
abs(30 * hour%12 + 30 * minutes/60 - 30 * minutes/5)
abs(30 * hour%12 + 30 * minutes/60 - 360 * minutes/60)
abs(30 * hour%12 - 330 * minutes/60)
abs(30 * hour%12 - 5.5 * minutes)
    '''
    hour, minutes = map(int, time.split(':'))
    angle = abs(30*(hour%12) - 5.5*minutes)
    return min(angle, 360-angle)


if __name__ == '__main__':
    print(check1('13:42'))
    print(check2('13:42'))

