# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ghj2cfaZXcnkRpTufu8U3b-V9hTqytPo
"""

def is_palindrome(num):
    return str(num) == str(num)[::-1]

for i in range(200, 300):
    if is_palindrome(i):
        print(i)
