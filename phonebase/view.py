def contact_to_s():
    return input('Введите инфо для поиска: ')

def choose_mode():
    return input('Введите команду (1 - добавление, 2 - поиск): ')

def new_contact():
    name = input('Введите имя: ')
    phone_num = input('Введите номер телефона: ')
    return f'{name}  // {phone_num}'

def show_found(res):
    print('Результат поиска: ')
    for i in res:
        print(i)