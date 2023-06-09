#В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.


from datetime import date


def chislo(x):
    for i in range(len(x)):
        x[i] = int(x[i])
    try:
        date(x[0], x[1], x[2])
        return True
    except:
        return False


x = input('Введите год, месяц и день через пробел: ').split()
print(chislo(x))
