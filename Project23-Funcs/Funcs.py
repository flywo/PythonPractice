#!/usr/bin/env python
# coding:utf-8


def check(f,g):
    def h(*args, **kwargs):
        fresult,gresult,errorf,errorg = None,None,None,None
        try:
            fresult = f(*args, **kwargs)
        except:
            errorf = 'f_error'
        try:
            gresult = g(*args, **kwargs)
        except:
            errorg = 'g_error'

        if (errorg != None and errorf != None) or \
                (fresult == None and gresult == None):
            return None, 'both_error'
        elif errorg != None or gresult == None:
            return fresult, 'g_error'
        elif errorf != None or fresult == None:
            return gresult, 'f_error'
        else:
            if fresult == gresult:
                return fresult, 'same'
            else:
                return fresult, 'different'
    return h


def check1(*funcs):
    def helper(*args, **kwargs):
        output = result = None
        status = 'same'
        for i,f in enumerate(funcs, ord('f')):
            try: result = f(*args, **kwargs)
            except: result = None
            if result == None:
                status = [chr(i), 'both']['error' in status] + '_error'
            elif output == None: output = result
            elif result != output: status = 'different'
        return output, status
    return helper


def check2(f,g):
    def c(f, *args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return None
    def h(*args, **kwargs):
        fr = c(f, *args, **kwargs)
        gr = c(f, *args, **kwargs)
        return {
            (False, False): (None, 'both_error'),
            (True, False): (fr, 'g_error'),
            (False, True): (gr, 'f_error'),
            (True, True): (fr, {True: 'same', False: 'different'}[fr == gr])
        }[(fr != None, gr != None)]
    return h

if __name__ == '__main__':
    print(check1(lambda x,y:x+y,
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,1.01))