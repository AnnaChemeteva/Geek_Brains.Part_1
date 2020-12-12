start = 2
purpose = 3
progress = 10

day = 0

while purpose >= start:
    day += 1
    result = (start * progress) / 100
    start = result + start
    print(f'День - {day}, Результат - {start:.2f} км')

print(f'Спортсмен достигнет цели на {day} день')
