#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

primelist = [2,3,5]

def gprime(limit = -1):
    for p in primelist:
        if limit < p:
            raise StopIteration
        yield p

    # 次が素数かチェック
#    p = p + 2
    d = (4 if p % 6 == 1 else 2)
    p = p + d
    d = 6 - d
    while p <= limit or limit < 0:
        try:
            (x for x in gprime(math.floor(math.sqrt(p))) if p % x == 0).next()
#            print "tugi", p
        except:
            primelist.append(p)
#            print "ok", p
            yield p
        p = p + d
        d = 6 - d
#        p = p + 2

if __name__ == '__main__':
    print(list(gprime(10000000))[-1])



