#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# При покупке товара на сумму от 200 до 500 руб предоставляется скидка 3%,
# при покупке товара на сумму от 500 до 800 - скидка 5%,
# при покупке товара на сумму от 800 до 1000 руб- скидка 7%,
# свыше 1000 руб - скидка 9%.
# Покупатель приобрел 8 рулонов обоев по цене Х и две банки краски по цене Х.
# Сколько он заплатил?

if __name__ == '__main__':
    x1 = int(input("Цена рулона обоев "))
    x2 = int(input("Цена банки краски "))
    priobrel = (x1*8) + (x2*2)
    print("Цена без скидки ", priobrel)
    priobrel3 = priobrel - priobrel*0.03
    priobrel4 = priobrel - priobrel*0.05
    priobrel5 = priobrel - priobrel*0.07
    priobrel6 = priobrel - priobrel*0.09
    if 200 < priobrel < 500:
        print("Ваша скидка 3%")
        print("К оплате ", priobrel3)
    elif 500 < priobrel < 800:
        print("Ваша скидка 5%")
        print("К оплате ", priobrel4)
    elif 800 < priobrel < 1000:
        print("Ваша скидка 7%")
        print("К оплате ", priobrel5)
    elif priobrel > 1000:
        print("Ваша скидка 9%")
        print("К оплате ", priobrel6)
    print("Спасибо за покупку!")
