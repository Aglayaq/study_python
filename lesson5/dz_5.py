"""

5. Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и 
 выводить ее на экран.

"""

out_f = open("5_file.txt", "w")
out_f.write('7 23 4 6 32')
out_f.close()

in_f = open("5_file.txt","r")
summ = 0
while True:
    content = in_f.read( 1024 )
    if not content:
        break

    n = content.split(' ')
    for i in n:
        summ = summ + float(i)

in_f.close()
print('Сумма =', summ)
