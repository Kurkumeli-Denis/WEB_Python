#Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
y = '/Users/deniskurkumeli/Desktop/Python/1_Lesson/DZ1.py'
z = y.split('/')
arr = [y]
for i in range(len(z)):
    if(i == len(z) - 1):
        arr.append(z[i])
        p = z[i].split('.')

        for j in range(len(p)):
            if(j == len(p) - 1):
                arr.append(p[j])

x = tuple(arr)

print(x)