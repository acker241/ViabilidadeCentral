# Arquivo para definir e separar os padrões que vão ser utilizados em vários momentos
# diferentes do projeto. O intuito é deixar salvo aqui e que outros consultem estes
# modelos para que fiquem dentro do mesmo padrão e poupar tempo caso seja necessário
# fazer alterações na estrutura.

# Bloco para carregar bases -------------------------------------------------------

# ----- Pastas -------
pastaBaseFin = 'pages\\Bases\\'
pastaBaseTemp = pastaBaseFin+'temp\\'

# --- Arquivos ---
# --- Dicionário com as strings para carregar as respectivas bases. ---
dicBase = {
    'Receita': ['receitas.json',
                'cat_receitas.json'],
    'Despesa': ['despesas.json',
                'cat_despesas.json']
}

FinRec = pastaBaseFin+dicBase['Receita'][0]
CatRec = pastaBaseFin+dicBase['Receita'][1]
FinDesp = pastaBaseFin+dicBase['Despesa'][0]
CatDesp = pastaBaseFin+dicBase['Despesa'][1]

basesCategoriasDict = {'Receita': CatRec,
                       'Despesa': CatDesp}

basesFinaisDict = {'Receita': FinRec,
                   'Despesa': FinDesp}

#categoria de Receita ou Despesa
attdesconsiderados = ['agrup', 'visivel']

categoria_padrao = {
    'tipoRecOuDesp': {'nome': 'Tipo da Categoria - Receita ou Despesa',
                      'valor': '',
                      'agrup': False,
                      'visivel': False},
    'indTipoProj': {'nome': 'Índice de Tipo de Projeto',
                    'valor': [], #lista pois pode ter vínculo com vários tipos de proj.
                    'agrup': False,
                    'visivel': False}, 
    'descricao': {'nome': 'Descrição da Categoria',
                'valor': '',
                'agrup': False,
                'visivel': True}, 
    'ativa': {'nome': 'Categoria Ativa',
                'valor':True,
                'agrup': False,
                'visivel': False}, 
    'ccSienge': {'nome': 'Centro de Custo no Sienge',
                'valor': '',
                'agrup': False,
                'visivel': True},
    'classcontabil': {'nome': 'Classificação Contábil no Sienge',
                    'valor': '',
                    'agrup': False,
                    'visivel': True},
    'atributosBase': {
            'agrup': True,
            'visivel': True
            }
    }

#Atributos de despesas/receitas para vincular em categorias

