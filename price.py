def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    one_with_two = one + delimiter + two
        
    return one_with_two

print(get_summ(1 , 2))


def get_summ(learn, python):
    learn_python = learn + ' ' + python

    return learn_python

print(get_summ('learn'.capitalize(), 'python'))


def format_price(price):
    price = int(price)
    total_price = f'Цена: {price} руб.'

    return total_price

print(format_price(56.24))