import streamlit as st
import json
from padroes.formapgt import FormaPagamento
from padroes.despesas import Categoria, SubCategoria, Despesa

st.page_link('home.py', label='Página Inicial')

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
        valmix = []
        for v in mixpg:
            valmix.append(v)
        despsubmitted = st.form_submit_button('Salvar Despesa')

        if despsubmitted:
            varmxpag = FormaPagamento('', numparc, mixpg)
            despcat = Categoria(catdesp, SubCategoria(subcat))
            vardesp = Despesa(nomedesp, valordesp, varmxpag, despcat)
            try:
                basedesps = json.load(open('despproj.json'))
                basedesps[nomedesp] = {
                    'Categoria': catdesp,
                    'SubCategoria': subcat,
                    'Valor': valordesp,
                    'Parcelas': numparc,
                }
                json.dump(basedesps, open('despproj.json', mode='w'))
            except:
                basedesps = {}
                basedesps[nomedesp] = {
                    'Categoria': catdesp,
                    'SubCategoria': subcat,
                    'Valor': valordesp,
                    'Parcelas': numparc,
                }
                json.dump(basedesps, open('despproj.json', mode='w'))

with col2:
    try:
        visualizdesp = json.load(open('despproj.json'))
        selecao = st.selectbox('Despesas já salvas', visualizdesp)

        if selecao:
            with st.form('desp para editar'):
                dicselec = visualizdesp[selecao]
                st.write(selecao)
                edit_catdesp = st.text_input('Categoria da despesa', dicselec['Categoria'])
                edit_subcat = st.text_input('SubCategoria da despesa', dicselec['SubCategoria'])
                edit_valordesp = st.number_input('Valor total da despesa, sem descontos', 0.00, step=0.01, value=dicselec['Valor'])
                edit_numparc = st.number_input('Quantidade de parcelas', 0, step=1, value=dicselec['Parcelas'])

                buteditdesp = st.form_submit_button('Salvar Alterações')
                if buteditdesp:
                    visualizdesp[selecao] = {
                    'Categoria': edit_catdesp,
                    'SubCategoria': edit_subcat,
                    'Valor': edit_valordesp,
                    'Parcelas': edit_numparc
                    }
                    json.dump(visualizdesp, open('despproj.json', mode='w'))


            
    except:
        st.write('Nenhuma despesa registrada ainda')

butapagdespesas = st.button('Apagar despesas registradas')

if butapagdespesas:
    emptydic = {}
    json.dump(emptydic, open('despproj.json', mode='w'))