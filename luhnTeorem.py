# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 15:29:56 2022

@author: semih
"""

def luhnteorem(card_number):
    def kartinrakamlari(n):
        return[int(d) for d in str(n)]
    rakamlar = kartinrakamlari(card_number)
    cift_sayilar = rakamlar[-1::-2]
    tek_sayilar = rakamlar[-2::-2]
    toplam = 0
    toplam += sum(cift_sayilar)
    for d in tek_sayilar:
        toplam += sum(kartinrakamlari(d*2))
    return toplam %10

print("Gecerli") if luhnteorem("28961216094")==0 else print("Gecersiz")
    