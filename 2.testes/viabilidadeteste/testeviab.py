def fluxocalculado(valor, mix):
    fluxo = []
    for pgt in mix:
        vlrpgt = valor*pgt[0]
        parcelas = pgt[1]
        for p in range(parcelas):
            fluxo.append(round(vlrpgt/parcelas, 2))
    return(fluxo)

def somadespesas(clasdespesas, imovel):
    fluxos = []
    fluxofin = []
    for desp in clasdespesas:
        fluxos.append(fluxocalculado(imovel[desp], imovel['Mix Pagamento']))
    for f in fluxos:
        for x in range(len(f)):
            val = f[x]
            if x+1 > len(fluxofin) or len(fluxofin) == 0:
                fluxofin.append(-val)
            else:
                fluxofin[x] =- val
    return(fluxofin)

def somareceitas(clasreceitas, imovel):
    fluxos = []
    fluxofin = []
    for desp in clasreceitas:
        fluxos.append(fluxocalculado(imovel[desp], imovel['Mix Pagamento']))
    for f in fluxos:
        for x in range(len(f)):
            val = f[x]
            if x+1 > len(fluxofin) or len(fluxofin) == 0:
                fluxofin.append(val)
            else:
                fluxofin[x] = val
    return(fluxofin)
            

genova101 = {
    'Vlr Descontado': 410958.8,
    'Perc. Desconto': 0.3,
    'Metragem': 80.1,
    'Mix Pagamento': [(0.2, 1), (0.8, 18)],
    'fluxo': []    
}
genova101['Valor Original'] = genova101['Vlr Descontado'] / genova101['Perc. Desconto']

genova202 = {
    'Vlr Descontado': 437355.10,
    'Perc. Desconto': 0.3,
    'Metragem': 78.85,
    'Mix Pagamento': [(0.2, 1), (0.8, 18)],
    'fluxo': []    
}
genova202['Valor Original'] = genova202['Vlr Descontado'] / genova202['Perc. Desconto']

capri01 = {
    'Vlr Descontado': 500500.00,
    'Perc. Desconto': 0.3,
    'Metragem': 82.28,
    'Mix Pagamento': [(0.2, 1), (0.8, 18)],
    'fluxo': []    
}
capri01['Valor Original'] = capri01['Vlr Descontado'] / capri01['Perc. Desconto']

capri04 = {
    'Vlr Descontado': 500500.00,
    'Perc. Desconto': 0.3,
    'Metragem': 82.28,
    'Mix Pagamento': [(0.2, 1), (0.8, 18)],
    'fluxo': []    
}
capri04['Valor Original'] = capri04['Vlr Descontado'] / capri04['Perc. Desconto']

imoveis = [genova202, genova101, capri01, capri04]

formatovenda = {'Tempo pra venda': 3,
                'Parcelas': 6}

clas_despesas = ['Vlr Descontado',
                 ]

clas_receitas = ['Valor Original',
                 ]

print(somadespesas(clas_despesas, genova101))
print(somareceitas(clas_receitas, genova101))