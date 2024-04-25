
"""

17/04/2024 - Criação de escopo inicial de projeto. Conforme abaixo.
    Preciso agora elencar quais desafios para iniciar. Caminho crítico para o projeto.
18/04/2024 - Objetivo é detalhar um cronograma das ações e delimitar o caminho crítico do projeto.
    Caminho crítico já criado. Salvo como arquivo Excel na pasta.
    Vou descrever o racional da definição de dados e bases no final do documento ponto 2)
19/042024 - Não consegui avançar muito ontem mas hoje pretendo ter algumas ferramentas mais avançadas neste aspecto.
    Meta de hoje é fazer o criador de despesas/receitas.
    Necessidades:
        - Base de categorias para receitas/despesas
        - Base das receitas e outra para despesas

    
1) Dashboard para visualização do meu trabalho na Halsten

    Premissas iniciais nesta fase do projeto - abr/2024
        
        Simplicidade.

            É um projeto super ousado para as minhas capacidades no momento. É um projeto de ERP,
            precário, mas um ERP. E o pior é que pode ser relativamente desnecessário.
            No entanto preciso de uma ferramenta de gestão, fora do Excel, para facilitar a informação de resultados e
            controle do resultado alcançado/projetado.
            Neste momento tenho que simplificar o máximo minha vida tentando fazer um conceito mais alcançável
            dentro das minhas habilidades.
            Isso significa:
                - Streamlit como interface do ERP para criação/visualização dos projetos
                - JSON/Base local para um projeto de database. O projeto vingando e virando um negócio sério para a empresa,
                este ponto vai ser a primeira coisa a melhorar. Como será a gestão de várias pessoas acessando ao mesmo tempo, por ex.
                - Neste momento, não ter controle de usuários ou ter um controle bem precário
        
        Funcional

            As páginas/apps criados tem que ter somente os campos/valores que eu utilizo nas análises e no dia-a-dia.
            Todo dado não utilizado é lixo. Se houver a necessidade da informação, tanto na concepção do produto ou na visualização,
            ela tem que ser usada.     
            

    Etapas a fazer do projeto:
    
    a) Ferramenta para criação, edição e visualização dos projetos de Novos Negócios

        Primeiro produto a ser criado. Se foi útil para mim pode ser útil para outra área e talvez para toda empresa.    
    
        a) Criação

            a) Eu ter categorias de produto para criação.

                Por ex. Quando eu for começar a considerar um imóvel para leilão eu já carregar que tem:
                ITBI, comissão leiloeiro, custas de desocupação, custas de cartório, juros financeiros...

            b) Criação/edição de receitas e despesas.

                Quando eu falo de criação de receitas e despesas, não é o vínculo de uma receita (ou tipo de receita), 
                já existente, ao projeto, mas sim a criação de uma nova despesa durante o racional do projeto.
                Por ex. estou fazendo a viabilidade de um loteamento em uma área em Joinville. Após a aprovação,
                durante a diligência foi levantado um problema ambiental, ocasionando uma nova despesa no projeto.

                Para o armazenamento destas despesas, eu imagino que o ideal seria eu ter uma base de receita,
                outra de despesa. Cada item em cada base tem seu índice único e quando eu for criar a viabilidade
                eu vinculo esses índices de despesa e receita ao projeto.

                Mas como eu armazeno o valor da despesa naquele projeto?
                Eu tenho algumas alternativas na minha cabeça para este problema:

                    a) Eu tenho a base de receita e salvo dentro do projeto o link com a base de receita, mas o valor eu salvo
                    no índice da base do projeto.
                        Analisando essa hipótese não acho que seja a mais viável a longo prazo.
                        Problemas já levantados:
                            Se eu quiser consultar todas as receitas da categoria, teria que consultar todos os projetos.
                            Não faz muito sentido.

                    b) Eu tenho a base de projeto, a base do tipo de receita e a base das receitas vinculadas.
                        Na concepção de um projeto, quando eu o salvo:
                            Na base do projeto: um projeto novo, com os índices das receitas vinculadas.
                            Na base de receitas vinculadas: cada indice tem seu valor, com um vínculo para consulta
                            de receitas, tipos e categorias na base de receita (base ou sei lá outro nome).
                            Na base de receitas: eu só altero quando eu crio uma receita, ou tipo novo. Essa base
                            fica praticamente como base de consulta para quando eu quiser vincular um valor a um projeto.
                        O problema é que eu vou ficar alimentando um monte de bases ao mesmo tempo. Sei lá, pode ser uma complexidade
                        desnecessária. Por enquanto é a melhor solução que eu encontrei.

                    c) Eu posso ter uma tag de receita, dentro da base, como raiz.
                        Quando eu for criar uma receita vinculada a um projeto eu buscaria dentro base as receitas RAIZ.
                        E quando eu for salvar um valor eu craria um novo lançamento, semelhante a opção b) anterior, 
                        na mesma base de receita. Assim eu teria 3 bases, projetos receitas e despesas.
                        O principal problema é sanitização destes dados. Eu vou ter categorias/tipos de receitas/despesas
                        dentro da mesma base. Com o tag talvez não seja tão problemático, mas pode ocasionar em pepinos.

                E se eu quiser repetir a mesma despesa?
                Por ex. Eu mobilio um cômodo, numa reforma. E agora eu quero mobiliar outro, mas quero armazenar com
                outro nome e valor.
            
            c) Vínculo de receitas e despesas.

                Por ex. A comissão é um percentual do valor de venda total. Eu posso querer também ter uma despesa
                a cada 1000 m² por ex. 
                Então eu preciso ter alguma configuração para que eu insira os parâmetros para cálculo o programa
                cuide do resto. No conceito, até o momento, eu vincularia as receitas/despesas novas a outras movimentações
                já registradas na base.
                
                Esse tipo de vínculo precisa ser pensado com cuidado. O principal desafio que eu vejo é:
                Quando eu atualizo estes valores? Pois vou salvar em uma base relativamente estática. Então:
                Quando eu faço a verificação de alteração destes valores?
                Quando eu altero esses valores?
                Em qual base eu faço consulta?
                Quando eu falo de IR após lucro, eu calculo somente após todas as receitas/despesas serem processadas. Como
                vou fazer isso? Talvez criar uma categoria de receitas/despesas que seja calculado diferente (somente no fluxo)?
                Juros financeiros ocorrendo via exposição de caixa entraria nesse critério.
                O vínculo de despesa financeira também seria talvez uma opção a parte. Dentro da viabilidade do Poffo é um boolean
                onde consulta se é alavancado ou não e considera o custo financeiro do projeto.
            
            d) Vínculo de tags/categorias ao projeto.
            
            e) Vínculo de documentos externos/links ao projeto.

            f) Vínculo de centro de custo do Sienge, caso o projeto seja aprovado.

            g) Status de aprovação do projeto (Desenvolvimento, em aprovação, aprovado, reprovado)

            h) Status de execução do projeto - eu posso ter um projeto aprovado porém eu vou executar e colocar ele
            em andamento em um segundo momento.

            i) Histórico de tarefas e execução de cada projeto.
                Cada projeto desencadeia em uma série de afazeres. Como vamos controlar isto dentro da ferramenta?
                Poderia também vincular usuários a cada etapa.
            
            j) Possibilidade de ter uma hierarquia de projetos
                Eu teria uma unidade de negócio com custos por ex. um mega condomínio em que eu separe as unidades comerciais
                das residenciais e/ou prédio de casas.
            
            k) Ferramenta para importação de projetos via csv ou json

            l) Criar histórico de versões de projeto

            m) 


        b) Edição

            Ferramenta para fácil (?) edição de projetos onde o usuário teria permissão para editar.
            Pode ser que seja limitado quais valores possa editar. Por ex. será que permito editar o lucro diretamente?
            Sendo campo calculado e não valor, já que vou salvá-lo diretamente na base? Tem algumas decisões que precisariam
            ser tomadas nesta etapa.

            a) Seletor de projetos existentes com base na permissão de nível de usuário.

            b) Dentro do seletor, permissão somente de certas receitas/despesas a serem editadas pelo usuário.

            c) Diferenciar talvez as janelas de premissas de viabilidade para tarefas/workflow do projeto.
                O workflow não vai ser diretriz para perfomance... ou vai. Se depender das metas (atingimento nas datas)

            d)

        c) Visualização

            a) Ter como base para apresentação o layout já aprovado pelo Neuton - OnePage com informações resumidas.
                Com base na categoria do projeto pode ser que eu tenha que ter vários layouts diferentes para visualização.
                Será que eu consigo fazer um editor de layouts dentro do app?

            b) Também incrementar com o modelo já criado pelo Poffo. Implementar as visualizações/indicadores
            de resultado já existentes.

            c) Entrar no detalhe de receitas/despesas: agrupador de categorias para eu poder comparar projetos.
                Dentro deste detalhamento, criar uma categoria de projetado/executado, pegando o executado do Sienge

            d) Tela/relatório para eu comparar retornos/receitas/despesas de diferentes projetos e/ou projetos
            da mesma categoria de projeto. Ex.
                Comparar unidade de leilão com Biarritz
                Comparar Biarritz com Costa Club.

            e) Resumo de performance da área/setor e também por empresa.
                Dentro deste escopo posso talvez abrir um resumo por área/empresa e depois abrir por projeto.
                Dentro construir a hierarquia dentro do projeto para poder vincular cada empresa/área

            f) Filtrar todos os resultados por data, período.
                Dentro deste filtro de data considerar datas de início, conclusão, 
                movimentação financeira (receita/despesa incorrida)
                Dentro desta visualização, criar possibilidade de agrupar resultados por períodos
                (meses, trimestres, semestres, anos)

            e) Algum relatório para auditoria
                Ter algum formato contábil para auditoria/conferência destes lançamentos e conferência dos valores
            
            f) Criar alguma ferramenta em que o software gere relatórios a cada n período.
                Dependendo do projeto, sendo crítico ou não, eu possa ter uma flag no projeto ou na visualização dele
                para que eu mande para uma lista de pessoas e/ou lideranças informações referentes ao projeto.
                Eu posso até configurar para que mande certas informações do projeto somente para algumas e não para outras.

            g) Criação de fluxo de caixas e movimentações para relatórios diários ou gestão externa

            h) Seletor de variável para cálculo de viabilidade - matriz sensibilidade

            i)

2) Definição de diretrizes e bases para armazenamento de dados do projeto.

    2.a) Conceitos Gerais

        2.a.a) Definição de base de dados.
            
            Pelo que eu imagino nesta etapa do projeto eu vou trabalhar com JSON em todas as bases e
            já que vou trabalhar neste formato o tipo ideal para importar e exportar seria usando
            dicts por todo tipo de dado.

            - JSON + dicts

        2.a.b) Estrutura de Pastas

            - última alteração na estrutura - 2024-04-18
            - alteração da estrutura - 2024-04-19 - não funciona pra função de pages do Streamlit.

            > Raiz
                - home.py
                > pages
                    pag_st_c_projeto.py
                    pag_st_c_desrec.py
                    pag_st_c_visual.py
                    pag_st_ed_projeto.py
                    pag_st_ed_desrec.py
                    pag_st_ed_visual.py
                    > Criação
                        > Projetos                      
                        > DespesasReceitas
                        > Visualização (Relatórios) - 2ª Etapa      
                    > Edição 
                        > Projetos 
                        > DespesasReceitas                  
                        > Visualização (Relatórios) - 2ª Etapa                     
                    > ClassDefinitions
                        Pasta para declarar algumas classes que vão ser utilizadas ao longo do projeto
                    > Bases
                        - projetos.json
                        - despesas.json
                        - receitas.json
                        - relatórios.json
                        > temp
                            imagino que tenha criar algo temporário para armazenar algo enquanto editam a pág.
                            - projetos_temp.json
                            - despesas_temp.json
                            - receitas_temp.json
                            - relatórios_temp.json

    2.b) Receitas/Despesas

        2.b.a) Conceito da base de dados

            Conforme o racional acima, segue primeira versão do que seria o dict de uma receita/despesa

            declaração

            --------------------------------------------------------------------------------------

            nomeVar = {
            'indCat' = 0, #int
            'indProj' = 0, #int
            'descricao' = '', #str
            'ativa' = True, #Boolean

            'receitaVinc' = False, #Boolean
            'indReceitaVinc' = 0, #int
            'proporReceitaVinc' = 0.00, #float
            'despesaVinc' = False, #Boolean
            'indDespesaVinc' = 0, #int
            'proporDespVinc' = 0.0, #float

            'valor' = 0.00, #float
            'percDesc' = 0.0 #float
            'fpag' = [], #lista
            'carencia' = 0, #int

            }

            #sintaxe para salvar, ex.

            ind = str(len(base))
            base[ind] = nomeVar

            --------------------------------------------------------------------------------------

            Explicação de Keys do dict

            ind = índice da base de dados - sempre vou buscar o maior indice da base e acrescentar um.

            indcat = índice relacionado ao tipo de despesa/receita cadastrado.
            indproj = índice relacionado ao projeto em que a receita/despesa está vinculada
            descricao = descritivo da receita/despesa, com base no campo no software
            ativa = Ao invés de eu apagar todo o log de despesas/receitas eu vou colocar ativa ou não.

            'receitaVinc' = False, #Boolean
            'indReceitaVinc' = 0, #int
            'proporReceitaVinc' = 0.00, #float
            Bloco para vincular a despesa/receita a uma receita já registrada.
            ReceitaVinc é a boolean onde salva se tem vinculo ou não. Setando isso no app abre a opção de preencher os outros campos.

            'despesaVinc' = False, #Boolean
            'indDespesaVinc' = 0, #int
            'proporDespVinc' = 0.0, #float
            Bloco para vincular a despesa/receita a uma receita já registrada.
            DespesaVinc é a boolean onde salva se tem vinculo ou não. Setando isso no app abre a opção de preencher os outros campos.

            valor = valor sem descontos da receita/despesa. seria o valor total para preenchimento
            percDesc = campo para preencher se há um desconto. Deixo o campo para preencher em % ou em float?
            fpag = uma lista com várias tuples para fazer o fluxo de caixa.
                Ex. - [(0.2, 1), (0.5, 10)]
                    (0.2, 1) - 20% na entrada em 1x
                    (0.5, 10) - 50% em 10 vezes, após entrada.
                    Ainda falta 30% então a função de fluxo vai acrescentar uma parcela de 30% no final.
                    Se passar de 100% tem que apresentar erro na hora de salvar e voltar para o cliente alterar.
            carencia = dado para quanto tempo vou colocar sem valor no fluxo. Pode ser tanto para receita para despesa.
                Tem valores que iniciam somente após x meses.
        
    2.c) Projeto

        2.c.a) Conceito da base de dados

            Declaração

            --------------------------------------------------------------------------------------

            nomeVar = {
            
            'tags' = [], #list
            'categoria' = '', #string
            'descricao' = '', #string
            'recvinculadas' = [], #list
            'despvinculadas' = [], #list
            'inicioVenda' = '', #data ou integer? Posso pedir para colocar uma data específica.
            'inicioProjeto' = '', #data - hoje como sugestão
            'valorVendaGeral' = 0.0, #float
            'percDesc' = 0.0, #float
            'taxaFin' = 0.0, #float


            'dadosEspecificos' = {}, #dict

            }
            
            #sintaxe para salvar, ex.

            ind = str(len(base))
            base[ind] = nomeVar

            --------------------------------------------------------------------------------------

            ind = índice da base de dados - sempre vou buscar o maior indice da base e acrescentar um.
            categoria = 
            descricao
            recvinculadas = lista de índices dentro da base de receitas com as receitas vinculadas no projeto
            despvinculadas = lista de índices dentro da base de despesas com as despesas vinculadas no projeto
            
            
            dadosEspecificos = nome placeholder. Estou pensando que vão ter projetos e templates onde eu vou ter mais informações para fazer a viabilidade
                Ex. Construção - terei m² total, m² privativos, CUB, etc... Alguns projetos vão compartilhar algumas informações em comum e outros não.
                
    2.d) Categorias de Receitas e Despesas

        Preciso de uma base para criação e parametrização de categorias de receitas e despesas.
        Tem alguns dados que eu posso alterar aqui que fica melhor a manutenção de todo log de receitas e depesas ao longo prazo.

            --------------------------------------------------------------------------------------

            nomeVar = {
            'indTipoProj' = [], #list
            'descricao' = '', #str
            'ativa' = True, #Boolean

            'atributosBase' = {
                'valor' = 0.00, #float
                'percDesc' = 0.0 #float
                'fpag' = [], #lista
                'carencia' = 0, #int
                }

            'ccSienge' = '', #str
            'classcontabil = '', #str
            }

            #sintaxe para salvar, ex.

            ind = str(len(base))
            base[ind] = nomeVar

            indTipoProj = Lista com os tipos de projeto em que a despesa é permitida ou já importada.
            descricao = descricao do tipo de despesa
            ativa = se tiver ativa puxa da base
            atributosBase = dicionario padrão para carregar alguns valores para algumas categorias. Talvez deixe uns campos
                livres para preencher e colocar uns atributos a mais.
            ccsienge = campo placeholder para implementação de conferência para centro de custo do Sienge
            classcontabil = campo placeholder para implementação de um vínculo contábil para a receita/despesa
"""