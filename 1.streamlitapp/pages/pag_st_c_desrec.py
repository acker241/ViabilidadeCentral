import streamlit as st
import json
from streamlit_option_menu import option_menu
from pages.definitions import atributos_padrao

# --- Bloco para funções

#Função teste para limpar dados
def clear_all_text():

    def save_all():
        
        catph = dict(atributos_padrao.categoria_padrao)

        with logoutput:
            st.write('Salvo... ?')
            for v in st.session_state:
                if st.session_state[v] != False and v not in categoriasDeAtributo:
                    st.write(v, st.session_state[v])
                    if v not in dicAttCatDesp:
                        catph[v]['valor'] = st.session_state[v]
                    else:
                        catph['atributosBase'][v] = dicAttCatDesp[v]
    
        catph['tipoRecOuDesp']['valor'] = selecRecOuDesCat
        baseExistenteCat[str(tambase+1)] = catph
        
        json.dump(baseExistenteCat, open(atributos_padrao.basesCategoriasDict[selecRecOuDesCat], mode='w'))
    
    save_all()

    for k in st.session_state:
        if k in categoriaDefault:
            st.session_state[k] = ''
        elif st.session_state[k]:
            st.session_state[k] = False

# --- Bloco para carregar base ---
def carregabase(RecOuDesp, itemOuCat):

    if itemOuCat == 'Cat':
        baseExistente = json.load(open(atributos_padrao.basesCategoriasDict[RecOuDesp]))
    else:
        baseExistente = json.load(open(atributos_padrao.basesFinaisDict[RecOuDesp]))

    return(baseExistente)

# ----------------------


# Bloco para links ---------------------------------------------------------
homelink = 'home.py'

st.page_link('home.py', label='Baby come backs')
st.title('Criação de Receitas e Despesas')

# -- Bloco para definir se quero criar categorias ou as despesas
selecionador = option_menu(
                            menu_title=None,
                           orientation='horizontal',
                           options=['Categorias', 'Itens']
                           )


# Bloco para página Criação de Despesas/Receitas-----------------------------

if selecionador == 'Itens':

    st.header('Criador de Receita/Despesa')
    
    selecRecOuDes = st.selectbox('Receita ou Despesa', ['Receita', 'Despesa'])

    baseExistenteCatPItem = carregabase(selecRecOuDes, 'Cat')

    if len(baseExistenteCatPItem) == 0:
        st.write('Nenhuma categoria registrada!')
    else:
        dicListKeys = baseExistenteCatPItem.keys()
        dicListNomes = []
        for it in baseExistenteCatPItem:
            dicListNomes.append(it+'_'+baseExistenteCatPItem[it]['descricao']['valor'])
        
        catEscolhida = st.selectbox('Categorias existentes para registro', dicListNomes)

        itCamposPreench = baseExistenteCatPItem[catEscolhida[:catEscolhida.find('_')]]

        for itCampo in itCamposPreench:
            itCatEsc = itCamposPreench[itCampo]
            if itCatEsc['visivel']:
                if itCatEsc['agrup']:
                    for x in itCatEsc:
                        subItem = itCatEsc[x]
                        st.write(subItem, x)
                        if subItem is dict and subItem['visivel']:
                            st.write('aaaa')
                            if subItem['agrup']:
                                st.write(subItem, 'tá com errinho ):')
                            else:
                                st.text_input(subItem['nome'])
                    st.text_input(itCatEsc['nome'])
                else:
                    st.text_input(itCatEsc['nome'])

elif selecionador == 'Categorias':
    
    st.header('Criador de Categorias')
    selecRecOuDesCat = st.selectbox('Receita ou Despesa', ['Receita', 'Despesa'])

    baseExistenteCat = carregabase(selecRecOuDesCat, 'Cat')

    tambase = len(baseExistenteCat)
    st.write(tambase, ' categorias existentes!')

    categoriaDefault = atributos_padrao.categoria_padrao
    
    # --- Lista de atributos desconsiderados
    a_desconsiderados = atributos_padrao.attdesconsiderados

    with st.container():
        for k in categoriaDefault:
            if categoriaDefault[k]['visivel'] and k != 'atributosBase':
                st.text_input(categoriaDefault[k]['nome'], key=k)

                #    Estou comentando essa parte pois acho que é um bloco interessante para o editor.
                #    Mas para a criação seria melhor um checkbox e depois eu trago ela, vamos testar.
                #
                #if categoriaDefault[k]['agrup']:
                #    '---'
                #    st.write('Atributos de: ', k)
                #    for k2 in categoriaDefault[k]:
                #        if a_desconsiderados.count(k2) == 0:
                #            st.text_input(k2)

            #Abaixo vai ser um campo onde seleciona-se os atributos base a serem vinculados a uma categoria.

    
    # --- Bloco para Selecionar categorias ---    

    '---'
    st.write('Seletor de Atributos para Categorias')

    categoriasDeAtributo = {}
    dicAttCatDesp = atributos_padrao.padAtributosCatDesp

    for atrPadCatDesp in dicAttCatDesp:
        itemAttCatDesp = dicAttCatDesp[atrPadCatDesp]
        descricaoCat = itemAttCatDesp['atCat']
        if descricaoCat in categoriasDeAtributo:
            categoriasDeAtributo[descricaoCat][atrPadCatDesp] = itemAttCatDesp
        else:
            categoriasDeAtributo[descricaoCat] = {atrPadCatDesp: itemAttCatDesp}

    selAtCol1, selAtCol2 = st.columns(2)

    with selAtCol1:
        st.write('Seletor de Categorias')
        with st.container(height=400):
            for catAtKey in categoriasDeAtributo:
                st.checkbox(catAtKey, key=catAtKey)

    with selAtCol2:
        st.write('Seletor de Atributos')
        with st.container(height=400):
            for catAtKey in categoriasDeAtributo:
                if catAtKey in st.session_state:
                    if st.session_state[catAtKey]:
                        for attFin in categoriasDeAtributo[catAtKey]:
                            st.checkbox(categoriasDeAtributo[catAtKey][attFin]['nome'], key=attFin)

    '---'
    
    logoutput = st.container(height=100)

    #Bloco para colocar em um log o que era selecionado. Não está sendo apagado pq tem um reminder de como estou salvando as variáveis.
    #with logoutput:
    #    for catAtKey in categoriasDeAtributo:
    #        if catAtKey in st.session_state:
    #            if st.session_state[catAtKey]:
    #                for attFin in categoriasDeAtributo[catAtKey]:
    #                    if st.session_state[attFin]:
    #                        st.write(categoriasDeAtributo[catAtKey][attFin]['nome'], ' selecionado!')

        
    enviado = st.button('Salvar Dados', on_click=clear_all_text)

    # ------------------------------------------


    #sintaxe para salvar, ex.

    #ind = str(len(base))
    #base[ind] = nomeVar