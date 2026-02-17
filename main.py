import streamlit as st
from streamlit_gsheets import GSheetsConnection
import datetime
import pandas as pd

# 1. Configuración y Estilo (Manteniendo tu diseño dorado)
st.set_page_config(page_title="Boda Joseline & Carlos", page_icon="💍", layout="centered")

# --- (Aquí va todo tu bloque de CSS anterior que ya perfeccionamos) ---
# [He omitido el bloque largo de CSS por brevedad, pero mantenlo en tu archivo]

# 2. Conexión Automática a Google Sheets
# Nota: Debes configurar la URL en los 'Secrets' de Streamlit Cloud
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df_existente = conn.read(worksheet="Sheet1")
except:
    df_existente = pd.DataFrame(columns=["Fecha", "Nombre", "Monto", "Mensaje"])

# 3. Encabezado
st.markdown('''
    <div class="header-container">
        <p class="logo-text">J&C</p>
        <p class="names-text">Joseline & Carlos</p>
    </div>
    ''', unsafe_allow_html=True)

# 4. Datos de Regalos
DATA_REGALOS = {
    "$500": {"link": "https://mpago.li/2FdE5fx", "img": "gracias_500.png"},
    "$1,000": {"link": "https://mpago.li/2Zeechq", "img": "gracias_1000.png"},
    "$1,500": {"link": "https://mpago.li/2E5Rjr1", "img": "gracias_1500.png"}
}

monto = st.radio("Seleccion", options=["$500", "$1,000", "$1,500"], horizontal=True, label_visibility="collapsed")

# ... (Bloque de imagen y botón de pago) ...

# 5. Libro de Mensajes 100% Automático
st.divider()
st.subheader("✍️ Déjanos un mensaje en las estrellas")

with st.form("libro_oro", clear_on_submit=True):
    nombre = st.text_input("Tu nombre:")
    mensaje = st.text_area("Tus deseos para nosotros:")
    confirmar = st.form_submit_button("Enviar Mensaje ✨")

if confirmar:
    if nombre and mensaje:
        fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        
        # Crear nueva fila
        nueva_fila = pd.DataFrame([{
            "Fecha": fecha,
            "Nombre": nombre,
            "Monto": monto,
            "Mensaje": mensaje
        }])
        
        # Actualizar Google Sheets de forma automática
        df_actualizado = pd.concat([df_existente, nueva_fila], ignore_index=True)
        conn.update(worksheet="Sheet1", data=df_actualizado)
        
        st.success("¡Mensaje guardado eternamente en nuestra lista! ❤️")
        st.balloons()
    else:
        st.error("Por favor, completa los campos.")

# 6. Panel Privado (Solo para ver la tabla)
with st.expander("🔐 Panel de Control"):
    clave = st.text_input("Contraseña:", type="password")
    if clave == "Boda2026":
        st.write("### 📜 Lista de Mensajes en Tiempo Real")
        st.dataframe(df_existente) # Muestra la tabla de Google Sheets directamente
