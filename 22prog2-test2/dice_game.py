'''
    PROG II - Segunda Avaliação -

    Integrantes:

    ADALINE NOGUEIRA FERNANDES FIRMO
    THIAGO VINICIOS LIMA DE ARAUJO SOUSA
    MATHEUS DA COSTA DA SILVA

    Questão 04
'''


from typing import List

TRAP_REPR = 'x'  # Representation of a trap


class Player:
    def __init__(self, player_id: int):
        self.player_id = player_id
        self.current_spot = 0
        self.can_play = True
        self.was_trapped_last_time = False


class NonePlayer:
    '''Representation of the absence of a player'''

    def __init__(self):
        self.player_id = -1
        self.current_spot = -1
        self.can_play = False
        self.was_trapped_last_time = False


class Game:
    def __init__(self, players: List[Player], trail: List[str]):
        self.players = players
        self.trail = trail
        self.current_player = players[0]

    def _passed_the_trail(self, player):
        return player.current_spot > len(self.trail)

    def move_player(self, steps_to_move: int):
        self.current_player.current_spot += steps_to_move

    def _is_the_last_player(self, player: Player):
        '''Returns if a given player is the last one'''
        return player.player_id == len(self.players)

    def _get_next_player(self):
        if self._is_the_last_player(self.current_player):
            return self.players[0]  # Go back to the beginning
        return self.players[self.current_player.player_id]

    def determine_next_player(self):
        '''Set the next player available to be the current player'''
        while True:
            self.current_player = self._get_next_player()

            if (
                self.current_player.can_play
                or self.current_player.was_trapped_last_time
            ):
                break

    def _is_in_a_trap(self, player: Player):
        spot = player.current_spot
        if spot == 0:  # Still in the starting point
            return False
        return self.trail[spot - 1] == TRAP_REPR

    def determine_can_play(self, player: Player):
        if self._is_in_a_trap(player) and player.was_trapped_last_time:
            player.can_play = True
            player.was_trapped_last_time = False
        elif self._is_in_a_trap(player):
            player.can_play = False
        else:
            player.can_play = True


def count_steps(d1, d2):
    '''Count the steps to move the player based on the dice numbers'''
    return d1 + d2


def create_players(num_of_players: int):
    return [Player(i + 1) for i in range(num_of_players)]


def create_trail(length: int, traps: List[int]):
    trail = [str(i + 1) for i in range(length)]

    trail[traps[0] - 1] = TRAP_REPR
    trail[traps[1] - 1] = TRAP_REPR
    trail[traps[2] - 1] = TRAP_REPR
    return trail


def main():
    while True:
        num_of_players, trail_length = list(map(int, input().split()))

        if num_of_players == 0 and trail_length == 0:
            break

        trap1, trap2, trap3 = list(map(int, input().split()))

        players = create_players(num_of_players)
        trail = create_trail(trail_length, [trap1, trap2, trap3])

        game = Game(players, trail)

        dice_rolls = int(input())
        times_rolled_dice = 0

        winner = NonePlayer()

        while times_rolled_dice < dice_rolls:
            game.determine_can_play(game.current_player)

            if game.current_player.can_play:
                die1, die2 = list(map(int, input().split()))
                times_rolled_dice += 1

                steps_to_move = count_steps(die1, die2)

                game.move_player(steps_to_move)

                if game._passed_the_trail(game.current_player):
                    winner = game.current_player
                    break
            else:
                game.current_player.was_trapped_last_time = True

            game.determine_next_player()

        print(winner.player_id)


if __name__ == '__main__':
    main()
