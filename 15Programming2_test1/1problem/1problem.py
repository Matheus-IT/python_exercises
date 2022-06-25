import sys


ISBN_EOF = '0-00000-000-0'


def is_isbn(code):
    s1 = s2 = 0

    for c in code:
        if not (c.isdigit() or (c == 'X')):
            continue

        d = int(c) if c != 'X' else 10
        s1 += d
        s2 += s1


def main():
    for line in sys.stdin:
        isbn = line.strip(' \n')

        if isbn == ISBN_EOF:
            break

        if is_isbn(isbn):
            print(f'{isbn} está correto.')
        else:
            print(f'{isbn} está incorreto.')


if __name__ == '__main__':
    main()
