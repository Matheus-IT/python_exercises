class Grafo:
    def __init__(self):
        self.lista = {}
        self.n = None
        self.m = None

    def mostrar_grafo(self):
        print("\nVetor de Adjacência: ")
        for v in self.lista:
            print(f"{v}: ", end="")
            for k in self.lista[v]:
                print(f"{k} ", end="")
            print()

    def gerar_digrafo(self, lines):
        self.n = int(lines[0].split()[0])
        self.m = int(lines[0].split()[1])
        for v in range(self.n):
            self.lista[v] = []
        i = 1
        while i <= self.m:
            u = int(lines[i].split()[0])
            v = int(lines[i].split()[1])
            p = int(lines[i].split()[2])
            self.lista[u].append((v, p))
            i += 1

    def dijkstra(self, raiz):
        d = [9999 for i in range(self.n)]
        pai = [-1 for i in range(self.n)]
        aberto = [True for i in range(self.n)]
        d[raiz], pai[raiz] = 0, raiz
        menor = raiz
        while True in aberto:
            for k in self.lista.keys():
                print("d[menor]", d[menor])
                if aberto[k] and d[k] < d[menor]:
                    menor = k
            aberto[menor] = False
            for tupla in self.lista[menor]:
                if d[tupla[0]] > d[menor] + tupla[1]:
                    d[tupla[0]] = d[menor] + tupla[1]
                    pai[tupla[0]] = menor
            if menor == raiz:
                menor = self.lista[menor][0][0]
            print()
            print(d)
            print(aberto)
            print(pai)


def main():
    grafo = Grafo()
    lines = list()
    with open("34Graphs/in5.txt", "r") as file:
        lines = [line.strip() for line in file if line.strip()]
        file.close()
    grafo.gerar_digrafo(lines)
    grafo.mostrar_grafo()
    input("Tecle ENTER para continuar...")
    print("Para sair, tecle apenas ENTER")
    raiz = int(input("Informe a raiz...: "))
    if raiz in grafo.lista.keys():
        grafo.dijkstra(raiz)
    input("Tecle ENTER para continuar...")


if __name__ == "__main__":
    main()
