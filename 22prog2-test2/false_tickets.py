'''
    PROG II - Segunda Avaliação -

    Integrantes:

    ADALINE NOGUEIRA FERNANDES FIRMO
    THIAGO VINICIOS LIMA DE ARAUJO SOUSA
    MATHEUS DA COSTA DA SILVA

    Questão 02
'''


from typing import List


class Ticket:
    def __init__(self, val: str):
        self.number = int(val)


class OccurrencesCounter:
    def __init__(self, tickets: List[Ticket]):
        self.tickets = tickets

    def count_occurrences(self):
        occurrences = {}

        for t in self.tickets:
            try:
                occurrences[str(t.number)] += 1
            except KeyError:
                occurrences[str(t.number)] = 1
        return occurrences


def main():
    while True:
        true_tickets, people_present = list(map(int, input().split()))

        if true_tickets == people_present == 0:
            break

        all_tickets = list(map(lambda v: Ticket(v), input().split()))

        counter = OccurrencesCounter(all_tickets)
        occurrences = counter.count_occurrences()

        false_tickets = 0
        for v in occurrences.values():
            if v > 1:
                false_tickets += 1

        print(false_tickets)


if __name__ == '__main__':
    main()
