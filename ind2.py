#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 2. В кортеже, состоящем из вещественных элементов, вычислить:
# 1) сумму положительных элементов кортежа;
# 2) произведение элементов кортежа, расположенных между максимальным по модулю и минимальным по модулю элементами.
# Сортировать элементы списка по убыванию.

if __name__ == '__main__':
    a = (5, 10, -2, 0, 3, -5)
    s = 0
    p = 1
    for el in a:
        p *= el
        if el > 0:
            s += el

    d = tuple(sorted(a, reverse=True))

print("Сумма положительных элементов списка = ", s)
print("Произведение элементов списка, расположенных между максимальным и минимальным элементами = ", p)
print("Элементы, расположенные по убыванию: ", d)
