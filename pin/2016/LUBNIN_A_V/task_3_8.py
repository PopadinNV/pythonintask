﻿# Задача 3. Вариант 8.
# Напишите программу, которая выводит имя "Борис Николаевич Бугаев", и
# запрашивает его псевдоним. Программа должна сцеплять две эти строки и
# выводить полученную строку, разделяя имя и псевдоним с помощью тире.

# Lubnin A.V.
# 04.04.2017

name = "Борис Николаевич Бугаев"
alias = "Андрей Белый"

print("Герой нашей сегодняшней программы - ", name)
getName = input("Под каким псевдонимом он известен? ")
if alias.upper() == getName.upper():
	print("Всё верно: ", name, " - ", alias)
else:
	print("Увы, но: ", name, " - ", alias)
input("\n \n Нажмите Enter для выхода")
