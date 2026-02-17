import streamlit as st
import os

# 1. Configuración de Página y Estilo Profesional
st.set_page_config(page_title="Boda Joseline & Carlos", page_icon="💍", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@400;700&display=swap');

    /* Fondo Estrellado */
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

    /* Limitador de ancho para Web (Mantiene el look de smartphone en PC) */
    [data-testid="stAppViewBlockContainer"] {
        max-width: 600px !important;
        padding-top: 2rem !important;
        margin: auto !important;
    }
    
    /* ENCABEZADO: Separación optimizada */
    .header-container { text-align: center; padding-bottom: 20px; }
    .logo-text {
        font-family: 'Great Vibes', cursive !important;
        color: #E6BE8A !important;
        font-size: 100px !important;
        text-shadow: 0px 0px 25px rgba(230, 190, 138, 0.6) !important;
        margin: 0 0 30px 0 !important; /* Espacio para no encimarse */
        line-height: 1.2 !important;
    }
    .names-text {
        font-family: 'Great Vibes', cursive !important;
        color: #D4AF37 !important;
        font-size: 65px !important;
        text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.4) !important;
        margin-top: 10px !important;
        line-height: 1 !important;
    }

    /* SECCIÓN DE BOTONES: Alineación perfecta */
    div[data-testid="stRadio"] > div[role="radiogroup"] {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        gap: 12px !important;
        width: 100% !important;
    }
    
    div[data-testid="stRadio"] label {
        background-color: rgba(212, 175, 55, 0.1) !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 30px !important;
        padding: 0 !important; 
        color: white !important;
        flex: 1 !important;
        height: 50px !important; 
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }

    div[data-testid="stRadio"] label p {
        font-size: 19px !important;
        font-weight: bold !important;
        color: white !important;
        margin: 0 !important;
        white-space: nowrap !important;
    }

    div[data-testid="stRadio"] input { display: none !important; }

    /* Estilo del Formulario HTML */
    .form-input {
        width: 100%;
        padding: 12px;
        margin-bottom: 15px;
        border-radius: 10px;
        border: 1px solid #D4AF37;
        background: rgba(255, 255, 255, 0.05);
        color: white;
        font-family: 'Playfair Display', serif;
    }
    
    .form-button {
        background: linear-gradient(90deg, #D4AF37 0%, #F4D03F 100%);
        color: #090A0F;
        border: none;
        padding: 15px;
        border-radius: 40px;
        font-weight: bold;
        font-size: 20px;
        width: 100%;
        cursor: pointer;
        box-shadow: 0px 5px 15px rgba(212, 175, 55, 0.3);
    }

    h3, .stMarkdown, p {
        color: #F5F5F5 !important;
        text-align: center !important;
        font-family: 'Playfair Display', serif;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Encabezado
st.markdown('''
    <div class="header-container">
        <p class="names-text">Nos Casamos</p>
        <p class="names-text">Joseline & Carlos</p>
    </div>
    ''', unsafe_allow_html=True)

st.subheader("✨ Nuestra Mesa de Regalos Digital ✨")
st.write("Tu presencia ilumina nuestro universo. Si deseas tener un detalle con nosotros, puedes elegir una de las siguiente tarjetas:")

# 3. Datos de Regalos
DATA_REGALOS = {
    "Ninguna": {"link": None, "img": None},
    "$500": {"link": "https://mpago.li/2FdE5fx", "img": "gracias_500.png"},
    "$1,000": {"link": "https://mpago.li/2Zeechq", "img": "gracias_1000.png"},
    "$1,500": {"link": "https://mpago.li/2E5Rjr1", "img": "gracias_1500.png"}
}

st.write("### 🎁 Mesa de Regalos Digital (Opcional)")
monto = st.radio("Monto", options=["Ninguna", "$500", "$1,000", "$1,500"], horizontal=True, label_visibility="collapsed")

# Visualización de Tarjeta y Botón de Pago
if monto != "Ninguna":
    if os.path.exists(DATA_REGALOS[monto]["img"]):
        st.image(DATA_REGALOS[monto]["img"], use_container_width=True)
    
    st.markdown(f'''
        <a href="{DATA_REGALOS[monto]["link"]}" target="_blank" style="text-decoration: none;">
            <div style="background: linear-gradient(90deg, #D4AF37 0%, #F4D03F 100%); 
                        color: #090A0F; padding: 20px; border-radius: 40px; 
                        text-align: center; font-weight: bold; font-size: 22px; 
                        margin: 15px 0px; box-shadow: 0px 8px 25px rgba(212, 175, 55, 0.4);">
                Regalar Tarjeta de {monto} 💳
            </div>
        </a>
        ''', unsafe_allow_html=True)
else:
    st.info("¡Puedes dejarnos un mensaje abajo! 👇")

# 4. Formulario de Mensajes vía Formspree
st.divider()
st.subheader("✍️ Déjanos un mensaje en las estrellas")

# Integramos tu ID de Formspree directamente
FORMSPREE_URL = "https://formspree.io/f/xlgwnwwz"

form_html = f"""
    <form action="{FORMSPREE_URL}" method="POST">
        <input type="text" name="Nombre" class="form-input" placeholder="Tu nombre" required>
        <input type="hidden" name="Regalo_Elegido" value="{monto}">
        <textarea name="Mensaje" class="form-input" placeholder="Tus deseos para nosotros" style="height: 120px;" required></textarea>
        <button type="submit" class="form-button">Enviar Mensaje ✨</button>
    </form>
"""
st.markdown(form_html, unsafe_allow_html=True)

st.write("")
st.caption("Al enviar el mensaje, serás redirigido para confirmar que no eres un robot.")
