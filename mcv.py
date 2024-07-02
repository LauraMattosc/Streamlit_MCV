import streamlit as st
import pandas as pd

# Título do aplicativo
st.title("Análise de Dados de Newsletter")

# Upload da planilha
uploaded_file = st.file_uploader("Faça o upload da planilha com os dados das newsletters", type=["csv"])

if uploaded_file is not None:
    st.write("Arquivo carregado com sucesso!")  # Log de depuração
    try:
        # Tentar ler a planilha com diferentes configurações
        try:
            df = pd.read_csv(uploaded_file, encoding='latin1', delimiter=',', on_bad_lines='skip')
        except pd.errors.ParserError:
            df = pd.read_csv(uploaded_file, encoding='latin1', delimiter=';', on_bad_lines='skip')

        st.write("Planilha lida com sucesso!")  # Log de depuração
        st.write("Dados da planilha bruta:")
        st.write(df)
        
        # Correção e formatação da tabela
        st.write("Corrigindo e formatando os dados...")
        # Aqui você pode adicionar a lógica necessária para corrigir e formatar os dados
        # Por exemplo, removendo valores nulos, ajustando tipos de dados, etc.
        
        # Exemplo de correção simples: removendo linhas com valores nulos
        df_clean = df.dropna()
        st.write("Dados da planilha após correção:")
        st.write(df_clean)
        
        # Outra formatação ou correção específica pode ser aplicada aqui
        
    except Exception as e:
        st.write("Erro ao ler a planilha:", e)
else:
    st.write("Por favor, faça o upload de uma planilha para começar.")
