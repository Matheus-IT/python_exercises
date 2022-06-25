class str(str):
    def isfloat(self):
        try:
            float(self)
            return True
        except ValueError:
            return False


def convert(n_formatted: str, thousands_sep, decimals_sep) -> str:
    thousands, decimals = n_formatted.split('.')
    thousands = thousands.replace(',', thousands_sep)
    return decimals_sep.join((thousands, decimals))


def format_to_number(input_val: str,
                     n_decimals=2,
                     thousands_sep='.',
                     decimals_sep=',') -> str:

    n_formatted = f'{float(input_val):,.{n_decimals}f}'
    return convert(n_formatted, thousands_sep, decimals_sep)


def main():
    while True:
        # input_val = str(input('Enter a real number: '))
        input_val = str('1500')

        if input_val.isnumeric() or input_val.isfloat():
            break
        print('Invalid number, try again...')

    formatted = format_to_number(input_val)
    print(f'Result: {formatted}')


if __name__ == '__main__':
    main()
