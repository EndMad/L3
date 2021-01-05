#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

EPS = 1e-10

if __name__ == '__main__':
    x = float(input("x = "))
    if x == 1:
        print("Неправильное значение", file=sys.stderr)
        exit(1)
    a = x
    S, n = a, 1
    while math.fabs(a) > EPS:
        a *= 2 * x * n / (2 * n + 1) ** 2
        S += a
        n += 1
print(f"Shi({x}) = {S}")
