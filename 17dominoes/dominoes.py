import sys


class DominoGame:
    def load(self, stdin=sys.stdin):
        n = int(stdin.readline())

        if n == 0:
            return False

        self.neighbours = list()

        for _ in range(7):
            self.neighbours.append(list())

        while n > 0:
            n -= 1
            i, j = tuple(map(int, stdin.readline().split()))

            if i > j:
                i, j = j, i

            self.neighbours[i].append(j)
            self.neighbours[j].append(i)

        self.odd_vertices = 0
        for i in range(7):
            if len(self.neighbours[i]) % 2 == 1:
                self.odd_vertices += 1
        return True

    def show(self):
        for i in range(len(self.neighbours)):
            print(f'{i}:', self.neighbours[i])
        print('ODDS', self.odd_vertices)

    def play(self):
        if self.odd_vertices > 2:
            return False

        stack = list()
        visited = [False]*7

        for j in range(7):
            if len(self.neighbours[j]) != 0:
                visited[j] = True
                stack.append(j)
                break

        while stack:
            i = stack.pop()

            for j in self.neighbours[i]:
                if not visited[i]:
                    visited[i] = True
                    stack.append(j)


def main():
    game = DominoGame()

    t = 0

    while game.load():


        if __name__ == '__main__':
            main()
