#fazer um template de compra e venda de mobiliado - costa 404
import despesas as dsp
from despesas import Despesa
from despesas import Categoria
from formapgt import FormaPagamento
from formapgt import MixPag
from receitas import Receita


pgt6x = FormaPagamento('6x', 6, MixPag())
catRef = Categoria('Reforma', dsp.subc_Servico)
catMaterial = Categoria('Reforma', dsp.subc_Material)

desp = []
rcta = []

costa404 = [desp, rcta]

projeto = Despesa('Versus Arquitetura', 7000, pgt6x, Categoria('Projeto e Acompanhamento', dsp.subc_Servico))
box = Despesa('Box Banheiro', 4000, pgt6x, catRef)
pintura = Despesa('Pintura', 5000, pgt6x, catRef)
marcenaria = Despesa('Marcenaria', 20000, pgt6x, catRef)
vinilico = Despesa('Vinílico', 7000, pgt6x, catRef)
limpeza = Despesa("Limpeza", 200, pgt6x, catRef)
aquisicao = Despesa("Aquisição Unidade 404", 472000, pgt6x, Categoria("Aquisição", dsp.subc_Aquisicao))

desp.append(projeto)
desp.append(box)
desp.append(pintura)
desp.append(marcenaria)
desp.append(vinilico)
desp.append(limpeza)
desp.append(aquisicao)

rcta.append(Receita('Venda', 590000, pgt6x, 2))

def montafluxo(receitas=list, despesas=list):

    def adicionareceitas(receitas, fluxo):

        for rec in receitas:
            fluxoreceita = list(rec.fluxo)
            for x in range(len(fluxo)):
                valor = fluxo[x]
                if len(fluxoreceita) > 0:
                    fluxo[x] = round(valor + fluxoreceita.pop(0), 2)
            if len(fluxoreceita) > 0:
                for rec in fluxoreceita:
                    fluxo.append(rec)

        return(fluxo)
    
    def adicionadespesas(despesas, fluxo):

        for desp in despesas:
            fluxodespesas = list(desp.fluxo)
            for x in range(len(fluxo)):
                valor = fluxo[x]
                if len(fluxodespesas) > 0:
                    fluxo[x] = round(fluxodespesas.pop(0) + valor, 2)
            if len(fluxodespesas) > 0:
                for desp in fluxodespesas:
                    fluxo.append(desp)

        return(fluxo)
    
    if len(despesas) == 0 and len(receitas) != 0:
        fluxoin = list(receitas[0].fluxo)
        receitas.pop(0)
    elif len(receitas) == 0 and len(despesas) != 0:
        fluxoin = list(despesas[0].fluxo)
        despesas.pop(0)
    elif len(receitas) == 0 and len(despesas) == 0:
        return([])
    else:
        fluxoin = list(despesas[0].fluxo)
        despesas.pop(0)
    
    fluxofinal = adicionadespesas(despesas, adicionareceitas(receitas, fluxoin))

    return(fluxofinal)

print(montafluxo(rcta, desp))
#variáveis
#valor mercado da unidade = 590000 - ok
#Desconto na compra - 20% - ok
#Prazo de devolução (pagamento a Halsten) - 6 meses - ok
#Pagamento da devolução - Parcelado, à Vista, na Venda - ok
#Valor da Venda (receita) = 590000 ok
#Prazo para venda - 1 mês - ok
#Forma de pgt - venda - ok
#% corretagem na venda - ok
#% impostos na venda - ok
#Prazo para início da obra - 1 mes
#Tx Juros
#