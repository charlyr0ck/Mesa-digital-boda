import streamlit as st
import datetime
import os

# 1. Configuración y Estilo "Noche Estrellada & Dorado"
st.set_page_config(page_title="Boda Joseline & Carlos", page_icon="💍", layout="centered")

st.markdown("""
    <style>
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
    
    /* Logo y Títulos */
    .logo-container {
        text-align: center;
        margin-bottom: -10px;
    }
    .logo-text {
        font-family: 'Great Vibes', cursive;
        color: #D4AF37;
        font-size: 80px;
        text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.6);
        margin: 0;
    }
    h1, h2, h3 {
        color: #D4AF37 !important;
        text-align: center;
        font-family: 'Playfair Display', serif;
        text-shadow: 0px 0px 10px rgba(212, 175, 55, 0.5);
    }
    .stMarkdown, p, label {
        color: #F5F5F5 !important;
        text-align: center;
    }

    /* CENTRADO DE BOTONES (Radio Buttons) */
    [data-testid="stMarkdownContainer"] + div [role="radiogroup"] {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
        flex-wrap: wrap;
    }

    div.stRadio label {
        background-color: rgba(212, 175, 55, 0.1) !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 25px !important;
        padding: 8px 20px !important;
        color: white !important;
        transition: 0.3s ease;
        font-weight: bold;
    }

    div.stRadio label:hover {
        background-color: rgba(212, 175, 55, 0.3) !important;
        transform: scale(1.05);
    }

    /* Quitar el punto del radio button original */
    div.stRadio [data-testid="stWidgetLabel"] { display: none; }
    div.stRadio input[type="radio"] { display: none; }

    /* Inputs y Formularios */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid #D4AF37 !important;
    }

    /* Botón Dorado */
    .stButton>button {
        background-color: #D4AF37 !important;
        color: #090A0F !important;
        border-radius: 25px;
        border: none;
        width: 100%;
        font-weight: bold;
        height: 3.5em;
        font-size: 18px;
    }
    hr { border-top: 1px solid #D4AF37; }
    </style>
    
    <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# 2. Encabezado con Logo
st.markdown('<div class="logo-container"><p class="logo-text">C & J</p></div>', unsafe_allow_html=True)
st.title("JOSELINE & CARLOS")
st.subheader("✨ Nuestra Mesa de Regalos Digital ✨")
st.write("Tu presencia ilumina nuestro universo. Si deseas tener un detalle con nosotros, puedes elegir una de las siguientes opciones.")

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
col1, col2, col3 = st.columns([0.5, 2, 0.5])
with col2:
    if os.path.exists(DATA_REGALOS[monto]["img"]):
        st.image(DATA_REGALOS[monto]["img"], use_container_width=True)
    else:
        st.warning(f"Cargando imagen de {monto}... (Asegúrate de que se llame {DATA_REGALOS[monto]['img']})")

# 5. Botón de Pago Mercado Pago
url_pago = DATA_REGALOS[monto]["link"]
st.markdown(f'''
    <a href="{url_pago}" target="_blank" style="text-decoration: none;">
        <div style="background: linear-gradient(90deg, #D4AF37 0%, #F4D03F 100%); 
                    color: #090A0F; padding: 18px; border-radius: 35px; 
                    text-align: center; font-weight: bold; font-size: 22px; 
                    margin: 15px 0px; box-shadow: 0px 5px 20px rgba(212, 175, 55, 0.4);">
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
