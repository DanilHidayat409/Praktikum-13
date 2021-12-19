# -*- coding: utf-8 -*-
"""
@Hari/Tanggal : Minggu,191221
@Judul : Praktikum 13
@Materi : Algoritma dan pemrograman
@author: Muhammad Danil Hidayat
@NIM : 06500210032
"""

import pandas as pd

data = {'Negara': ['Indonesia', 'Jepang', 'India', 'China', 'Amerika Serikat', 'Brazil', 'Rusia', 'Meksiko', 'Nigeria', 'Jerman', 'Aljazair', 'Inggris'],
        'Ibu Kota': ['Jakarta', 'Tokyo', 'New Delhi', 'Beijing', 'Washington, D.C.', 'Brazilia', 'Moskow', 'Meksiko City', 'Abuja', 'Berlin', 'Aljazair', 'London'],
        'Benua': ['Asia', 'Asia', 'Asia', 'Asia', 'Amerika', 'Amerika', 'Asia', 'Amerika', 'Afrika', 'Eropa', 'Afrika', 'Eropa'],
        'Luas': [1905, 377, 3287, 9597, 9834, 8515, 17098, 1964, 923, 357, 2381, 242],
        'Populasi': [264, 143, 1252, 1357, 329, 210, 146, 126, 200, 83, 43, 66]}

df = pd.DataFrame(data)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print('Berikut Data Data Framenya: ')
print(df)
print('')
print('Berikut Data Mean: ')
print(mean)
print('')
print('Berikut Data Standard Deviation: ')
print(std)
print('')

