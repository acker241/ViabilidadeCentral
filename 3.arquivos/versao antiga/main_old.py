import streamlit as st
from compraerevenda.despesas import Despesa
from compraerevenda.despesas import Categoria
from compraerevenda.despesas import SubCategoria
from compraerevenda.formapgt import FormaPagamento
from compraerevenda.formapgt import MixPag
#from compraerevenda.receitas import Receita

st.title('Cálculo Viabilidade')

col1, col2 = st.columns(2)


with col1:
    with st.form('DespForm'):
        st.write('Inclusão dos dados básicos de despesas')
        nomedesp = st.text_input('Nome da despesa')
        catdesp = st.text_input('Categoria da despesa')
        subcat = st.text_input('SubCategoria da despesa')

        valordesp = st.number_input('Valor total da despesa, sem descontos', 0.00, step=0.01)
        numparc = st.number_input('Quantidade de parcelas', 0, step=1)
        parclist = []
        st.write('Mix de pagamentos')
        mixpg = st.data_editor(parclist, num_rows='dynamic', disabled=False)
        despsubmitted = st.form_submit_button('Salvar Despesa')

        if despsubmitted:
            varmxpag = FormaPagamento('', numparc, MixPag(mixpg))
            despcat = Categoria(catdesp, SubCategoria(subcat))
            vardesp = Despesa(nomedesp, valordesp, varmxpag, despcat)