import streamlit as st
from streamlit_gsheets import GSheetsConnection
import datetime
import pandas as pd
import os

# 1. Estilo Visual con Espaciado y Diseño Responsive
st.set_page_config(page_title="Boda Joseline & Carlos", page_icon="💍", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@400;700&display=swap');

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
    
    /* ENCABEZADO: Separación optimizada */
    .header-container { 
        text-align: center; 
        padding: 20px 0;
    }
    .logo-text {
        font-family: 'Great Vibes', cursive !important;
        color: #E6BE8A !important;
        font-size: 100px !important;
        text-shadow: 0px 0px 25px rgba(230, 190, 138, 0.6) !important;
        margin: 0 0 20px 0 !important;
        line-height: 1.1 !important;
    }
    .names-text {
        font-family: 'Great Vibes', cursive !important;
        color: #D4AF37 !important;
        font-size: 65px !important;
        text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.4) !important;
        margin-top: 5px !important;
        line-height: 1 !important;
    }

    /* BOTONES: Alineación Perfecta */
    div[data-testid="stRadio"] > div[role="radiogroup"] {
        display: flex !important;
        justify-content: center !important;
        gap: 10px !important;
    }
    
    div[data-testid="stRadio"] label {
        background-color: rgba(212, 175, 55, 0.1) !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 30px !important;
        padding: 10px 15px !important; 
        color: white !important;
        flex: 1 !important;
        min-width: 90px !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        transition: 0.3s ease;
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

    /* Botón Dorado */
    .stButton>button {
        background: linear-gradient(90deg, #D4AF37 0%, #F4D03F 100%) !important;
        color: #090A0F !important;
        border-radius: 40px !important;
        font-weight: bold !important;
        height: 3.5em !important;
        font-size: 20px !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Conexión a Google Sheets
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
except:
    st.error("Error de conexión con la base de datos.")

# 3. Encabezado
st.markdown('''
    <div class="header-container">
        <p class="logo-text">C & J</p>
        <p class="names-text">Joseline & Carlos</p>
    </div>
    ''', unsafe_allow_html=True)

st.subheader("✨ Nuestra Mesa de Regalos Digital ✨")
st.write("Tu presencia ilumina nuestro universo. Si deseas tener un detalle con nosotros, puedes elegir una de las opciones.")

# 4. Datos y Selección de Regalo
DATA_REGALOS = {
    "Ninguna": {"link": None, "img": None},
    "$500": {"link": "https://mpago.li/2FdE5fx", "img": "gracias_500.png"},
    "$1,000": {"link": "https://mpago.li/2Zeechq", "img": "gracias_1000.png"},
    "$1,500": {"link": "https://mpago.li/2E5Rjr1", "img": "gracias_1500.png"}
}

st.write("### 🎁 Mesa de Regalos (Opcional)")
# Añadimos la opción "Ninguna" por defecto
monto = st.radio("Monto", options=["Ninguna", "$500", "$1,000", "$1,500"], horizontal=True, label_visibility="collapsed")

# Solo mostramos imagen y botón si eligen un monto
if monto != "Ninguna":
    if os.path.exists(DATA_REGALOS[monto]["img"]):
        st.image(DATA_REGALOS[monto]["img"], use_container_width=True)
    
    st.markdown(f'''
        <a href="{DATA_REGALOS[monto]["link"]}" target="_blank" style="text-decoration: none;">
            <div style="background: linear-gradient(90deg, #D4AF37 0%, #F4D03F 100%); 
                        color: #090A0F; padding: 18px; border-radius: 40px; 
                        text-align: center; font-weight: bold; font-size: 22px; 
                        margin: 15px 0px; box-shadow: 0px 8px 25px rgba(212, 175, 55, 0.4);">
                Regalar Tarjeta de {monto} 💳
            </div>
        </a>
        ''', unsafe_allow_html=True)
else:
    st.info("No has seleccionado ninguna tarjeta. ¡Igualmente puedes dejarnos un mensaje abajo! 👇")

# 5. Formulario de Mensajes (Funciona siempre)
st.divider()
st.subheader("✍️ Déjanos un mensaje en las estrellas")
with st.form("libro_oro", clear_on_submit=True):
    nombre = st.text_input("Tu nombre:")
    mensaje = st.text_area("Tus deseos para nosotros:")
    submit = st.form_submit_button("Enviar Mensaje ✨")

if submit:
    if nombre and mensaje:
        fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        monto_registro = monto if monto != "Ninguna" else "Solo mensaje"
        
        try:
            # Registrar en Google Sheets
            df_actual = conn.read()
            nueva_fila = pd.DataFrame([{"Fecha": fecha, "Nombre": nombre, "Monto": monto_registro, "Mensaje": mensaje}])
            df_final = pd.concat([df_actual, nueva_fila], ignore_index=True)
            conn.update(data=df_final)
            
            st.success(f"¡Gracias {nombre}! Tu mensaje ha sido enviado con éxito. ❤️")
            st.balloons()
        except:
            st.error("Lo sentimos, hubo un error al guardar tu mensaje.")
    else:
        st.error("Por favor, escribe tu nombre y un mensaje.")

# 6. Panel de Control
with st.expander("🔐 Panel de Control"):
    clave = st.text_input("Contraseña:", type="password")
    if clave == "Boda2026":
        try:
            df_ver = conn.read()
            st.dataframe(df_ver)
        except:
            st.info("Aún no hay mensajes.")
