day = int(input('Введите день: '))
month = input('Введите месяц: ')
if month == 'Декабрь':
  sign = 'Стрелец' if (day < 22) else 'Козерог'
elif month == 'Январь':
  sign = 'Козерог' if (day < 20) else 'Водолей'
elif month == 'Февраль':
  sign = 'Водолей' if (day < 19) else 'Рыбы'
elif month == 'Март':
  sign = 'Рыбы' if (day < 21) else 'Овен'
elif month == 'Апрель':
  sign = 'Овен' if (day < 20) else 'Телец'
elif month == 'Май':
  sign = 'Телец' if (day < 21) else 'Близнецы'
elif month == 'Июнь':
  sign = 'Близнецы' if (day < 21) else 'Рак'
elif month == 'Июль':
  sign = 'Рак' if (day < 23) else 'Лев'
elif month == 'Август':
  sign = 'Лев' if (day < 23) else 'Дева'
elif month == 'Сентябрь':
  sign = 'Дева' if (day < 23) else 'Весы'
elif month == 'Октябрь':
  sign = 'Весы' if (day < 23) else 'Скорпион'
elif month == 'Ноябрь':
  sign = 'Скорпион' if (day < 22) else 'Стрелец'
print('Ваш знак зодиака: ',sign)
