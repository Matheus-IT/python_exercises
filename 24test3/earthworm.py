'''
    PROG II - Terceira Avaliação -

    Integrantes:

    ADALINE NOGUEIRA FERNANDES FIRMO
    THIAGO VINICIOS LIMA DE ARAUJO SOUSA
    MATHEUS DA COSTA DA SILVA

    Questão 05
'''


from typing import Dict, List


class EarthwarmField:
    def __init__(self, n_lines, n_columns):
        self.n_of_lines = n_lines
        self.lines_sums: Dict[int, int] = dict()

        self.n_of_columns = n_columns
        self.columns_sums: Dict[int, int] = dict()

    def calc_lines_sums(self, line: List[int], line_number: int):
        '''Accumulate values of lines of cells'''
        self.lines_sums[line_number] = sum(line)

    def calc_columns_sums(self, line: List[int]):
        '''Accumulate values of columns of cells'''
        for i in range(len(line)):
            try:
                self.columns_sums[i] += line[i]
            except KeyError:
                self.columns_sums[i] = line[i]

    def calc_earthwarms_of_greater_line(self):
        '''Returns num of earthwarms of line that has more earthwarms'''
        return max(self.lines_sums.values())

    def calc_earthwarms_of_greater_column(self):
        '''Returns num of earthwarms of column that has more earthwarms'''
        return max(self.columns_sums.values())


def main():
    while True:
        n_of_lines, n_of_columns = list(map(int, input().split()))

        if n_of_lines == n_of_columns == 0:
            break

        field = EarthwarmField(n_of_lines, n_of_columns)

        for i in range(n_of_lines):
            line = list(map(int, input().split()))

            field.calc_lines_sums(line, i)
            field.calc_columns_sums(line)

        greater_line_warms = field.calc_earthwarms_of_greater_line()
        greater_column_warms = field.calc_earthwarms_of_greater_column()

        if greater_line_warms > greater_column_warms:
            print(greater_line_warms)
        else:
            print(greater_column_warms)


if __name__ == '__main__':
    main()
