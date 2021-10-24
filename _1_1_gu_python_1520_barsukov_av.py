# Найти сумму и произведение цифр введённого пользователем трёхзначного числа.

message_1 = 'Введите без пробелов целое трёхзначное положительное число. \n' \
          'Для завершения программы вместо числа введите команду "stop" без кавычек: '
message_2 = 'Ошибка формата ввода! Введено некорректное значение:'
number = ''

# Проверка корректности ввода
test = 0  # Вспомогательная переменная корректности ввода
while number != 'stop' and test != 1:
    number = input(message_1)
    if number != 'stop':
        try:
            number = int(number)
            if number < 100 or number > 999:  # Проверка нахождения числа в нужном диапазоне
                test = 0
                print(f'{message_2} "{number}"')
            else:
                test = 1
        except ValueError:
            print(f'{message_2} "{number}"')

# Обработка введённого числа
if number != 'stop':
    number = [int(x) for x in str(number)]
    number_amount = 0
    for x in number:
        number_amount = number_amount + x
    print(f'Сумма цифр введённого числа: {number_amount}')
    number_multi = 1
    for x in number:
        number_multi = number_multi * x
    print(f'Произведение цифр введённого числа: {number_multi}')
    print('Программа завершена успешно!')

if number == 'stop':
    print('Программа остановлена пользователем!')
