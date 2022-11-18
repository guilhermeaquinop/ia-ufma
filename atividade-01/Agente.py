import time
from Ambiente import Ambiente
from colorama import init
from termcolor import colored

class Agente(Ambiente):

    def agente(self, ambiente):
        global count, livre, amb
        amb = Ambiente()
        livre = 'O'
        count = 0
        
        for secao in ambiente:
            posAtual = 0

            for i in secao:
                if i != livre and i == 'X':
                    count += 1
                    secao[posAtual] = count
                    amb.exibeAmbiente(ambiente)
                    time.sleep(0.5)
                    secao[posAtual] = livre
                    posAtual += 1
                    
                else:
                    salva = secao[posAtual] 
                    secao[posAtual] = count
                    amb.exibeAmbiente(ambiente)
                    secao[posAtual] = salva 
                    time.sleep(0.5)
                    posAtual += 1
                    continue
        
        return ambiente

    def agenteOrganiza(self, ambiente):
        x = count

        for secao in reversed(ambiente):
            posAtual = (len(ambiente[0]) - 1)

            for i in reversed(secao):
                    if i == livre and x > 0:
                        secao[posAtual] = x
                        amb.exibeAmbiente(ambiente)
                        time.sleep(0.5)
                        secao[posAtual] = 'X'
                        posAtual -= 1
                        x -= 1
                    else:
                        salva = secao[posAtual] 
                        secao[posAtual] = x
                        amb.exibeAmbiente(ambiente)
                        secao[posAtual] = salva 
                        time.sleep(0.5)
                        posAtual -= 1
                        continue 
        
        return ambiente

    def agentePrinta(self):
        init()
        a = count
        print(colored("{} pacientes encontrados e enfileirados".format(a), "white", "on_red"))
    

