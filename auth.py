import streamlit as st
import base64

# ==============================================================================
# 🔐 BANCO DE DADOS DE USUÁRIOS
# ==============================================================================
USUARIOS = {
    "admin": "@tecadi2026",
    "gerentes": "@tecadi2026",
    "supervisores": "@tecadi2026"
}

def init_session_state():
    """Inicializa as variáveis de sessão."""
    if "logado" not in st.session_state:
        st.session_state.logado = False
    if "usuario" not in st.session_state:
        st.session_state.usuario = ""

def get_base64_img(file_path):
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return ""

def login_screen():
    """Renderiza a tela de login."""
    bg_b64 = get_base64_img("assets/tecadi.png")
    bg_css = f'background-image: url("data:image/png;base64,{bg_b64}");' if bg_b64 else 'background-color: #0c2340;'

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');

        html, body, [class*="css"], [class*="st-"] {{ font-family: 'Montserrat', sans-serif !important; }}
        [data-testid="stApp"] {{ {bg_css} background-size: cover !important; background-position: center !important; background-attachment: fixed !important; }}
        [data-testid="stHeader"], [data-testid="stDecoration"], [data-testid="stToolbar"], [data-testid="stSidebar"], [data-testid="collapsedControl"] {{ display: none !important; }}
        section[data-testid="stMain"] {{ background: transparent !important; }}

        .block-container {{
            background: rgba(15, 25, 40, 0.85) !important; backdrop-filter: blur(10px) !important;
            -webkit-backdrop-filter: blur(10px) !important; max-width: 400px !important; margin: 12vh auto !important;
            padding: 40px 30px !important; border-radius: 16px !important; border: 1px solid rgba(255, 255, 255, 0.1) !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.8) !important;
        }}

        .titulo-login {{ color: #ffffff !important; font-size: 34px !important; font-weight: 700 !important; text-align: center !important; margin-bottom: 5px !important; }}
        .subtitulo-login {{ color: #deba0d !important; font-size: 14px !important; font-weight: 600 !important; text-align: center !important; letter-spacing: 1px !important; margin-bottom: 30px !important; text-transform: uppercase !important; }}
        
        div[data-testid="stTextInput"] label p {{ color: #ffffff !important; font-weight: 600 !important; }}
        div[data-testid="stTextInput"] input {{ background-color: #ffffff !important; color: #000000 !important; border: 1px solid rgba(255, 255, 255, 0.2) !important; border-radius: 8px !important; padding: 12px !important; font-weight: bold !important; }}
        div[data-testid="stTextInput"] input:focus {{ border-color: #deba0d !important; box-shadow: 0 0 8px rgba(222, 186, 13, 0.5) !important; }}
        
        div[data-testid="stButton"] button {{ background-color: #0c2340 !important; color: #ffffff !important; border: 1px solid #deba0d !important; border-radius: 8px !important; width: 100% !important; padding: 12px !important; font-size: 16px !important; font-weight: bold !important; margin-top: 20px !important; transition: 0.3s !important; }}
        div[data-testid="stButton"] button:hover {{ background-color: #deba0d !important; color: #0c2340 !important; }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="titulo-login">🔐 Portaria Digital</div>
        <div class="subtitulo-login">Central de Apps Tecadi</div>
    """, unsafe_allow_html=True)

    usuario = st.text_input("Usuário").lower().strip()
    senha = st.text_input("Senha", type="password")

    if st.button("ENTRAR", use_container_width=True):
        if usuario in USUARIOS and senha == USUARIOS[usuario]:
            st.session_state.logado = True
            st.session_state.usuario = usuario
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos.")

def check_auth():
    """Verifica o status de login."""
    init_session_state()
    return st.session_state.get("logado", False)

def logout():
    """Faz o logout."""
    st.session_state.logado = False
    st.session_state.usuario = ""
    st.rerun()