#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Определить, есть ли среди трёх заданных чисел чётные.

if __name__ == '__main__':
    x1 = int(input("Введите первое число "))
    x2 = int(input("Введите второе число "))
    x3 = int(input("Введите третье число "))
    if x1 & 1:
        print("Первое число - нечетное")
    else:
        print("Первое число - четное")
    if x2 & 1:
        print("Второе число - нечетное")
    else:
        print("Второе число - четное")
    if x3 & 1:
        print("Третье число - нечетное")
    else:
        print("Третье число - четное")
