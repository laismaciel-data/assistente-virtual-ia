# SysReview AI - Assistente de Revisão Sistemática

Assistente virtual inteligente desenvolvido para auxiliar biomédicos e pesquisadores na triagem de artigos científicos para revisões sistemáticas, utilizando o protocolo PRISMA.

## 6 Passos do Projeto
1. **Documentação:** O agente foca na validação de critérios PICO para triagem de resumos.
2. **Base de Conhecimento:** Dados estruturados em `data/criterios.txt` com as diretrizes de elegibilidade.
3. **Prompts:** Instruções baseadas em persona de especialista em metodologia científica.
4. **Aplicação Funcional:** Interface web desenvolvida com Streamlit e processada via Google Gemini API (modelo gemini-3.5-flash).
5. **Avaliação:** Testado com abstracts de hematologia para validar a concordância com critérios de exclusão.
6. **Pitch:** Ferramenta voltada para reduzir o tempo de triagem manual em 70%.

## Como rodar
1. Clone o repositório.
2. Instale as dependências: `pip install streamlit google-generativeai`
3. Execute: `python -m streamlit run src/app.py`
