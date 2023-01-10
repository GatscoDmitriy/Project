player = input("Введите игровое имя")
import os
import time
def clear():
    os.system('cls')
print("Приветствую в этой игре" , player)
print("Начнём.............")
time.sleep(5)
clear()
print( "2022 год. Альтернативня Вселенная:")
print("Дорогая, завари кофейку, пож")
print("Хорошо сейчас, включи пока новости")
f = open("1.txt" , "r")
print(*f)