import streamlit as st
import google.generativeai as genai


genai.configure(api_key="SUA_CHAVE_AQUI")

st.title("💳 SysFraud AI")


with open("data/regras_fraude.txt", "r", encoding="utf-8") as f:
    criterios = f.read()


abstract = st.text_area("Descreva a transação:")

if st.button("Analisar"):
    model = genai.GenerativeModel('gemini-3.5-flash')
    response = model.generate_content(f"{criterios} Analise: {abstract}")
    st.write(response.text)