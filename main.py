import streamlit as st
import datetime
import os

# 1. Configuración y Estilo "Noche Estrellada & Dorado Pro"
st.set_page_config(page_title="Boda Joseline & Carlos", page_icon="💍", layout="centered")

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
    
    /* Encabezado Cursivo GIGANTE y Dorado Metálico */
    .header-container {
        text-align: center;
        margin-bottom: 30px;
        padding-top: 20px;
    }
    .logo-text {
        font-family: 'Great Vibes', cursive;
        color: #E6BE8A; /* Tono Champagne Gold */
        font-size: 130px; /* Tamaño máximo impacto */
        text-shadow: 0px 0px 25px rgba(230, 190, 138, 0.6);
        margin: 0;
        line-height: 0.7;
    }
    .names-text {
        font-family: 'Great Vibes', cursive;
        color: #D4AF37; /* Dorado Clásico */
        font-size: 85px; /* Tamaño máximo impacto */
        text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.5);
        margin-top: 5px;
        line-height: 1.1;
    }

    /* Estilos de texto general */
    h3, .stMarkdown, p, label {
        color: #F5F5F5 !important;
        text-align: center;
        font-family: 'Playfair Display', serif;
    }

    /* CENTRADO ABSOLUTO DE BOTONES (Radio Buttons) */
    div.stRadio > div {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 15px !important;
        width: 100% !important;
    }
    
    /* Estilo de cápsulas para los botones */
    div.stRadio label {
        background-color: rgba(212, 175, 55, 0.1) !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 30px !important;
        padding: 12px 30px !important;
        color: white !important;
        transition: 0.3s ease;
        font-weight: bold;
        cursor: pointer;
        font-size: 18px !important;
    }
    
    div.stRadio label:hover {
        background-color: rgba(212, 175, 55, 0.3) !important;
        transform: scale(1.05);
        box-shadow: 0px 0px 15px rgba(212, 175, 55, 0.4);
    }

    /* Ocultar elementos nativos de Streamlit */
    div.stRadio [data-testid="stWidgetLabel"] { display: none; }
    div.stRadio input[type="radio"] { display: none; }

    /* Inputs y Formularios */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid #D4AF37 !important;
        text-align: left !important;
    }

    /* Botón Dorado de Pago Mejorado */
    .stButton>button {
        background: linear-gradient(90deg, #D4AF37 0%, #F4D03F 100%) !important;
        color: #090A0F !important;
        border-radius: 35px !important;
        border: none !important;
        width: 100% !important;
        font-weight: bold !important;
        height: 3.8em !important;
        font-size: 22px !important;
        transition: 0.3s !important;
        box-shadow: 0px 5px 20px rgba(0,0,0,0.4) !important;
    }
    .stButton>button:hover {
        box-shadow: 0px 0px 25px rgba(212, 175, 55, 0.6) !important;
        transform: translateY(-2px);
    }
    
    hr { border-top: 2px solid rgba(212, 175, 55, 0.5); }
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
monto = st.radio(
    "Selección",
    options=["$500", "$1,000", "$1,500"],
    horizontal=True
)

# Mostrar la tarjeta centrada
col1, col2, col3 = st.columns([0.1, 2, 0.1])
with col2:
    if os.path.exists(DATA_REGALOS[monto]["img"]):
        st.image(DATA_REGALOS[monto]["img"], use_container_width=True)
    else:
        st.warning(f"Cargando imagen de {monto}... (Verifica que sea {DATA_REGALOS[monto]['img']})")

# 5. Botón de Pago Mercado Pago
url_pago = DATA_REGALOS[monto]["link"]
st.markdown(f'''
    <a href="{url_pago}" target="_blank" style="text-decoration: none;">
        <div style="background: linear-gradient(90deg, #D4AF37 0%, #F4D03F 100%); 
                    color: #090A0F; padding: 20px; border-radius: 40px; 
                    text-align: center; font-weight: bold; font-size: 24px; 
                    margin: 15px 0px; box-shadow: 0px 8px 25px rgba(212, 175, 55, 0.4);">
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
    else:
        st.error("Por favor, completa los campos para enviar tu mensaje.")

# 7. Acceso Privado
with st.expander("🔐 Acceso Privado"):
    clave = st.text_input("Contraseña:", type="password")
    if clave == "Boda2026":
        st.write("### 📜 Mensajes Recibidos")
        if os.path.exists("mensajes_boda.txt"):
            with open("mensajes_boda.txt", "r", encoding="utf-8") as f:
                st.text_area("Lectura de mensajes:", f.read(), height=300)
        else:
            st.info("Aún no hay mensajes registrados.")
