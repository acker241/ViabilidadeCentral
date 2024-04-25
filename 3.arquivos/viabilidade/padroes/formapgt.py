class MixPag:

    def __init__(self, *args):
        self.mix = []
        for v in args:
            self.mix.append(v)
        pass

class FormaPagamento:

    def __init__(self, nome, parcelas, mixp=list):
        
        self.nome = nome
        self.parcelas = parcelas
        self.mixp = mixp
        
        if self.mixp != []:
            if sum(self.mixp) != 1:
                self.mixp = []
                for x in range(self.parcelas):
                    self.mixp.append(1/self.parcelas)
        else:
            for x in range(self.parcelas):
                self.mixp.append(1/self.parcelas)

        pass