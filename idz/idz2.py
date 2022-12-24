#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def car_displ(*args):
    k = 0
    o = 0
    s1 = 0
    res = []
    for i in args:
        res.append(i)
           
    return (res)


if __name__ == "__main__":
    print(car_displ("toyota "," mark 1 ","mark 2 ", " mark3 "))
    print(car_displ("nissan "," 350 Z "," 450 Z "," 250fx "))
  
