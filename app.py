import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(page_title="Guardian IA", page_icon="🛡️", layout="centered")

# Estilo visual básico
st.title("🛡️ Guardian Anti-Fraude")
st.subheader("Inteligência Artificial contra Golpes")
st.write("Cole abaixo qualquer mensagem, SMS ou link suspeito que você recebeu.")

# Conectando com a Chave de Segurança (que colocaremos no Streamlit)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Configure a chave de API nas configurações do Streamlit.")

# Função que pergunta para a IA
def analisar_mensagem(texto):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"""
    Você é um especialista em segurança digital e detecção de fraudes. 
    Analise o texto abaixo e responda de forma clara:
    1. Veredito: (GOLPE, SUSPEITO ou SEGURO) em destaque.
    2. Explicação: Por que você chegou a essa conclusão?
    3. O que fazer: Dê um conselho prático ao usuário.
    
    Texto para analisar: {texto}
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "Erro ao conectar com a IA. Verifique sua chave."

# Interface do Usuário
entrada = st.text_area("Mensagem ou Link:", placeholder="Ex: Parabéns! Você recebeu um PIX de R$ 5.000...")

if st.button("Analisar com Inteligência Artificial"):
    if entrada:
        with st.spinner('Analisando padrões e riscos...'):
            resultado = analisar_mensagem(entrada)
            st.markdown("---")
            st.markdown(resultado)
    else:
        st.warning("Por favor, cole algum conteúdo antes de analisar.")

st.markdown("---")
st.caption("Guardian v1.0 - Proteção gratuita e inteligente.")
