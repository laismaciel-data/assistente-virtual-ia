import streamlit as st
import google.generativeai as genai

# Configuração da sua API Key
genai.configure(api_key="SUA_CHAVE_AQUI")

st.title("SysReview AI - Assistente de Pesquisa")

# Leitura da base de conhecimento
with open("data/criterios.txt", "r") as f:
    criterios = f.read()

abstract = st.text_area("Cole o resumo (abstract) do artigo aqui:")

if st.button("Analisar"):
    model = genai.GenerativeModel('gemini-3.5-flash')
    prompt = f"Com base nestes critérios: {criterios}, analise o abstract: {abstract}. Diga se deve ser incluído ou excluído e por quê."
    response = model.generate_content(prompt)
    st.write(response.text)