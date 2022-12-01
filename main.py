#print('hello')
import math
print('1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.')

def exe1(x):
    if x <=0 or x >= 8:
        return print('не корректное число')
    elif x >= 0 and x <= 5: 
        return print('будни')
    else: return print('выходной')
#day = int(input('Введите день недели: '))
#exe1(day)

print('3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).')

def exe3(x, y):
    if x == 0 and y==0:
        return print('x = 0, y = 0')
    elif x > 0 and y > 0:
        return print('1 четверть')
    elif x > 0 and y < 0:
        return print('2 четверть')
    elif x < 0 and y < 0:
        return print('3 четверть')
    else: return print('4 четверть')
#x = int(input('Введите x: '))
#y = int(input('Введите y: '))
#exe3(x , y)

print('4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).')
def exe4(half):
    if half <=0 or half >= 5:
        return print('не корректное число')
    elif half == 1:
        return print('x: [0, +∞], y: [0, +∞]')
    elif half == 2:
        return print('x: [0, +∞], y: [0, -∞]')
    elif half == 3:
        return print('x: [0, -∞], y: [0, -∞]')
    else: return print('x: [0, -∞], y: [0, +∞]')
#half = int(input('Введите четверть: '))
#exe4(half)

print('5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.')
def exe5(x1, y1, x2,y2):
    s = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return print('расстояние между 2-мя точками', s)
x1 = int(input('Введите координаты X 1 числа: '))
y1 = int(input('Введите координаты Y 1 числа: '))
x2 = int(input('Введите координаты X 2 числа: '))
y2 = int(input('Введите координаты Y 2 числа: '))
exe5(x1, y1, x2, y2)
       

    