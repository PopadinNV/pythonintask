#Задача 7. Вариант 16.
#Создайте игру, в которой компьютер загадывает 
#имя одной из шести официальных жен
#Ивана IV Грозного, а игрок должен его угадать.

#feokritova A.V.
#7.04.2017

import random
print('Программа случайным образом загадывает имя одной из шести официальных жен Ивана IV Грозного.')
tries = 1
score = 2000
number = random.randint(1,6)
if number == 1:
	realname = 'Анастасия Романовна'
elif number == 2:
	realname = 'Мария Темрюковна'
elif number == 3:
	realname = 'Марфа Собакина'
elif number == 4:
	realname = 'Анна Колтовская'
elif number == 5:
	realname = 'Анна Васильчикова'
else :
	realname = 'Мария Нагая'
name = input('\n\nНазовите имя одной из шести официальных жен Ивана IV Грозного:')
while name != realname:
	tries += 1
	score -= 100
	name = input('\n\nПопробуйте снова:')
print('Верно! Это', realname, 'Вам потребовалось', tries, 'попыток')
print('Начислено' , score , 'очков')

input('\n\nPress Enter')