padAtributosCatDesp = {
    'quantia': {'nome': 'Valor atribuido',
                'valor': 0,
                'visivel': True,
                'agrup': False,
                'atCat':'Dados Gerais'},
    'percDesc': {'nome': 'Percentual de Desconto',
                 'visivel': True,
                 'valor': 0.0,
                 'agrup': False,
                'atCat':'Dados Gerais'},
    'fpag': {'nome': 'Fluxo de Pagamento',
                 'visivel': True,
                 'valor': [],
                 'agrup': False,
                'atCat':'Dados Gerais'},
    'carencia': {'nome': 'Carencia do Valor - tempo em Meses para começar',
                 'visivel': True,
                 'valor': 0.0,
                 'agrup': False,
                'atCat':'Dados Gerais'},
    'acresc': {'nome': 'Acréscimo do Valor',
                 'visivel': True,
                 'valor': 0.0,
                 'agrup': False,
                'atCat':'Dados Gerais'},
    'areaTer': {'nome': 'Area do Terreno',
                 'visivel': True,
                 'valor': 0.0,
                 'agrup': False,
                'atCat':'Dados Imóvel'},
    'AreaConstTotal': {'nome': 'Área Construída Total',
                 'visivel': True,
                 'valor': 0.0,
                 'agrup': False,
                'atCat':'Dados Imóvel'},
    'numUndProp': {'nome': 'Número de Unidades - Properties',
                 'visivel': True,
                 'valor': 0,
                 'agrup': False,
                'atCat':'Dados Imóvel'},
    'numVagasGaragem': {'nome': 'Número Total de Vagas de Garagem',
                 'visivel': True,
                 'valor': 0,
                 'agrup': False,
                'atCat':'Dados Imóvel'},
    'numVagasGaragemUnd': {'nome': 'Número de Vagas de Garagem das Unidades',
                 'visivel': True,
                 'valor': 0,
                 'agrup': False,
                'atCat':'Dados Imóvel'},
    'numVagasGaragemAv': {'nome': 'Número de Vagas de Garagem - Avulsas',
                 'visivel': True,
                 'valor': 0,
                 'agrup': False,
                'atCat':'Dados Imóvel'},
    'prazoParaAprovacao': {'nome': 'Prazo para Aprovação do Projeto',
                 'visivel': True,
                 'valor': 0,
                 'agrup': False,
                 'atCat': 'Prazos & Datas Chave'},
    'prazoParaLançamento': {'nome': 'Prazo para Lançamento',
                 'visivel': True,
                 'valor': 0,
                 'agrup': False,
                 'atCat': 'Prazos & Datas Chave'},
    'prazoParaInícioDasObras': {'nome': 'Prazo para início das Obras',
                 'visivel': True,
                 'valor': 0,
                 'agrup': False,
                 'atCat': 'Prazos & Datas Chave'},                 
    'prazoParaConstrução': {'nome': 'Prazo para Construção (Conclusão de Obra)',
                 'visivel': True,
                 'valor': 0,
                 'agrup': False,
                 'atCat': 'Prazos & Datas Chave'},
    'prazoDeRepasseOuSec': {'nome': 'Prazo de Repasse ou Securitização',
                 'visivel': True,
                 'valor': 0,
                 'agrup': False,
                 'atCat': 'Prazos & Datas Chave'},                 
    'canalVendasHouse': {'nome': 'Canal de Vendas - House',
                 'visivel': True,
                 'valor': 0.0,
                 'agrup': False,
                 'atCat': 'Despesas Comerciais'},
    'comissoesHouse': {'nome': 'Comissões - House',
                 'visivel': True,
                 'valor': 0.0,
                 'agrup': False,
                 'atCat': 'Despesas Comerciais'},                 
    'comissoesMercado': {'nome': 'Comissões - Mercado',
                 'visivel': True,
                 'valor': 0.0,
                 'agrup': False,
                 'atCat': 'Despesas Comerciais'},
    'gestaoComShow': {'nome': 'Gestão Comercial + Showroom',
                 'visivel': True,
                 'valor': 0.0,
                 'agrup': False,
                 'atCat': 'Despesas Comerciais'},
    'mktInst': {'nome': 'Marketing Institucional',
                 'visivel': True,
                 'valor': 0.0,
                 'agrup': False,
                 'atCat': 'Despesas Comerciais'},                         
    'mkt': {'nome': 'Canal de Vendas - House',
                 'visivel': True,
                 'valor': 0.0,
                 'agrup': False,
                 'atCat': 'Despesas Comerciais'},
    'txGestInc': {'nome': 'Taxa de Gestão - Incorporador',
                 'visivel': True,
                 'valor': 0.0,
                 'agrup': False,
                 'atCat': 'Despesas de Gestão'},                 
    'geASPEGastosMensais': {'nome': 'G&A (SPE) - Média de Gastos Mensais',
                 'visivel': True,
                 'valor': 0,
                 'agrup': False,
                 'atCat': 'Despesas de Gestão'},
    'inicioSPE': {'nome': 'Data de Início das atividades da SPE',
                 'visivel': True,
                 'valor': 0,
                 'agrup': False,
                 'atCat': 'Despesas de Gestão'},                                  
    'prcMedioUndVenda': {'nome': 'Preço Médio Unidades para Venda',
                 'visivel': True,
                 'valor': 0.0,
                 'agrup': False,
                 'atCat': 'VGV Estimado'},     
}

padAtributosProj = {
    'prAprov': {'nome': 'Prazo para Aprovação',
                'visivel': True,
                'valor': 0,
                'agrup': False},   
}