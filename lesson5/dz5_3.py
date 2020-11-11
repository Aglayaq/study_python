"""
Создать текстовый файл (не программно), 
построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
"""

f_obj = open('sotrud.txt', 'r', encoding='utf-8')

totsalary = 0
nsotrud = 0

for s in f_obj:
    nsotrud += 1
    l = s.split()
    name = l[0]
    salary = int(l[1])
    totsalary += salary
    if salary < 20000:
        print(name)

print('Средняя зарплата: ', totsalary/nsotrud)
