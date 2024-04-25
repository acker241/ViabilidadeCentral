import streamlit as st
import json

st.page_link('pages/ed_viab.py', label='Editor de Viabilidades')
#st.page_link('pages/vis_viab.py', 'Vizualiador de Viabilidades')
st.page_link('home.py', label='Página Inicial')

st.title('Página para ter acesso as viabilidades que já existen')

col1, col2 = st.columns(2)

with col1:
    try:
        viabilidades_salvas = json.load(open('viabilidades_salvas.json'))
        seletor_viab = st.selectbox('Viabilidades Salvas', sorted(viabilidades_salvas))

        st.write('Carregando: ',seletor_viab)
    except:
        st.write('Nenhuma viabilidade salva no momento')

with col2:
    st.write('Editor de viabilidade')
    acesso_ed_viab = st.button('Acessar')

    if acesso_ed_viab:
        st.switch_page('pages/ed_viab.py')