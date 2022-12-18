def search_contact(base, contact):
    base = base.split('\n')
    flag = True
    res = []
    for i in base:
        if contact in i:
            flag = False
            res.append(i)
    if flag:
        res.append(f'Контакт {contact} не найден')
    return res