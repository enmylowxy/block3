# Декоратор для обработки скидки
def discount(func):
    total_discount = 0
    def wrapper(movie, price, count):
        nonlocal total_discount
        if (count) % 5 == 0:
            discount = float(price)*0.10
            total_discount += discount
            with open('discount.txt', 'w') as f:
                f.write(str(total_discount))
                # f.write(f'{int(total_discount)}\n')
            return func(movie, price, True)
        else:
            return func(movie, price, False)
    return wrapper

@discount
def display_movie(movie, price, has_discount):
    if has_discount:
        print(f'Вы идете на фильм «{movie}» со скидкой')
    else:
        print(f'Вы идете на фильм «{movie}»')


tickets = []
ticket_count =0

with open('tickets.txt', 'r', encoding='utf-8') as file:
    for line in file:
        movie, price = line.rsplit(maxsplit=1)
        tickets.append((movie, int(price)))
        ticket_count += 1
        display_movie(movie, price, ticket_count)

print('Введите фильм и цену или нажмите -е для выхода')

while True:
    answer = input()
    if answer == 'e' or 'е':
        break
    movie, price = answer.rsplit(maxsplit=1)
    price = int(price)
    ticket_count += 1
    display_movie(movie, price, ticket_count)