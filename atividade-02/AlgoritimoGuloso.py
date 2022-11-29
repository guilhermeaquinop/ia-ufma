class AlgoritimoGuloso:

    @staticmethod
    def mochilaFracionaria(c, n, p, v):
        global valor
        valor = 0

        x = [0.0 for i in range(n)]
  
        for j in range(n-1, 0, -1):
            if (p[j] <= c):
                x[j] = 1.0
                c -= p[j]
                valor += v[j]
            else:
                x[j] = round(c / float(p[j]), 3)  
                c = 0
                valor = valor + (v[j] * x[j])
        
        return x

    def getValor(self):
        return valor