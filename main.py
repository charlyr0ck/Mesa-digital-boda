import streamlit as st
from streamlit_gsheets import GSheetsConnection
import datetime
import pandas as pd
import os

# 1. Configuración de Página y Estilo "Universal & Elegante"
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

    /* LIMITADOR DE ANCHO PARA WEB (Efecto Móvil en PC) */
    [data-testid="stAppViewBlockContainer"] {
        max-width: 600px !important;
        padding-top: 2rem !important;
        margin: auto !important;
    }
    
    /* ENCABEZADO: Dorado Champagne */
    .header-container { text-align: center; padding-top: 10px; }
    .logo-text {
        font-family: 'Great Vibes', cursive !important;
        color: #E6BE8A !important;
        font-size: 100px !important;
        text-shadow: 0px 0px 25px rgba(230, 190, 138, 0.6) !important;
        margin: 0 !important;
        line-height: 0.8 !important;
    }
    .names-text {
        font-family: 'Great Vibes', cursive !important;
        color: #D4AF37 !important;
        font-size: 65px !important;
        text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.4) !important;
        margin-top: 5px !important;
        line-height: 1 !important;
    }

    /* SECCIÓN DE BOTONES: Alineación Perfecta */
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
        cursor: pointer !important;
        transition: 0.3s ease !important;
    }

    /* Centrado del texto dentro de la cápsula */
    div[data-testid="stRadio"] label div[data-testid="stMarkdownContainer"] {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        height: 100% !important;
    }

    div[data-testid="stRadio"] label p {
        font-size: 20px !important;
        font-weight: bold !important;
        color: white !important;
        margin: 0 !important;
        line-height: 1 !important;
    }

    /* Ocultar círculo de radio nativo */
    div[data-testid="stRadio"] input {
        position: absolute !important;
        opacity: 0 !important;
        width: 0 !important;
    }
    
    /* Brillo al seleccionar */
    div[data-testid="stRadio"] label:has(input:checked) {
        background-color: rgba(212, 175, 55, 0.4) !important;
        box-shadow: 0px 0px 15px rgba(212, 175, 55, 0.5) !important;
    }

    /* Botón Dorado de Pago */
    .stButton>button {
        background: linear-gradient(90deg, #D4AF37 0%, #F4D03F 100%) !important;
        color: #090A0F !important;
        border-radius: 40px !important;
        font-weight: bold !important;
        height: 3.8em !important;
        font-size: 22px !important;
        border: none !important;
        width: 100% !important;
        box-shadow: 0px 5px 15px rgba(0,0,0,0.3) !important;
    }

    h3, .stMarkdown, p {
        color: #F5F5F5 !important;
        font-family: 'Playfair Display', serif;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Conexión Automática a Google Sheets
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
except Exception as e:
    st.error("Error al conectar con la base de datos.")

# 3. Encabezado
st.markdown('''
    <div class="header-container">
        <p class="logo-text">C & J</p>
        <p class="names-text">Joseline & Carlos</p>
    </div>
    ''', unsafe_allow_html=True)

st.subheader("✨ Nuestra Mesa de Regalos Digital ✨")
st.write("Tu presencia ilumina nuestro universo. Si deseas tener un detalle con nosotros, puedes elegir una de las opciones.")

# 4. Datos de Regalos
DATA_REGALOS = {
    "$500": {"link": "https://mpago.li/2FdE5fx", "img": "gracias_500.png"},
    "$1,000": {"link": "https://mpago.li/2Zeechq", "img": "gracias_1000.png"},
    "$1,500": {"link": "https://mpago.li/2E5Rjr1", "img": "gracias_1500.png"}
}

st.write("### 🎁 Elige el monto de tu regalo")
monto = st.radio("Seleccion", options=["$500", "$1,000", "$1,500"], horizontal=True, label_visibility="collapsed")

# Visualización de Tarjeta Centrada
if os.path.exists(DATA_REGALOS[monto]["img"]):
    st.image(DATA_REGALOS[monto]["img"], use_container_width=True)

# 5. Botón de Pago Mercado Pago
st.markdown(f'''
    <a href="{DATA_REGALOS[monto]["link"]}" target="_blank" style="text-decoration: none;">
        <div style="background: linear-gradient(90deg, #D4AF37 0%, #F4D03F 100%); 
                    color: #090A0F; padding: 20px; border-radius: 40px; 
                    text-align: center; font-weight: bold; font-size: 24px; 
                    margin: 15px 0px; box-shadow: 0px 8px 25px rgba(212, 175, 55, 0.4);">
            Regalar Tarjeta de {monto} 💳
        </div>
    </a>
    ''', unsafe_allow_html=True)

# 6. Formulario con Guardado Eterno en Google Sheets
st.divider()
st.subheader("✍️ Déjanos un mensaje en las estrellas")
with st.form("libro_oro", clear_on_submit=True):
    nombre = st.text_input("Tu nombre:")
    mensaje = st.text_area("Tus deseos para nosotros:")
    confirmar = st.form_submit_button("Enviar Mensaje ✨")

if confirmar:
    if nombre and mensaje:
        fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        try:
            # Leer datos actuales, añadir nueva fila y actualizar nube
            df_actual = conn.read()
            nueva_fila = pd.DataFrame([{"Fecha": fecha, "Nombre": nombre, "Monto": monto, "Mensaje": mensaje}])
            df_final = pd.concat([df_actual, nueva_fila], ignore_index=True)
            conn.update(data=df_final)
            
            st.success(f"¡Gracias {nombre}! Tu mensaje se ha guardado eternamente. ❤️")
            st.balloons()
        except:
            st.error("Hubo un problema al guardar el mensaje. Verifica los 'Secrets'.")
    else:
        st.error("Por favor, completa los campos para enviar tu mensaje.")

# 7. Acceso Privado (Para ver tu lista de regalos)
with st.expander("🔐 Panel de Control"):
    clave = st.text_input("Contraseña:", type="password")
    if clave == "Boda2026":
        try:
            df_ver = conn.read()
            st.dataframe(df_ver)
        except:
            st.info("Aún no hay mensajes registrados.")
