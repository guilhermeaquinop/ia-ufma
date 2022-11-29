from AlgoritimoGuloso import AlgoritimoGuloso

algoritimoGuloso = AlgoritimoGuloso()

c = 100 #CAPACIDADE MOCHILA
n = 5 #QUANTIDADE DE ITENS A SER SELECIONADO
p = [10, 20, 20, 30, 40] #VETOR DE PESOS DE CADA ITEM
v = [100, 300, 400, 600, 840] #VETOR DE VALORES DE CADA ITEM

x = algoritimoGuloso.mochilaFracionaria(c, n, p, v) #ACIONA O ALGORITMO GULOSO

v.reverse()
p.reverse()
x.reverse()

print("v: " + str(v))
print("p: " + str(p))
print("x: " + str(x))
print("Valor total dos produtos contidos na mochila: ", round(algoritimoGuloso.getValor()))