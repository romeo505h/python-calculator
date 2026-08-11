def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def floor_divide(a, b):
    return a // b


def modulus(a, b):
    return a % b


def power(a, b):
    return a ** b


def get_number(message):
    valid = False
    while not valid:
        try:
            number = float(input(message))
            valid = True
            return number
        except ValueError:
            print('Please enter a valid number!')


def get_operator(message):
    valid = False
    while not valid:
        operator = input(message)

        if operator in operations:
            valid = True
            return operator
        else:
            print('Please choose a valid operator.')


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '//': floor_divide,
    '%': modulus,
    '**': power
}

menu = {
    '+': '+ Addition',
    '-': '- Subtraction',
    '*': '* Multiplication',
    '/': '/ Division',
    '**': '** Power',
    '%': '% Modulus',
    '//': '// Floor Division'
}

history = []

continue_calculating = True
while continue_calculating:

    a = get_number('Please enter the first number: ')
    b = get_number('Please enter the second number: ')

    print('*.' * 11)
    print('------Calculator------')
    print('*~' * 11)
    for value in menu.values():
        print(value)
    print('-' * 22)

    operator = get_operator('Choose an operator: ')

    try:
        result = operations[operator](a, b)
        print(result)

        history.append(f'{a} {operator} {b} = {result}')

    except ZeroDivisionError:
        print('Cannot divide by zero. ')
        history.append(f'{a} {operator} {b} = Cannot divide by zero.')

    valid = False
    while not valid:
        ask = input('Would you like to continue? (y/n): ').lower()
        if ask in ('y', 'yes'):
            valid = True
            continue_calculating = True
        elif ask in ('n', 'no'):
            valid = True
            print('-----History-----')
            for calculation in history:
                print(calculation)
            print('Bye.')
            continue_calculating = False
        else:
            print('please enter y/yes or n/no.')
