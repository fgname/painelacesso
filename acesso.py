import streamlit as st
import base64
import os

# ==============================================================================
# 🛠 CONFIGURAÇÃO DA PÁGINA E ESTILO
# ==============================================================================
st.set_page_config(
    page_title="Central de Apps Tecadi",
    page_icon="favicon.ico",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

if os.path.exists('tecadi.png'):
    set_background('tecadi.png')

# ==============================================================================
# 🔐 MÓDULO DE LOGIN MULTI-PERFIL TECADI
# ==============================================================================
def modulo_login():
    if "logado" not in st.session_state:
        st.session_state.logado = False
        st.session_state.perfil = None

    if not st.session_state.logado:
        st.markdown("""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
            html, body, [class*="css"], [class*="st-"] {
                font-family: 'Montserrat', sans-serif !important;
            }
            header[data-testid="stHeader"] { display: none !important; }
            
            /* Removemos o fundo azul bugado e simplificamos a caixa */
            .login-box {
                max-width: 400px;
                margin: 50px auto;
                text-align: center;
            }
            
            /* Textos do Login em Preto */
            .titulo-login {
                color: #000000;
                font-size: 32px;
                font-weight: 700;
                margin-bottom: 5px;
            }
            
            .subtitulo-login {
                color: #deba0d; /* Amarelo Tecadi para contraste */
                margin-bottom: 30px;
                font-size: 14px;
                font-weight: 600;
            }
            
            /* Forçar textos de "Usuário" e "Senha" para Preto */
            div[data-testid="stTextInput"] label p {
                color: #000000 !important;
                font-weight: 600;
            }

            .stButton>button {
                background-color: #deba0d;
                color: #0c2340;
                border-radius: 8px;
                font-weight: bold;
                border: none;
                height: 45px;
                transition: 0.3s;
                margin-top: 10px;
            }
            .stButton>button:hover {
                background-color: #0c2340;
                color: #ffffff;
            }
            </style>
        """, unsafe_allow_html=True)

        _, col2, _ = st.columns([1, 1.5, 1])
        with col2:
            st.markdown('<div class="login-box">', unsafe_allow_html=True)
            
            # Textos
            st.markdown('<div class="titulo-login">🔐 Portaria Digital</div>', unsafe_allow_html=True)
            st.markdown('<div class="subtitulo-login">Desenvolvido por Sucesso do Cliente</div>', unsafe_allow_html=True)

            usuario = st.text_input("Usuário", placeholder="Admin ou Gerente")
            senha = st.text_input("Senha", type="password", placeholder="••••••••")

            if st.button("ACESSAR PLATAFORMA", use_container_width=True):
                users = {
                    "admin": "@tecadi2026",
                    "gerente": "@solucoes2026"
                }
                
                if usuario.lower() in users and senha == users[usuario.lower()]:
                    st.session_state.logado = True
                    st.session_state.perfil = usuario.lower()
                    st.rerun()
                else:
                    st.error("Credenciais inválidas")
            
            st.markdown('</div>', unsafe_allow_html=True)
        st.stop()

modulo_login()

# ==============================================================================
# 🚀 DASHBOARD PRINCIPAL (PÓS-LOGIN)
# ==============================================================================

st.markdown("""
    <style>
    .app-card {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 25px;
        border-radius: 12px;
        border-left: 6px solid #0c2340;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: 0.3s;
        height: 180px;
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-decoration: none !important;
    }
    .app-card:hover {
        transform: translateY(-5px);
        background-color: #ffffff;
        box-shadow: 0 10px 15px rgba(0,0,0,0.2);
        border-left: 6px solid #deba0d;
    }
    .app-title {
        color: #0c2340;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .app-desc {
        color: #666;
        font-size: 13px;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Cabeçalho do Portal (Logo e User/Logout)
col_logo, col_empty, col_user = st.columns([1, 1, 1])

with col_logo:
    if os.path.exists('logosemfundotecadi.png'):
        st.image('logosemfundotecadi.png', width=180)

with col_user:
    # Bem-vindo em Preto
    st.markdown(f"<div style='text-align: right; color: #000000; padding-top: 10px; margin-bottom: 5px;'>Bem-vindo, <b>{st.session_state.perfil.capitalize()}</b></div>", unsafe_allow_html=True)
    
    # Botão de sair usando a funcionalidade nativa para não bugar o navegador
    col_espaco, col_btn = st.columns([3, 1])
    with col_btn:
        if st.button("Sair"):
            st.session_state.logado = False
            st.session_state.perfil = None
            st.rerun()

# Textos do dashboard em PRETO
st.markdown("<h2 style='color: #000000; text-align: center;'>Central de Aplicativos</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #000000; text-align: center; margin-bottom: 40px; font-weight: 500;'>Selecione o sistema que deseja acessar abaixo:</p>", unsafe_allow_html=True)

# Definição dos Apps
apps = [
    {"nome": "Horímetro Tecadi", "url": "https://htecadi.streamlit.app/", "icon": "⏱️"},
    {"nome": "Ocupação Tecadi", "url": "https://ocupacaotecadi.streamlit.app/", "icon": "📊"},
    {"nome": "MOT Tecadi", "url": "https://mottecadi.streamlit.app/", "icon": "🚛"},
    {"nome": "SLA Tecadi", "url": "https://slatecadi.streamlit.app/", "icon": "📉"},
    {"nome": "Movimentações", "url": "https://entradaesaidatecadi.streamlit.app/", "icon": "🔄"},
    {"nome": "Painel Hisense", "url": "https://hisensetecadi.streamlit.app/", "icon": "📺"},
    {"nome": "Painel SKF", "url": "https://skftemporario.streamlit.app/", "icon": "🔩"},
]

# Grid
cols = st.columns(3)
for idx, app in enumerate(apps):
    with cols[idx % 3]:
        st.markdown(f"""
            <a href="{app['url']}" target="_blank" style="text-decoration: none;">
                <div class="app-card">
                    <div style="font-size: 35px; margin-bottom: 10px;">{app['icon']}</div>
                    <div class="app-title">{app['nome']}</div>
                    <div class="app-desc">Clique para abrir em nova aba</div>
                </div>
            </a>
        """, unsafe_allow_html=True)
        st.write("")

st.markdown("---")
# Rodapé em Preto
st.markdown(f"<div style='text-align: center; color: #000000; font-size: 12px; font-weight: 500;'>Desenolvimento Sucesso do Cliente © 2026 - Logado como {st.session_state.perfil}</div>", unsafe_allow_html=True)