from padroes import formapgt

class Receita:

    def __init__(self, nome=str, valor=float, formapgt=formapgt.FormaPagamento, inicio=1, desconto=0.0) -> None:

        assert inicio > 0
        assert desconto >= 0

        self.nome = nome
        self.valor = round(valor*(1-desconto), 2)
        self.formapgt = formapgt
        self.inicio = inicio

        if self.formapgt.mixp == [] and inicio == 1:
            self.fluxo = [self.valor]
        elif self.inicio != 1:
            fluxoinicial = []
            for x in range(inicio-1):
                fluxoinicial.append(0)
            if formapgt.mixp == []:
                fluxoinicial.append(self.valor)
            else:
                for m in formapgt.mixp:
                    fluxoinicial.append(round(m*self.valor, 2))
            self.fluxo = fluxoinicial
        else:
            fluxoinicial = []
            for m in formapgt.mixp:
                fluxoinicial.append(round(m*self.valor, 2))
            self.fluxo = fluxoinicial
            
        pass