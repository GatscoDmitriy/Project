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
time.sleep(5)
clear()
f = open("1.txt" , "r")
print(*f)
time.sleep(3)
c = open("3.txt" , "r" , encoding="utf-8")
print(*c)
time.sleep(5)
print("Интересно, верно ли всё это или это очередной фейк, - думал Олег Владимирович, полковник в запасе.")
print("Он ещё не знал о том что произойдет в его квартире через два месяца....")
time.sleep(8)
clear()
print("Два месяца спустя.....")
print("""Уже 2 месяца прошло с тех пор как пришельцы высадились на Землю и начали войну с человечеством.
Тяжела была эта война, пришельцы, высадившиеся в Сибири за несколько дней успели дойти до Китая и Индии, Захватили Аляску и рвутся к Москве....""")
ime.sleep(8)
a = open("4.txt" , "r" , encoding="utf-8")
print(*a)
c = input("Решение Да - Олег Владимирович со своей семьёй уезжает из города. Решение Нет - Олег Владимирович отправляется на фронт с пришельцами")
if c == " Да":
    clear()
    print('Концовка "Сбежавшие" Олег Владимирович с семьёй уезжают из Москвы, их дальнейшая судьба неизвестна. Статус Концовки: Нейтральная')
    time.sleep(8)
    exit()
elif c == 'Нет':
    print("hf")
