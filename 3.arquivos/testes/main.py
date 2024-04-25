import streamlit as st
import json


st.write('Pagina de testes')

dados = []

with st.form('form teste', clear_on_submit=True):
    var1 = st.text_input('Variavel 1')
    var2 = st.text_input('Variável 2')

    botao = st.form_submit_button('salvar variáveis')

    if botao:
        dados.append(str(var1))
        dados.append(str(var2))
        st.write('Dados Salvos')
        st.write(dados)

botaoapagar = st.button('Apagar dados Salvos')

if botaoapagar:
    json.dump([], open('dados.json', mode='w'))
try:
    dadosfora = json.load(open('dados.json'))
    for d in dados:
        dadosfora.append(d)
    st.write(dadosfora)
    json.dump(dadosfora, open('dados.json', mode='w'))
except:
    json.dump(dados, open('dados.json', mode='w'))
    st.write(dados)

var3 = st.text_input('Variável 3')
var4 = st.text_input('Variável 4')
var5 = st.number_input('Variável 5', 1, step=1)

st.write('Variáveis', var3, var4, var5)