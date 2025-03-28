import streamlit as st
import pandas as pd
import os

# Nome do arquivo onde as respostas serão armazenadas
CSV_FILE = "respostas_logotipo.csv"

# Lista de perguntas para o briefing
perguntas = [
    "Nome da empresa/marca:",
    "Slogan (se houver):",
    "Área de atuação:",
    "Produtos/serviços oferecidos:",
    "Quem são os clientes ideais? (idade, gênero, localização, interesses):",
    "Qual a percepção que deseja transmitir ao público? (ex.: confiabilidade, inovação, sofisticação, acessibilidade):",
    "A empresa já possui uma identidade visual ou está começando do zero?",
    "Já possui uma paleta de cores definida? (Se sim, especifique as cores):",
    "Quais cores deseja no logotipo? Alguma cor a ser evitada?",
    "Tem alguma fonte/tipografia preferida? (ex.: serifada, sem serifa, manuscrita, futurista):",
    "Há referências ou inspirações que gosta? (ex.: logotipos de outras marcas que admira, estilos gráficos):",
    "Que estilo de logotipo prefere? (Tipográfico, Símbolo + texto, Emblema, Abstrato, Outro):",
    "Existe algum símbolo ou elemento gráfico que gostaria de incluir?",
    "Quais palavras descrevem melhor a marca? (ex.: moderna, sofisticada, sustentável, minimalista):",
    "Que sensação o logotipo deve transmitir? (ex.: confiança, proximidade, criatividade):",
    "Onde o logotipo será mais utilizado? (ex.: site, redes sociais, papelaria, embalagens, uniformes):",
    "Precisa de versões específicas? (ex.: versão monocromática, favicon, ícone para redes sociais):",
    "Há algo mais que devemos considerar?"
]

# Função para carregar respostas salvas
def carregar_respostas():
    if os.path.exists(CSV_FILE) and os.path.getsize(CSV_FILE) > 0:
        try:
            return pd.read_csv(CSV_FILE)
        except pd.errors.EmptyDataError:
            return pd.DataFrame(columns=perguntas)
    else:
        return pd.DataFrame(columns=perguntas)

# Interface do Streamlit
st.title("Formulário de Briefing para Logotipo")

dados = {}
for pergunta in perguntas:
    resposta = st.text_input(pergunta, "")
    dados[pergunta] = resposta

if st.button("Salvar Respostas"):
    df = carregar_respostas()
    novo_registro = pd.DataFrame([dados])
    df = pd.concat([df, novo_registro], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)
    st.success("Respostas salvas com sucesso!")

# Permitir o download do arquivo CSV
if os.path.exists(CSV_FILE) and os.path.getsize(CSV_FILE) > 0:
    with open(CSV_FILE, "rb") as f:
        st.download_button("Baixar Respostas", f, file_name="respostas_logotipo.csv", mime="text/csv")
