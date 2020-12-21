import itertools

for i in itertools.count(3, 4):
    print(i)
    if i > 20:
        break

print('Вторая часть. Чтобы прервать цикл нажмите Ctrl+C')
test = [n for n in range(3, 10)]
try:
    for i in itertools.cycle(test):
        print(i)
except KeyboardInterrupt:
    print('Цикл завершен')
