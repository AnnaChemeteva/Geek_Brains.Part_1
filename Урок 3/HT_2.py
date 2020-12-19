def info(name, surname, year, city, email, phone):
    return f'Личная информация - {surname} {name}, дата рождения {year}, город проживания - {city}, контакты - ' \
           f'тел: {phone}, email - {email}'


user_name = input('Введите свое имя: ')
user_surname = input('Введите свою фамилию: ')
user_city = input('Город проживания: ')
user_year = input('Ваш год рождения в формате дд.мм.гг: ')
user_email = input('Ваша почта: ')
user_phone = input('Ваш телефон в формате 8хххххххххх: ')

print(info(name=user_name, surname=user_surname, phone=user_phone, email=user_email, year=user_year, city=user_city))
