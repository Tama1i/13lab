#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def s(*args):
    k = 0
    o = 0
    s1 = 0
    for i in args:
        k += 1
        if i < 0:
            kk = k
    for i in args:
         if i < kk:
            if o == 1:
                s1 += i
            if i < 0:
                o = 1
           
    return (s1)


if __name__ == "__main__":
    print(s(3, -7, 1, 6, 9, -5, -6, 9, 4, -8, 3, 5))
    print(s(-2,3,1,4,24,-5,-4,-4, 2,46,-2 ,25,3))
  
