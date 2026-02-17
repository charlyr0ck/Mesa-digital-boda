import streamlit as st
from streamlit_gsheets import GSheetsConnection
import datetime
import pandas as pd
import os

# 1. Estilo y Corrección de Visibilidad
st.set_page_config(page_title="Boda Joseline & Carlos", page_icon="💍", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@400;700&display=swap');

    .stApp {
        background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
        background-attachment: fixed;
    }
    
    /* Logo equilibrado */
    .header-container { text-align: center; padding: 10px 0; }
    .logo-text {
        font-family: 'Great Vibes', cursive !important;
        color: #E6BE8A !important;
        font-size: 90px !important;
        text-shadow: 0px 0px 20px rgba(230, 190, 138, 0.6);
        margin: 0 !important;
    }
    .names-text {
        font-family: 'Great Vibes', cursive !important;
        color: #D4AF37 !important;
        font-size: 60px !important;
        margin-top: -10px !important;
    }

    /* BOTONES: Forzar que el texto sea visible */
    div[data-testid="stRadio"] > div[role="radiogroup"] {
        display: flex !important;
        justify-content: center !important;
        gap: 15px !important;
    }
    
    div[data-testid="stRadio"] label {
        background-color: rgba(212, 175, 55, 0.1) !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 30px !important;
        padding: 10px 20px !important;
        color: white !important;
        min-width: 100px !important;
        display: flex !important;
        justify-content: center !important;
    }
    
    /* Asegurar que el texto del monto se vea */
    div[data-testid="stRadio"] label p {
        font-size: 20px !important;
        font-weight: bold !important;
        color: white !important;
        display: block !important;
    }

    div[data-testid="stRadio"] input { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. Conexión y Lógica
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    # Encabezado
    st.markdown('<div class="header-container"><p class="logo-text">C & J</p><p class="names-text">Joseline & Carlos</p></div>', unsafe_allow_html=True)
    st.subheader("✨ Nuestra Mesa de Regalos Digital ✨")

    # Selección
    DATA_REGALOS = {
        "$500": {"link": "https://mpago.li/2FdE5fx", "img": "gracias_500.png"},
        "$1,000": {"link": "https://mpago.li/2Zeechq", "img": "gracias_1000.png"},
        "$1,500": {"link": "https://mpago.li/2E5Rjr1", "img": "gracias_1500.png"}
    }

    monto = st.radio("Seleccion", options=["$500", "$1,000", "$1,500"], horizontal=True, label_visibility="collapsed")

    # Imagen y Botón
    st.image(DATA_REGALOS[monto]["img"], use_container_width=True)
    st.markdown(f'<a href="{DATA_REGALOS[monto]["link"]}" target="_blank" style="text-decoration: none;"><div style="background: linear-gradient(90deg, #D4AF37 0%, #F4D03F 100%); color: #090A0F; padding: 20px; border-radius: 40px; text-align: center; font-weight: bold; font-size: 24px; margin: 15px 0px;">Regalar Tarjeta de {monto} 💳</div></a>', unsafe_allow_html=True)

    # Formulario
    st.divider()
    with st.form("libro_oro", clear_on_submit=True):
        nombre = st.text_input("Tu nombre:")
        mensaje = st.text_area("Tus deseos:")
        if st.form_submit_button("Enviar Mensaje ✨"):
            if nombre and mensaje:
                df_actual = conn.read()
                nueva_fila = pd.DataFrame([{"Fecha": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"), "Nombre": nombre, "Monto": monto, "Mensaje": mensaje}])
                df_final = pd.concat([df_actual, nueva_fila], ignore_index=True)
                conn.update(data=df_final)
                st.success("¡Guardado en Google Sheets! ❤️")
                st.balloons()
except:
    st.warning("Configura tus 'Secrets' en Streamlit para activar el libro de mensajes.")
