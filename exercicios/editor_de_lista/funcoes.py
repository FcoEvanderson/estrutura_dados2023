class Funcoes:
    def __init__(self):
        self.itens = []
        self.n = 0

    def get(self, i):
        return self.itens[i]

    def mostrar(self):
        i = 0
        while i < self.n:
            print(self.itens[i], end="")
            i += 1

    def inserir(self, pos, valor):
        if not self.estaVazia():
            if pos == 0:
                self.itens.insert(0,valor)
            elif pos >= self.n:
                self.itens.append(valor)
            else:
                self.itens.insert(pos,valor)
        else:
            self.itens.append(valor)

    def estaVazia(self):
        return self.n == 0

    def remover(self, pos):
        if pos < self.n - 1:
            while pos < self.n - 1:
                self.itens[pos] = self.itens[pos+1]
                pos += 1
        self.n -= 1

    def pesquisar_valor(self, valor):
        if valor in self.itens:
            return self.itens.index(valor)
        return -1

    def pesquisar_posicao(self, pos):
        return self.itens[pos]
