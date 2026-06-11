import streamlit as st
import base64
import os

# ==============================================================================
# 🛠 CONFIGURAÇÃO DA PÁGINA
# ==============================================================================
st.set_page_config(
    page_title="Central de Apps Tecadi",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 🎨 ESTILIZAÇÃO CSS PROFISSIONAL (CSS-in-JS Style)
# ==============================================================================
def apply_custom_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');

        /* Reset e Fonte Global */
        html, body, [class*="css"], [class*="st-"] {
            font-family: 'Montserrat', sans-serif !important;
        }

        /* Esconder Elementos Nativos */
        header[data-testid="stHeader"] { visibility: hidden; }
        footer { visibility: hidden; }
        #MainMenu { visibility: hidden; }

        /* Fundo da Aplicação */
        .stApp {
            background-color: #f4f7f6;
        }

        /* Container de Login Otimizado */
        .login-wrapper {
            background: rgba(255, 255, 255, 0.9);
            padding: 3rem;
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            border: 1px solid rgba(255,255,255,0.5);
            text-align: center;
        }

        /* Estilização dos Cards de Apps */
        .app-card {
            background: white;
            padding: 20px;
            border-radius: 15px;
            border-left: 6px solid #0c2340;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            height: 160px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-decoration: none !important;
            margin-bottom: 20px;
        }

        .app-card:hover {
            transform: translateY(-10px) scale(1.02);
            background-color: #0c2340;
            border-left: 6px solid #deba0d;
            box-shadow: 0 12px 20px rgba(12, 35, 64, 0.2);
        }

        .app-card:hover .app-title, .app-card:hover .app-desc, .app-card:hover .app-icon {
            color: #ffffff !important;
        }

        .app-icon { font-size: 40px; margin-bottom: 10px; transition: 0.3s; }
        .app-title { color: #0c2340; font-size: 16px; font-weight: 700; margin: 0; transition: 0.3s; }
        .app-desc { color: #888; font-size: 11px; margin-top: 5px; transition: 0.3s; }

        /* Títulos de Seção */
        .section-header {
            color: #0c2340;
            border-bottom: 2px solid #deba0d;
            padding-bottom: 5px;
            margin: 30px 0 20px 0;
            font-weight: 700;
            font-size: 22px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        /* Botão Sair Premium */
        .stButton>button {
            border-radius: 10px;
            background-color: #0c2340;
            color: white;
            transition: 0.3s;
            border: none;
        }
        .stButton>button:hover {
            background-color: #deba0d;
            color: #0c2340;
            transform: scale(1.05);
        }

        /* Inputs de Texto */
        div[data-testid="stTextInput"] label p {
            color: #0c2340 !important;
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_styles()

# ==============================================================================
# 🔐 MÓDULO DE LOGIN
# ==============================================================================
def login():
    if "logado" not in st.session_state:
        st.session_state.logado = False

    if not st.session_state.logado:
        _, col_central, _ = st.columns([1, 1.2, 1])
        
        with col_central:
            st.markdown('<div class="login-wrapper">', unsafe_allow_html=True)
            if os.path.exists('logosemfundotecadi.png'):
                st.image('logosemfundotecadi.png', width=250)
            
            st.markdown("<h2 style='color: #0c2340; margin-top:0;'>Portaria Digital</h2>", unsafe_allow_html=True)
            st.markdown("<p style='color: #deba0d; font-weight: 600;'>Sucesso do Cliente Tecadi</p>", unsafe_allow_html=True)

            user = st.text_input("Usuário")
            pwd = st.text_input("Senha", type="password")
            
            if st.button("ACESSAR SISTEMA", use_container_width=True):
                users = {"admin": "@tecadi2026", "gerente": "@solucoes2026"}
                if user.lower() in users and pwd == users[user.lower()]:
                    st.session_state.logado = True
                    st.session_state.perfil = user.lower()
                    st.rerun()
                else:
                    st.error("Credenciais inválidas")
            st.markdown('</div>', unsafe_allow_html=True)
        st.stop()

login()

# ==============================================================================
# 🚀 DASHBOARD PRINCIPAL
# ==============================================================================

# Top Bar (Header)
col_l, col_r = st.columns([1, 1])
with col_l:
    if os.path.exists('logosemfundotecadi.png'):
        st.image('logosemfundotecadi.png', width=180)

with col_r:
    st.markdown(f"<div style='text-align: right; color: #0c2340; font-weight: 600;'>👤 {st.session_state.perfil.upper()}</div>", unsafe_allow_html=True)
    col_btn_l, col_btn_r = st.columns([4, 1])
    with col_btn_r:
        if st.button("Sair"):
            st.session_state.logado = False
            st.rerun()

st.markdown("<h1 style='text-align: center; color: #0c2340; margin-bottom: 0;'>Hub de Soluções Tecadi</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Selecione o painel operacional abaixo</p>", unsafe_allow_html=True)

# Função para renderizar os cards de forma elegante
def render_app_card(nome, url, icon):
    st.markdown(f"""
        <a href="{url}" target="_blank" style="text-decoration: none;">
            <div class="app-card">
                <div class="app-icon">{icon}</div>
                <div class="app-title">{nome}</div>
                <div class="app-desc">Clique para acessar</div>
            </div>
        </a>
    """, unsafe_allow_html=True)

# --- SETOR 1: PRINCIPAIS ACESSOS ---
st.markdown('<div class="section-header">⭐ Principais Acessos</div>', unsafe_allow_html=True)
c1, c2, c3, c4, c5 = st.columns(5)
with c1: render_app_card("Ocupação Tecadi", "https://ocupacaotecadi.streamlit.app/", "📊")
with c2: render_app_card("Visão Geral Pátio", "https://resumopatio.streamlit.app/", "🏗️")
with c3: render_app_card("Movimentações", "https://entradaesaidatecadi.streamlit.app/", "🔄")
with c4: render_app_card("Mot Tecadi", "https://mottecadi.streamlit.app/", "🚛")
with c5: render_app_card("Horímetro Tecadi", "https://htecadi.streamlit.app/", "⏱️")

# --- SETOR 2: PAINÉIS ---
st.markdown('<div class="section-header">🖥️ Painéis de Clientes</div>', unsafe_allow_html=True)
p1, p2, p3, p4, _ = st.columns(5)
with p1: render_app_card("Painel Hisense", "https://hisensetecadi.streamlit.app/", "📺")
with p2: render_app_card("Painel Zen", "https://zentecadi.streamlit.app/", "🧘")
with p3: render_app_card("Painel Midea 117", "https://filial117.streamlit.app/", "❄️")
with p4: render_app_card("Painel SKF", "https://skftemporario.streamlit.app/", "🔩")

# --- SETOR 3: INDICADORES ---
st.markdown('<div class="section-header">📈 Gestão e Indicadores</div>', unsafe_allow_html=True)
i1, _ = st.columns([1, 4])
with i1: render_app_card("SLA Tecadi", "https://slatecadi.streamlit.app/", "📉")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    f"<div style='text-align: center; color: #888; font-size: 12px;'>"
    f"Tecadi Logística © 2026 | Sucesso do Cliente | Versão Enterprise 2.0"
    f"</div>", 
    unsafe_allow_html=True
)
