print('Welcome to my first Python calculator!')


def get_number(message):
    valid = False
    while not valid:
        try:
            number = float(input(message))
            valid = True
            return number
        except ValueError:
            print('please enter a valid number!')


def calculator(a, b, operator):
    if operator == '*':
        return a * b, None
    elif operator == '/':
        try:
            return a / b, None
        except ZeroDivisionError:
            return None, 'Zero Division Error, please try again. '
    elif operator == '+':
        return a + b, None
    elif operator == '-':
        return a - b, None
    elif operator == '**':
        return a ** b, None
    elif operator == '%':
        try:
            return a % b, None
        except ZeroDivisionError:
            return None, 'Zero Division Error, please try again.'
    elif operator == '//':
        try:
            return a // b, None
        except ZeroDivisionError:
            return None, 'Zero Division Error, please try again.'
    else:
        return None, 'invalid operator, please choose from +, -, *, /, **, %, //.'


continue_calculating = True
while continue_calculating:

    a = get_number('enter the first number: ')
    b = get_number('enter the second number: ')

    result, error = calculator(
        a, b, (input('Choose an operator (+, -, *, /, **, %, //): ')))
    if error is None:
        print(f'Result: {result}')
    else:
        print(error)

    valid = False
    while not valid:
        ask = input('do you still want to continue? (y/n): ').lower()
        if ask in ('y', 'yes'):
            valid = True
            continue_calculating = True
        elif ask in ('n', 'no'):
            valid = True
            print('Goodbye')
            continue_calculating = False
        else:
            print('please enter y/yes or n/no.')
