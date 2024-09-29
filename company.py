"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.

Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.

13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""
import sys
from audioop import reverse
from collections import defaultdict
from typing import Any, Dict, NoReturn

from utils import delimiter

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

# -------------------------------------------------------
# Task 1
# 1. Вывести названия всех отделов
# -------------------------------------------------------
delimiter()
department_names = [department['title'] for department in departments]
print('All departments names:', *department_names, sep='\n')

# -------------------------------------------------------
# Task 2
# 2. Вывести имена всех сотрудников компании.
# -------------------------------------------------------
delimiter()
employer_names = [
    employer['first_name'] for department in departments for employer in department['employers']
]
print('All employer names:', *employer_names, sep='\n')

# -------------------------------------------------------
# Task 3
# 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
# -------------------------------------------------------
delimiter()
rv = [
    (department['title'], employer['first_name']) for department in departments for employer in department['employers']
]
print('All employer names with hist/her department:', *rv, sep='\n')

# -------------------------------------------------------
# Task 4
# 4. Вывести имена всех сотрудников компании, которые получают больше 100к.
# -------------------------------------------------------
delimiter()
rv = [
    emp['first_name'] for dep in departments for emp in dep['employers'] if emp['salary_rub'] > 100000
]
print('All employer names with salary more than 100000:', *rv, sep='\n')

# -------------------------------------------------------
# Task 5
# 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
# -------------------------------------------------------
delimiter()
rv = {emp['position'] for dep in departments for emp in dep['employers'] if emp['salary_rub'] < 80000}
print('All positions with salary less than 80000:', *rv, sep='\n')

# -------------------------------------------------------
# Task 6
# 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
# -------------------------------------------------------
delimiter()
expenses = defaultdict(int)
for department in departments:
    for employer in department['employers']:
        title = department['title']
        expenses[title] += employer['salary_rub']
print('Expenses for each department:', *expenses.items(), sep='\n')

# -------------------------------------------------------
# Task 7
# 7. Вывести названия отделов с указанием минимальной зарплаты в нём.
# -------------------------------------------------------
delimiter()
min_salary_by_department = defaultdict(lambda: sys.maxsize)
for department in departments:
    for employer in department['employers']:
        title = department['title']
        salary = employer['salary_rub']
        min_salary_by_department[title] = min(salary, min_salary_by_department[title])
print('Minimal salary for each department:', *min_salary_by_department.items(), sep='\n')

# -------------------------------------------------------
# Task 8
# 8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
# -------------------------------------------------------
delimiter()
salary_info = {
    'employer_num': 0,
    'min': sys.maxsize,
    'max': 0,
    'avg': 0,
    'total': 0
}
salary_info_by_department = defaultdict(salary_info.copy)
for department in departments:
    for employer in department['employers']:
        title = department['title']
        department_info = salary_info_by_department[title]
        salary = employer['salary_rub']

        department_info['min'] = min(salary, department_info['min'])
        department_info['max'] = max(salary, department_info['max'])
        department_info['total'] += salary
        department_info['employer_num'] += 1
        department_info['avg'] += department_info['total'] / department_info['employer_num']
print('Salary info for each department:', *salary_info_by_department.items(), sep='\n')

# -------------------------------------------------------
# Task 9
# 9. Вывести среднюю зарплату по всей компании.
# -------------------------------------------------------
delimiter()
total, employer_num = 0, 0
for department in departments:
    for employer in department['employers']:
        total += employer['salary_rub']
        employer_num += 1
avg = total / employer_num
print('Average salary:', avg)

# -------------------------------------------------------
# Task 10
# 10. Вывести названия должностей, которые получают больше 90к без повторений.
# -------------------------------------------------------
delimiter()
rv = {
    emp['position'] for dep in departments for emp in dep['employers'] if emp['salary_rub'] > 90000
}
print('Positions with salary amount more than 90000:', *rv, sep='\n')

# -------------------------------------------------------
# Task 11
# 11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
# -------------------------------------------------------
delimiter()
ladies = {'Michelle', 'Nicole', 'Christina', 'Caitlin'}
rv = {
    emp['salary_rub'] for dep in departments for emp in dep['employers'] if emp['first_name'] in ladies
}
avg = sum(rv) / len(rv)
print('Ladies average salary:', avg, sep='\n')

# -------------------------------------------------------
# Task 12
# 12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
# -------------------------------------------------------
delimiter()
vowels = ('A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y')
rv = {
    emp['last_name'] for dep in departments for emp in dep['employers'] if emp['last_name'].endswith(vowels)
}
print('Lastnames with a vowel at the end:', *rv, sep='\n')

# Третий уровень:
# Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
# Если department None, значит, этот налог применяется ко всем сотрудникам компании.
# Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
# К одному сотруднику может применяться несколько налогов.

