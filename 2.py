# year = 2020
year = 2019

if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
  print('Високосный год')
else:
  print('Обычный год')
