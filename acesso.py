import streamlit as st
import os
import auth  

# ==============================================================================
# 🛠 CONFIGURAÇÃO DA PÁGINA
# ==============================================================================
st.set_page_config(
    page_title="Central de Apps Tecadi",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Verifica a Autenticação
if not auth.check_auth():
    auth.login_screen()
    st.stop()  

# ==============================================================================
# 🎨 ESTILIZAÇÃO CSS DO DASHBOARD LOGADO
# ==============================================================================
def apply_dashboard_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
        html, body, [class*="css"], [class*="st-"] { font-family: 'Montserrat', sans-serif !important; }
        [data-testid="stApp"] { background-color: #f4f7f6 !important; background-image: none !important; }
        
        /* Ajuste do padding-top para não cortar a logo nem o login */
        .block-container { 
            background: transparent !important; 
            backdrop-filter: none !important; 
            max-width: 1200px !important; 
            margin: auto !important; 
            padding-top: 4rem !important; 
            padding-right: 2rem !important;
            padding-bottom: 2rem !important;
            padding-left: 2rem !important;
            border: none !important; 
            box-shadow: none !important; 
        }

        .app-card { background: white; padding: 20px; border-radius: 15px; border-left: 6px solid #0c2340; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: all 0.4s; height: 160px; display: flex; flex-direction: column; align-items: center; justify-content: center; text-decoration: none !important; margin-bottom: 20px; }
        .app-card:hover { transform: translateY(-10px) scale(1.02); background-color: #0c2340; border-left: 6px solid #deba0d; box-shadow: 0 12px 20px rgba(12, 35, 64, 0.2); }
        .app-card:hover .app-title, .app-card:hover .app-desc, .app-card:hover .app-icon { color: #ffffff !important; }
        .app-icon { font-size: 40px; margin-bottom: 10px; transition: 0.3s; }
        .app-title { color: #0c2340; font-size: 16px; font-weight: 700; margin: 0; transition: 0.3s; text-align: center; }
        .app-desc { color: #888; font-size: 11px; margin-top: 5px; transition: 0.3s; text-align: center; }

        .section-header { color: #0c2340; border-bottom: 2px solid #deba0d; padding-bottom: 5px; margin: 30px 0 20px 0; font-weight: 700; font-size: 22px; display: flex; align-items: center; gap: 10px; }
        .sub-section-header { color: #444; font-weight: 600; font-size: 18px; margin: 15px 0 10px 0; }
        div[data-testid="stButton"] button { border-radius: 10px !important; background-color: #0c2340 !important; color: white !important; transition: 0.3s !important; border: none !important; width: auto !important; margin-top: 0 !important; }
        div[data-testid="stButton"] button:hover { background-color: #deba0d !important; color: #0c2340 !important; transform: scale(1.05) !important; }
        </style>
    """, unsafe_allow_html=True)

apply_dashboard_styles()

# ==============================================================================
# 🚀 DASHBOARD PRINCIPAL
# ==============================================================================

# Cabeçalho com alinhamento corrigido
col_l, col_empty, col_r = st.columns([2, 5, 2])
with col_l:
    if os.path.exists('assets/logosemfundotecadi.png'):
        st.markdown('<div style="margin-top: 15px;">', unsafe_allow_html=True)
        st.image('assets/logosemfundotecadi.png', width=180)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color: #0c2340; margin-top: 15px;'>Tecadi Logística</h3>", unsafe_allow_html=True)

with col_r:
    st.markdown(f"<div style='text-align: right; color: #0c2340; font-weight: 700; font-size: 18px; margin-top: 10px; margin-bottom: 10px;'>👤 {st.session_state.usuario.upper()}</div>", unsafe_allow_html=True)
    col_btn_vazio, col_btn_sair = st.columns([1, 1])
    with col_btn_sair:
        if st.button("Sair", use_container_width=True):
            auth.logout()

st.markdown("<h1 style='text-align: center; color: #0c2340; margin-bottom: 0; margin-top: 20px;'>Hub de Soluções Tecadi</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Selecione o painel operacional abaixo</p>", unsafe_allow_html=True)

def render_app_card(nome, url, icon):
    st.markdown(f'<a href="{url}" target="_blank" style="text-decoration: none;"><div class="app-card"><div class="app-icon">{icon}</div><div class="app-title">{nome}</div><div class="app-desc">Clique para acessar</div></div></a>', unsafe_allow_html=True)

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
with p5: render_app_card("Painel Sestini", "https://sestinitecadi.streamlit.app/", "🧳")

# --- SETOR 3: INDICADORES ---
st.markdown('<div class="section-header">📈 Gestão e Indicadores</div>', unsafe_allow_html=True)
i1, _, _, _, _ = st.columns(5)
with i1: render_app_card("SLA Tecadi", "https://slatecadi.streamlit.app/", "📉")

# --- SETOR 4: APLICATIVOS ACURACIDADE ---
st.markdown('<div class="section-header">🎯 Aplicativos Acuracidade</div>', unsafe_allow_html=True)

st.markdown('<div class="sub-section-header">ZEN (107)</div>', unsafe_allow_html=True)
a1, a2, a3, a4 = st.columns(4)
with a1: render_app_card("Pulos de Endereço", "https://acuracidade-zen-pulos.streamlit.app/", "📍")
with a2: render_app_card("Cortes de Pedido", "https://acuracidade-zen-cortes-de-pedido.streamlit.app/", "✂️")
with a3: render_app_card("Painel Operacional", "https://operacional-zen-acompanhamento.streamlit.app/", "⚙️")
with a4: render_app_card("Mapa de Calor Picking", "https://picking-abc-zen.streamlit.app/", "🔥")

st.markdown('<div class="sub-section-header">Geral (103, 107, 108 e 117)</div>', unsafe_allow_html=True)
g1, _, _, _ = st.columns(4)
with g1: render_app_card("Pendências WMS Fênix", "https://pendencias-wms-fenix.streamlit.app/", "📋")

# ==============================================================================
# 👣 FOOTER
# ==============================================================================
st.markdown("<br><br><hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: #888; font-size: 12px; padding-bottom: 20px;'>Tecadi Logística © 2026 | Sucesso do Cliente | Versão Enterprise 2.1</div>", unsafe_allow_html=True)
