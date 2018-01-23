#!/usr/bin/env python
# coding:utf-8


def check1(text):
    words = text.split(' ')
    result = []
    for word in words:
        if word.startswith('$'):
            if word.endswith(',') or word.endswith('.'):
                front = word[:-4].replace('.', ',')
                back = word[-4:-1].replace(',', '.', 1)
                rest = word[-1]
                new_word = front+back+rest
            else:
                front = word[:-3].replace('.', ',')
                back = word[-3:].replace(',', '.', 1)
                new_word = front+back
            result.append(new_word)
        else:
            result.append(word)
    return ' '.join(result)


if __name__ == '__main__':
    str = 'Us Style = $12,345.67, Euro Style = $12.345,67'
    print(check1(str))
