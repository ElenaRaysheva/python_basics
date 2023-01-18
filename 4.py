""" width = 15
length = 55
height = 15 """

width = 45
length = 205
height = 45

if width <= 15 and length <= 15 and height <= 15:
  print('Коробка №1')
  exit()

for value in [width, length, height]:
  if value > 200:
    print('Упаковка для лыж')
    exit()

for value in [width, length, height]:
  if value > 15 and value < 50:
    print('Коробка №2')
    exit()

print('Коробка №3')

