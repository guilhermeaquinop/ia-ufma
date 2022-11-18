from random import choice

class Ambiente():

    def geraoOcupacoes(self, ambiente): 
        for secao in ambiente:
            atual = 0
            for local in secao: 
                secao[atual] = choice(["X", "O"]) 
                atual += 1
        return ambiente

    def exibeAmbiente(self, ambiente):
        for secao in ambiente:
            print(secao)
        print(2*'\n')