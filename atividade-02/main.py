Classe BagObject():
    def __init__(proprio, peso, valor, indice):
        auto.indice = indice
        auto.peso = peso
        auto.valor = valor
        self.report = valor // peso
  #Função para comparação entre must BagObjects
  #Comparamos a proporção para classificá-los
    def __lt__ (próprio, outro):
        return auto.relatório < outro.relatório


def getMaxValue(peso, valores, capacidade):
        arraySort = []
        for i in range(len (peso)):
            arraySort. append(BagObject(peso[i], valores[i], i))

        # Classific os elementos da sacola por seu relatório
        arraySort.sort(reverse=True)

        valorContador = 0
        for objeto em arraySort:
            pesoatual = int(objeto.peso)
            valoratual = int(objeto. valor)
            se capacidade - peso atual >= 0:
                # adicionamos o objeto no saco
                # Nossos subtraímos a capacidade
                capacidade - = peso atual
                ValorContador += ValorAtual
                # Nossos adicionais o valor no saco
            mais longe:
                rendimento = capacidade / peso atual
                counterValue + = currentValue * inglês
                capacitância = int (capacitância - (peso atual * receita))
                intervalo
        return counterValue


peso = [1,5,3,2,4]
valores = [10,50,20,30,60]
capacitância = 11
maxValue = getMaxValue (peso, valores, capacidade)
print("Valor máximo na mochila=", maxValue)