# -------------------------------------------------------
# Task 13
# 13. Вывести список отделов со средним налогом на сотрудников этого отдела.
# -------------------------------------------------------
delimiter()
tax_info = {
    'salary_sum': 0,
    'tax_sum': 0,
    'employer_num': 0,
    'tax_avg': 0
}
tax_info_by_department = defaultdict(tax_info.copy)
for department in departments:
    for employer in department['employers']:
        title = department['title']
        employer_tax_departments = [title.lower()]
        salary = employer['salary_rub']
        tax_sum = 0
        for tax in taxes:
            tax_department = tax['department']
            if tax_department is None:
                tax_sum += salary * tax['value_percents'] * 0.01
            elif tax['department'].lower() in employer_tax_departments:
                tax_sum += salary * tax['value_percents'] * 0.01

        department_tax_info = tax_info_by_department[title]
        department_tax_info['salary_sum'] += salary
        department_tax_info['tax_sum'] += tax_sum
        department_tax_info['employer_num'] += 1
        department_tax_info['tax_avg'] = department_tax_info['tax_sum'] / department_tax_info['employer_num']
print('Average taxes by department:', *tax_info_by_department.items(), sep='\n')

# -------------------------------------------------------
# Task 14
# 14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
# -------------------------------------------------------
delimiter()
tax_info_by_employer = list()
for department in departments:
    for employer in department['employers']:
        title = department['title']
        employer_tax_departments = [title.lower()]
        name = employer['first_name']
        salary = employer['salary_rub']
        tax_sum = 0
        for tax in taxes:
            tax_department = tax['department']
            if tax_department is None:
                tax_sum += salary * tax['value_percents'] * 0.01
            elif tax['department'].lower() in employer_tax_departments:
                tax_sum += salary * tax['value_percents'] * 0.01
        tax_info = {
            'name': name,
            'salary_with_taxes': salary,
            'salary_without_taxes': salary - tax_sum
        }
        tax_info_by_employer.append(tax_info)
print('Salary and taxes info by employer name:', *tax_info_by_employer, sep='\n')

# -------------------------------------------------------
# Task 15
# 15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
# -------------------------------------------------------
delimiter()
tax_info = {
    'salary_sum': 0,
    'tax_sum': 0,
    'employer_num': 0,
    'tax_avg': 0
}
tax_info_by_department = defaultdict(tax_info.copy)
for department in departments:
    for employer in department['employers']:
        title = department['title']
        employer_tax_departments = [title.lower()]
        salary = employer['salary_rub']
        tax_sum = 0
        for tax in taxes:
            tax_department = tax['department']
            if tax_department is None:
                tax_sum += salary * tax['value_percents'] * 0.01
            elif tax['department'].lower() in employer_tax_departments:
                tax_sum += salary * tax['value_percents'] * 0.01

        department_tax_info = tax_info_by_department[title]
        department_tax_info['salary_sum'] += salary
        department_tax_info['tax_sum'] += tax_sum
        department_tax_info['employer_num'] += 1
        department_tax_info['tax_avg'] = department_tax_info['tax_sum'] / department_tax_info['employer_num']
rv = sorted(tax_info_by_department.items(), key=lambda x: x[1].get('tax_sum'),reverse = True)
print('Departments sorted by high taxes:', *rv, sep='\n')

# -------------------------------------------------------
# Task 16
# 16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
# -------------------------------------------------------
delimiter()
tax_info_by_employer = list()
for department in departments:
    for employer in department['employers']:
        title = department['title']
        employer_tax_departments = [title.lower()]
        name = employer['first_name']
        salary = employer['salary_rub']
        tax_sum = 0
        for tax in taxes:
            tax_department = tax['department']
            if tax_department is None:
                tax_sum += salary * tax['value_percents'] * 0.01
            elif tax['department'].lower() in employer_tax_departments:
                tax_sum += salary * tax['value_percents'] * 0.01
        if tax_sum < 100000:
            continue
        tax_info = {
            'name': name,
            'salary_with_taxes': salary,
            'salary_without_taxes': salary - tax_sum,
            'tax_sum': tax_sum
        }
        tax_info_by_employer.append(tax_info)
print('Employers with taxes more than 100000:', *tax_info_by_employer, sep='\n')

# -------------------------------------------------------
# Task 17
# 17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
# -------------------------------------------------------
delimiter()
min_employer, min_tax = [], sys.maxsize
for department in departments:
    for employer in department['employers']:
        title = department['title']
        employer_tax_departments = [title.lower()]
        name = employer['first_name']
        salary = employer['salary_rub']
        tax_sum = 0
        for tax in taxes:
            tax_department = tax['department']
            if tax_department is None:
                tax_sum += salary * tax['value_percents'] * 0.01
            elif tax['department'].lower() in employer_tax_departments:
                tax_sum += salary * tax['value_percents'] * 0.01
        tax_info = {
            'name': name,
            'salary_with_taxes': salary,
            'salary_without_taxes': salary - tax_sum,
            'tax_sum': tax_sum
        }

        if tax_sum < min_tax:
            min_employer, min_tax = [tax_info], tax_sum
        elif tax_sum == min_tax:
            min_employer.append(tax_info)

print('Employers with minimal taxes:', *min_employer, sep='\n')
exit()
