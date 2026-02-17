import streamlit as st
from streamlit_gsheets import GSheetsConnection
import datetime
import pandas as pd
import os

# 1. Estilo con Espaciado Corregido
st.set_page_config(page_title="Boda Joseline & Carlos", page_icon="💍", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@400;700&display=swap');

    .stApp {
        background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
        background-attachment: fixed;
    }
    
    /* ENCABEZADO: Separación de logo y nombres */
    .header-container { 
        text-align: center; 
        padding-top: 20px;
    }
    .logo-text {
        font-family: 'Great Vibes', cursive !important;
        color: #E6BE8A !important;
        font-size: 90px !important;
        text-shadow: 0px 0px 20px rgba(230, 190, 138, 0.6) !important;
        margin: 0 0 25px 0 !important; /* El tercer valor (25px) da el espacio abajo */
        line-height: 1.2 !important; /* Evita que se encimen las letras cursivas */
    }
    .names-text {
        font-family: 'Great Vibes', cursive !important;
        color: #D4AF37 !important;
        font-size: 60px !important;
        text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.4) !important;
        margin-top: 10px !important;
        line-height: 1 !important;
    }

    /* BOTONES: Alineación Perfecta en una línea */
    div[data-testid="stRadio"] > div[role="radiogroup"] {
        display: flex !important;
        justify-content: center !important;
        gap: 8px !important;
    }
    
    div[data-testid="stRadio"] label {
        background-color: rgba(212, 175, 55, 0.1) !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 30px !important;
        padding: 8px 5px !important; 
        color: white !important;
        flex: 1 !important;
        min-width: 95px !important;
        height: 45px !important; 
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }

    div[data-testid="stRadio"] label p {
        font-size: 18px !important;
        font-weight: bold !important;
        white-space: nowrap !important;
    }

    div[data-testid="stRadio"] input { display: none !important; }

    /* Estilos generales */
    h3, .stMarkdown, p {
        color: #F5F5F5 !important;
        text-align: center !important;
        font-family: 'Playfair Display', serif;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Lógica y Conexión
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
except:
    st.warning("Base de datos en modo lectura.")

# 3. Renderizado de Encabezado
st.markdown('''
    <div class="header-container">
        <p class="logo-text">C & J</p>
        <p class="names-text">Joseline & Carlos</p>
    </div>
    ''', unsafe_allow_html=True)

st.subheader("✨ Nuestra Mesa de Regalos Digital ✨")

# 4. Datos y Selección
DATA_REGALOS = {
    "$500": {"link": "https://mpago.li/2FdE5fx", "img": "gracias_500.png"},
    "$1,000": {"link": "https://mpago.li/2Zeechq", "img": "gracias_1000.png"},
    "$1,500": {"link": "https://mpago.li/2E5Rjr1", "img": "gracias_1500.png"}
}

monto = st.radio("Monto", options=["$500", "$1,000", "$1,500"], horizontal=True, label_visibility="collapsed")

if os.path.exists(DATA_REGALOS[monto]["img"]):
    st.image(DATA_REGALOS[monto]["img"], use_container_width=True)

# 5. Botón de Pago
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

# 6. Formulario
st.divider()
with st.form("libro_oro", clear_on_submit=True):
    nombre = st.text_input("Tu nombre:")
    mensaje = st.text_area("Tus deseos:")
    if st.form_submit_button("Enviar Mensaje ✨"):
        if nombre and mensaje:
            try:
                df_actual = conn.read()
                nueva_fila = pd.DataFrame([{"Fecha": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"), "Nombre": nombre, "Monto": monto, "Mensaje": mensaje}])
                df_final = pd.concat([df_actual, nueva_fila], ignore_index=True)
                conn.update(data=df_final)
                st.success("¡Mensaje guardado! ❤️")
                st.balloons()
            except:
                st.error("Error al guardar en la nube.")
