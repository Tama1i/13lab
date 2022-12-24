#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def car_displ(**cars):
    res = []
    for t,m in cars.items():
        res.append(f"{t} {m}")
           
    return (res)


if __name__ == "__main__":
    print(car_displ(mark1 = " toyota ",mark2 = " toyota ", mark3  =" toyota"))
    print(car_displ(Z350 = " nissan ",Z450 = " nissan ",fx250 = " nissan "))
  
