"""3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
 Напишите решения через list и через dict."""

# seasons = ['зима','зима','весна','весна','весна','лето','лето','лето',
#            'осень','осень','осень','зима']
# a = int(input('Введите номер месяца в диапазоне от 1 до 12: '))
# print(seasons[a-1])
seasons = {1:'зима',2:'зима',3:'весна',4:'весна',5:'весна',6:'лето',7:'лето',8:'лето',
           9:'осень',10:'осень',11:'осень',12:'зима'}
a = int(input('Введите номер месяца в диапазоне от 1 до 12: '))
print(seasons[a])
