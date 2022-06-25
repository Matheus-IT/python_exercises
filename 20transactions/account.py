from datetime import datetime


class Transaction:
    DEPOSIT = 101
    CRD_TRANSFER = 102
    CRD_PIX = 103

    WITHDRAW = -201
    DEB_TRANSFER = -202
    DEB_PIX = -203

    TRANS_NAME = {
        DEPOSIT: 'Depósito',
        CRD_TRANSFER: 'Crédito via tranferência',
        CRD_PIX: 'Crédito via pix',
        WITHDRAW: 'Saque',
        DEB_TRANSFER: 'Débito via transferência',
        DEB_PIX: 'Pagamento via pix'
    }

    def __init__(self, trans_type, value, date=None):
        self.type = trans_type
        self.value = value

        if date is not None:
            self.date = date
        else:
            self.date = datetime.now()

    def __str__(self):
        return Transaction.TRANS_NAME[self.type]


class CurrentAccount:
    def __init__(self, number, name, balance=0.0):
        self._transactions = list()
        self.number = number
        self.name = name
        self.balance = balance

    def register_transaction(self, trans, value, date=None):
        self._transactions.append(Transaction(trans, value, date))

    def deposit(self, value):
        if value < 0:
            return False

        self.balance += value
        self.register_transaction(Transaction.DEPOSIT, value)

        return True

    def withdraw(self, value):
        if value < 0:
            return False

        if self.balance - value < 0:
            return False

        self.balance -= value

        self.register_transaction(Transaction.WITHDRAW, value)

        return True

    def statement(self):
        w = 36
        print('SAMPLE BANK'.center(w))
        print('ACCOUNT STATEMENT'.center(w))
        print('-' * w)
        print('ACCOUNT:', self.number)
        print('NAME:', self.name)
        print('-' * w)
        print('DATE'.ljust(8), 'TRANSACTION'.center(16), 'VALUE'.rjust(10))

        for t in self._transactions:
            date = t.date.strftime('%d/%m/%y')
            trans = '%-17.17s' % str(t)
            value = '%9.2f' % t.value
            print(date, trans, value)


class SavingAccount(CurrentAccount):
    def __init__(self, number, name, mday, balance=0.0):
        super().__init__(number, name, balance)
        self.mday = mday


c = CurrentAccount(12550, 'Matheus Costa', 40)
c.deposit(150)
c.deposit(500)
c.withdraw(250)
c.deposit(350)
c.statement()
