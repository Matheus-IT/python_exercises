'''
    PROG II - Segunda Avaliação -

    Integrantes:

    ADALINE NOGUEIRA FERNANDES FIRMO
    THIAGO VINICIOS LIMA DE ARAUJO SOUSA
    MATHEUS DA COSTA DA SILVA

    Questão 01
'''

import sys


class Bag:
    def __init__(self, mindt=0, lilka=0):
        self.mindt = mindt
        self.lilka = lilka

    def get_mindt(self):
        return self.mindt

    def get_lilka(self):
        return self.lilka

    def set_mindt(self, value):
        self.mindt = value

    def set_lilka(self, value):
        self.lilka = value

    def remove(self, choc_t, value):
        if choc_t == 'mindt':
            self.mindt -= value
        elif choc_t == 'lilka':
            self.lilka -= value


class Box:
    def __int__(self, choc_t='', choc_q=-1):
        self.choc_t = choc_t
        self.choc_q = choc_q
        self.is_full = False
        self.box_cap = 0

    def get_cap(self):
        return self.box_cap

    def set_cap(self, value):
        self.box_cap = value

    def get_isFull(self):
        return self.is_full

    def set_isFull(self, value):
        self.is_full = value

    def get_choc_t(self):
        return self.choc_t

    def get_choc_q(self):
        return self.choc_q

    def set_choc_t(self, value):
        self.choc_t = value

    def set_choc_q(self, value):
        self.choc_q = value


def main():
    store = []
    n_boxes = 0
    struct = 1
    bag = Bag()
    check_box = True

    lines = sys.stdin.readlines()

    for l in lines:
        nums = l.split()
        int_nums = list(map(lambda n: int(n), nums))
        if struct > 3:
            struct = 1
        if struct == 1:
            if int_nums[0] == 0 and int_nums[1] == 0:
                break
            bag.set_mindt(int_nums[0])
            bag.set_lilka(int_nums[1])
        if struct == 2:
            n_boxes = int_nums[0]
        if struct == 3:
            index = 0
            while n_boxes > 0:
                box = Box()
                box.set_cap(int_nums[index])
                box.set_choc_t('none')
                box.set_choc_q(0)
                store.append(box)
                index += 1
                n_boxes -= 1
        struct += 1
        if struct == 4:
            for i in store:
                if bag.get_mindt() > 0 and bag.get_mindt() - i.get_cap() >= 0:
                    i.set_choc_t('mindt')
                    i.set_choc_q(i.get_cap())
                    bag.remove(i.get_choc_t(), i.get_choc_q())
                    if i.get_cap() == i.get_choc_q():
                        i.set_isFull(True)

                elif (
                    bag.get_lilka() > 0 and bag.get_lilka() - i.get_cap() >= 0
                ):
                    i.set_choc_t('lilka')
                    i.set_choc_q(i.get_cap())
                    bag.remove(i.get_choc_t(), i.get_choc_q())
                    if i.get_cap() == i.get_choc_q():
                        i.set_isFull(True)
                else:
                    i.set_choc_t('Impossible to distribute')
                    i.set_isFull(False)
            count = 0
            for i in store:
                if i.get_isFull() == False:
                    check_box = False
                if i.get_choc_t() == 'mindt':
                    count += 1
            if check_box == False:
                print('\nImpossible to distribute')
            if check_box == True:
                out = []
                out.append(count)
                for i in store:
                    if i.get_choc_t() == 'mindt':
                        out.append(store.index(i) + 1)
                for i in out:
                    print('{}'.format(i), end=' ')
            store.clear()
            check_box = True


if __name__ == '__main__':
    main()
