from sys import argv

script_salary, salary, hours, premium = argv

pay = int(salary) * int(hours) + (int(premium) * 0.9)

print(f'Ваша ЗП c учетом премии: {pay}')
