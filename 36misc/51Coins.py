from datetime import datetime


def calc_exec_time(time):
    '''Returns the execution time in milliseconds'''
    return time.total_seconds() * 1000


def count_how_many(val, el):
    '''Count how many values are there from this element'''
    # count = 0
    # while el >= val:
    #     el -= val
    #     count += 1
    # return count
    return el // val


def main():
    input_values = [1, 72, 0, 10000]

    for i, el in enumerate(input_values):
        print(f'Teste {i+1}')

        fifties = count_how_many(50, el)
        el %= 50
        tens = count_how_many(10, el)
        el %= 10
        fives = count_how_many(5, el)
        el %= 5
        ones = count_how_many(1, el)

        print(fifties, tens, fives, ones)


if __name__ == '__main__':
    start = datetime.now()
    main()
    end = datetime.now()

    print('Execution time: ', calc_exec_time(end - start))
