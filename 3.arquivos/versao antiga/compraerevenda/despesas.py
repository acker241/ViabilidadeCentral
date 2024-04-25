from compraerevenda import formapgt

class SubCategoria:

    def __init__(self, nome=str) -> None:
        self.nome = nome
        pass

subc_MaoDeObra = SubCategoria('Mão de Obra')
subc_Material = SubCategoria('Material')
subc_Servico = SubCategoria('Serviço')
subc_Equipamento = SubCategoria('Equipamento')
subc_Aquisicao = SubCategoria("Aquisição")

class Categoria:

    def __init__(self, nome=str, subc=SubCategoria) -> None:
        self.nome = nome
        self.subc = subc
        pass

class Despesa:

    def __init__(self, nome=str, valor=float, formapgt=formapgt.FormaPagamento, categoria=Categoria, inicio=1, desconto=0.0) -> None:

        assert inicio > 0
        assert desconto >= 0

        self.nome = nome
        self.valor = round(-valor*(1-desconto), 2)
        self.formapgt = formapgt
        self.categoria = categoria
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