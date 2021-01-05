#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = int(input("Сумма к оплате "))
    if s > 0:
        a1 = s // 500
        s1 = s - a1 * 500
        print("500руб. шт - ", a1)
        a2 = s1 // 100
        s2 = s1 - a2 * 100
        print("100руб. шт - ", a2)
        a3 = s2 // 10
        s3 = s2 - a3 * 10
        print("10руб. шт - ", a3)
        a4 = s3 // 5
        s4 = s3 - a4 * 5
        print("5руб. шт - ", a4)
        a5 = s4 // 2
        s5 = s4 - a5 * 2
        print("2руб. шт - ", a5)
        a6 = s5 // 1
        s6 = s5 - a6 * 1
        print("1руб. шт - ", a6)
    else:
        print("Денег нет")
