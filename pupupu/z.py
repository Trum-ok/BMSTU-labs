x = abs(float(input('Введите x: ')))
y = float(input('Введите y: '))


def y1(x):
    return (-1/8) * (x-9)**2 + 8

def y2(x):
    return 7*(x-8)**2 + 1

def y3(x):
    return (1/49) * (x-1)**2

def y4(x):
    return -4*x**2 + 2

def y5(x):
    return 4*x**2 - 6

def y6(x):
    return (-1/16) * x**2

def y7(x):
    return -2*(x-1)**2 - 2

def y8(x):
    return (1/3) * (x - 5)**2 - 7
 

if y >= 0:
    if x >= 1 and x <= 9:
        if x >= 8 and x <= 9:
            if (y >= y2(x)) and (y1(x) >= y):
                print('Точка принаджелит')
            else:
                print('Точка не принадлежит')
        elif x >= 1 and x <= 8:
            if (y3(x) <= y) and (y1(x) >=y):
                print('Точка принаджелит')
            elif y == 1.5*(x) + 2:
                print('Точка принаджелит')
            else:
                print('Точка не принадлежит')
        else:
            print('Точка не принадлежит')
                
    elif x >= 0 and x <= 1:
        if y == 1.5*(x) + 2:
            print('Точка принаджелит')
        elif (y >= y5(x)) and (y <= y4(x)):
            print('Точка принадлежит')
        else:
            print('Точка не принадлежит')
    else:
        print('Точка не принадлежит')

elif y < 0:
    if x >= 2 and x <= 8:
        if (y >= y8(x)) and (y <= y6(x)):
            print('Точка принадлежит')
        else:
            print('Точка не принадлежит')
    elif x >= 1 and x <= 8:
        if (y >= y7(x)) and (y <= y6(x)):
            print('Точка принадлежит')
        else:
            print('Точка не принадлежит')
    elif x >= 0 and x <= 1:
        if (y >= y5(x)) and (y <= y4(x)):
            print('Точка принадлежит')
        else:
            print('Точка не принадлежит')
    else:
        print('Точка не принадлежит')
else:
    print('Точка не принадлежит!')
