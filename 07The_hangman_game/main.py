# -*- coding: utf-8 -*-
from os import system


def random_word():
    from random import randint
    with open('word_bank.txt', 'r') as f:
        bank: list = f.readlines()
    return bank[randint(0, len(bank))-1].strip() #return a random word


def words_match(word_hidden, word):
    for c in range(len(word_hidden)):
        if not(word_hidden[c] == word[c]):
            return False
    return True


class Game():
    def __init__(self):
        self.game_over = False
        self.plays: set = set()
        self.dolls: dict = {'values': [
            '''
            +----+
            |    |
                 |
                 |
                |||
        ==============        
        ''',
            '''
            +----+
            |    |
            O    |
                 |
                |||
        ==============
        ''',
            '''
            +----+
            |    |
            O    |
            |    |
                |||
        ==============
        ''',
            '''
            +----+
            |    |
            O    |
            |\\   |
                |||
        ==============
        ''',
            '''
            +----+
            |    |
            O    |
           /|\\   |
                |||
        ==============
        ''',
            '''
            +----+
            |    |
            O    |
           /|\\   |
           /    |||
        ==============
        ''',
            '''
            +----+
            |    |
            O    |
           /|\\   |
           / \\  |||
        ==============
        ''',
        ], 'index': 0}
        self.current_doll: str = self.dolls['values'][self.dolls['index']]
        self.word: str = ''
        self.word_hidden: list = []
        self.letter: str = ''

    def start_game(self):
        self.game_over = False
        self.plays = set()
        self.dolls['index'] = 0
        self.word = random_word()
        for c in range(len(self.word)):
            self.word_hidden.append('_')
        self.letter = ''

    def show_word_hidden(self):
        for c in range(len(self.word)):
            print(f' {self.word_hidden[c]}', end='')
        print()

    def guess(self):
        at_least_one: bool = False
        for i, l in enumerate(self.word):
            # if there's any letter in the word like the one I chose
            if self.letter == l:
                self.word_hidden[i] = self.letter
                at_least_one = True
        return at_least_one


def main():
    g = Game()
    guess_res: bool = False
    words_match_res: bool = False
    g.start_game()
    while not g.game_over:
        system('cls')
        print(g.current_doll)
        print('The word is', end='')
        g.show_word_hidden()
        g.letter = str(input(' - Digite uma letra: ')).strip()[0]
        while g.letter in g.plays:
            g.letter = str(input(' - Já jogou essa letra! Digite outra letra: ')).strip()[0]
        g.plays.add(g.letter)
        guess_res = g.guess()
        if guess_res:
            print('Acertou!')
        else: # If I miss the guess
            g.dolls['index'] += 1
            g.current_doll = g.dolls['values'][g.dolls['index']]
        words_match_res = words_match(g.word_hidden, g.word)
        if g.dolls['index'] == 6 or words_match_res:
            g.game_over = True
    system('cls')
    print(g.current_doll)
    print(f'The word is {g.word}')
    if words_match_res:
        print('Parabéns você ganhou!!')
    else:
        print('Você perdeu!')
    print('Game over!')


if __name__ == '__main__':
    main()
