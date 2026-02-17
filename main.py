
import streamlit as st
import datetime
import os

# 1. Configuración y Estilo "Noche Estrellada & Dorado"
st.set_page_config(page_title="Boda Joseline & Carlos", page_icon="💍", layout="centered")

st.markdown("""
    <style>
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
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid #D4AF37 !important;
    }
    .stButton>button {
        background-color: #D4AF37 !important;
        color: #090A0F !important;
        border-radius: 25px;
        border: none;
        width: 100%;
        font-weight: bold;
    }
    hr { border-top: 1px solid #D4AF37; }
    </style>
    """, unsafe_allow_html=True)

# 2. Encabezado
st.title("JOSELINE & CARLOS")
st.subheader("✨ Nuestra Mesa de Regalos Digital ✨")

# 3. Datos de Regalos (Sustituye con tus links reales)
DATA_REGALOS = {
    "$500": {"link": "https://mpago.li/2FdE5fx", "img": "gracias_500.jpeg"},
    "$1000": {"link": "https://mpago.li/2Zeechq", "img": "gracias_1000.jpeg"},
    "$1500": {"link": "https://mpago.li/2E5Rjr1", "img": "gracias_1500.jpeg"}
}

monto = st.select_slider("Selecciona el monto de tu regalo:", options=["$500", "$1000", "$1500"])
st.image(DATA_REGALOS[monto]["img"], use_container_width=True)

# Botón de Pago
url_pago = DATA_REGALOS[monto]["link"]
st.markdown(f'<a href="{url_pago}" target="_blank" style="text-decoration: none;"><div style="background: linear-gradient(90deg, #D4AF37 0%, #F4D03F 100%); color: #090A0F; padding: 15px; border-radius: 30px; text-align: center; font-weight: bold; font-size: 20px; margin: 20px 0px; box-shadow: 0px 4px 15px rgba(0,0,0,0.3);">🎁 Regalar Tarjeta de {monto}</div></a>', unsafe_allow_html=True)

# 4. Libro de Mensajes
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

# 5. SECCIÓN PRIVADA PARA LOS NOVIOS
st.write("---")
with st.expander("🔐 Acceso Privado (Solo Novios)"):
    clave = st.text_input("Contraseña:", type="password")
    if clave == "Boda2026": # <--- Puedes cambiar esta contraseña
        st.write("### 📜 Libro de Visitas Digital")
        if os.path.exists("mensajes_boda.txt"):
            with open("mensajes_boda.txt", "r", encoding="utf-8") as f:
                contenido = f.read()
                st.text_area("Mensajes recibidos:", contenido, height=400)
                st.download_button("Descargar Libro de Mensajes", contenido, file_name="mensajes_boda.txt")
        else:
            st.info("Aún no hay mensajes registrados.")
