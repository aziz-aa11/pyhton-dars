# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 19:05:54 2025

@author: User
"""


narh = 15000
choy = True
salat = True
if choy and salat:
    narh = narh + 10000
elif choy or salat:
    narh = narh +5000
print(f"Jami {narh} so`m")


narh = 15000
choy = True
salat = False
assorti = True
non = 1
kompot = 1
if choy:
    print("Mijoz choy oldi")
    narh = narh + 5000
if salat:
    print("Mijoz salat oldi")
    narh = narh + 12000
if assorti:
    print("Mijoz assorti oldi")
    narh = narh + 22000
if non:
    print("Mijoz non oldi")
    narh = narh + 5000
if kompot:
    print("Mijoz kompot oldi")
    narh = narh + 8500
print(f"Jami {narh}")


menu = ['osh', 'somsa', 'xonim', 'norin', 'shashlik']
ovqat = input("Nima ovqat yeysiz? ")
if ovqat.lower() in menu:
    print("Buyurtma qabul qilindi")
else:
    print("Bunday ovqat yo`q")



menu = ['osh', 'somsa', 'xonim', 'norin', 'shashlik']
buyurtmalar = ['somsa', 'norin', 'manti', 'shashlik']
for taom in buyurtmalar:
    if taom in menu:
        print(f"Menyuda {taom} bor")
    else:
        print(f"Menyuda {taom} yo`q")
