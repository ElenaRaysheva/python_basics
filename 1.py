
# phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
# phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

# phrase_1 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
# phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'

phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'

if len(phrase_1) > len(phrase_2):
  print('Фраза 1 длиннее фразы 2')
elif len(phrase_2) > len(phrase_1):
  print('Фраза 2 длиннее фразы 1')
else:
  print('Фразы равной длины')
