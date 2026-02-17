import streamlit as st
import datetime
import os

# 1. Configuración y Estilo "Noche Estrellada & Dorado Pro"
st.set_page_config(page_title="Boda Carlos y Joseline", page_icon="💍", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@400;700&display=swap');

    /* Fondo de cielo oscuro con estrellas */
    .stApp {
        background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
        background-attachment: fixed;
    }
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: url('https://www.transparenttextures.com/patterns/stardust.png');
        opacity: 0.3;
        pointer-events: none;
    }
    
    /* ENCABEZADO: Forzamos el tamaño con !important */
    .header-container {
        text-align: center;
        width: 100%;
        padding: 40px 0 20px 0;
    }
    .logo-text {
        font-family: 'Great Vibes', cursive !important;
        color: #E6BE8A !important;
        font-size: 120px !important; /* Aún más grande */
        text-shadow: 0px 0px 30px rgba(230, 190, 138, 0.7) !important;
        margin: 0 !important;
        line-height: 0.6 !important;
    }
    .names-text {
        font-family: 'Great Vibes', cursive !important;
        color: #D4AF37 !important;
        font-size: 70px !important; /* Aún más grande */
        text-shadow: 0px 0px 20px rgba(212, 175, 55, 0.5) !important;
        margin-top: 20px !important;
        line-height: 1 !important;
    }

    /* CENTRADO DE BOTONES: Selector ultra-específico */
    div[data-testid="stRadio"] > div[role="radiogroup"] {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 20px !important;
        width: 100% !important;
        margin: 0 auto !important;
    }
    
    /* Estilo de los botones */
    div[data-testid="stRadio"] label {
        background-color: rgba(212, 175, 55, 0.1) !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 35px !important;
        padding: 15px 40px !important;
        color: white !important;
        transition: 0.3s ease !important;
        font-weight: bold !important;
        font-size: 22px !important; /* Texto del botón más legible */
    }
    
    div[data-testid="stRadio"] label:hover {
        background-color: rgba(212, 175, 55, 0.4) !important;
        transform: scale(1.08);
    }

    /* Ocultar el círculo blanco original de Streamlit */
    div[data-testid="stRadio"] div[data-testid="stMarkdownContainer"] { display: none !important; }
    div[data-testid="stRadio"] input { display: none !important; }

    /* Estilos de texto general */
    h3, .stMarkdown, p {
        color: #F5F5F5 !important;
        text-align: center !important;
        font-family: 'Playfair Display', serif;
    }

    /* Botón Dorado de Pago */
    .stButton>button {
        background: linear-gradient(90deg, #D4AF37 0%, #F4D03F 100%) !important;
        color: #090A0F !important;
        border-radius: 40px !important;
        font-weight: bold !important;
        height: 4em !important;
        font-size: 24px !important;
    }
    
    hr { border-top: 2px solid rgba(212, 175, 55, 0.6); }
    </style>
    """, unsafe_allow_html=True)

# 2. Encabezado
st.markdown('''
    <div class="header-container">
        <p class="logo-text">C & J</p>
        <p class="names-text">Joseline & Carlos</p>
    </div>
    ''', unsafe_allow_html=True)

st.subheader("✨ Nuestra Mesa de Regalos Digital ✨")
st.write("Tu presencia ilumina nuestro universo. Si deseas tener un detalle con nosotros, puedes elegir una de las opciones.")

# 3. Datos de Regalos
DATA_REGALOS = {
    "$500": {"link": "https://mpago.li/2FdE5fx", "img": "gracias_500.png"},
    "$1,000": {"link": "https://mpago.li/2Zeechq", "img": "gracias_1000.png"},
    "$1,500": {"link": "https://mpago.li/2E5Rjr1", "img": "gracias_1500.png"}
}

# 4. Selección del Regalo
st.write("---")
st.write("### 🎁 Elige el monto de tu regalo")
monto = st.radio("Seleccion", options=["$500", "$1,000", "$1,500"], horizontal=True, label_visibility="collapsed")

# Mostrar la tarjeta centrada
col1, col2, col3 = st.columns([0.1, 2, 0.1])
with col2:
    if os.path.exists(DATA_REGALOS[monto]["img"]):
        st.image(DATA_REGALOS[monto]["img"], use_container_width=True)
    else:
        st.warning(f"Cargando imagen de {monto}...")

# 5. Botón de Pago Mercado Pago
url_pago = DATA_REGALOS[monto]["link"]
st.markdown(f'''
    <a href="{url_pago}" target="_blank" style="text-decoration: none;">
        <div style="background: linear-gradient(90deg, #D4AF37 0%, #F4D03F 100%); 
                    color: #090A0F; padding: 25px; border-radius: 45px; 
                    text-align: center; font-weight: bold; font-size: 26px; 
                    margin: 15px 0px; box-shadow: 0px 8px 30px rgba(212, 175, 55, 0.5);">
            Regalar Tarjeta de {monto} 💳
        </div>
    </a>
    ''', unsafe_allow_html=True)

# 6. Libro de Mensajes
st.divider()
st.subheader("✍️ Déjanos un mensaje en las estrellas")
with st.form("libro_oro"):
    nombre = st.text_input("Tu nombre:")
    mensaje = st.text_area("Tus deseos para nosotros:")
    confirmar = st.form_submit_button("Enviar Mensaje ✨")

if confirmar:
    if nombre and mensaje:
        fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        registro = f"DE: {nombre} | REGALÓ: {monto} | MENSAJE: {mensaje} | FECHA: {fecha}\n{'-'*60}\n"
        with open("mensajes_boda.txt", "a", encoding="utf-8") as f:
            f.write(registro)
        st.success(f"¡Gracias {nombre}! Tu mensaje ha sido guardado. ❤️")
        st.balloons()

# 7. Acceso Privado
with st.expander("🔐 Acceso Privado"):
    clave = st.text_input("Contraseña:", type="password")
    if clave == "Boda2026":
        if os.path.exists("mensajes_boda.txt"):
            with open("mensajes_boda.txt", "r", encoding="utf-8") as f:
                st.text_area("Mensajes:", f.read(), height=300)
