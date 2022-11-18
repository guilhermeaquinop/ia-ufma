import time
from Ambiente import Ambiente
from Agente import Agente

amb = Ambiente()
age = Agente()

while True:

    ambiente = [["O","O","O"], 
                ["O","O","O"],
                ["O","O","O"],
                ["O","O","O"]]
    
    ambiente = amb.geraoOcupacoes(ambiente)
    amb.exibeAmbiente(ambiente)
    amb.exibeAmbiente(age.agente(ambiente))
    amb.exibeAmbiente(ambiente)
    amb.exibeAmbiente(age.agenteOrganiza(ambiente))
    age.agentePrinta()
    time.sleep(1)
    break