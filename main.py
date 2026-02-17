import streamlit as st
import datetime
import os

# 1. Configuración y Estilo "Noche Estrellada & Dorado"
st.set_page_config(page_title="Boda Joseline & Carlos", page_icon="💍", layout="centered")
st.markdown("""
    <style>
    /* ... (tus estilos anteriores se mantienen) ... */

    /* NUEVO: Centrado absoluto para los botones de opción */
    [data-testid="stMarkdownContainer"] + div [role="radiogroup"] {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
        flex-wrap: wrap; /* Para que en pantallas pequeñas no se corten */
    }

    /* Estilo para que cada botón se vea como una cápsula dorada */
    div.stRadio [data-testid="stWidgetLabel"] {
        display: none; /* Escondemos el label interno para limpiar la vista */
    }
    
    div.stRadio label {
        background-color: rgba(212, 175, 55, 0.1) !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 20px !important;
        padding: 5px 15px !important;
        color: white !important;
        transition: 0.3s !important;
    }

    div.stRadio label:hover {
        border-color: #F4D03F !important;
        background-color: rgba(212, 175, 55, 0.2) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Encabezado con Logo
# Nota: Si subes un archivo de logo a GitHub llamado 'logo.png', puedes usar st.image('logo.png', width=150)
st.markdown('<div class="logo-container"><h1>C & J</h1></div>', unsafe_allow_html=True)
st.title("JOSELINE & CARLOS")
st.subheader("✨ Nuestra Mesa de Regalos Digital ✨")
st.write("Tu presencia ilumina nuestro universo. Si deseas tener un detalle con nosotros, puedes elegir una de las siguientes opciones.")

# 3. Datos de Regalos (Asegúrate de que los nombres coincidan con tus nuevos PNG)
DATA_REGALOS = {
    "$500": {"link": "https://mpago.li/2FdE5fx", "img": "gracias_500.png"},
    "$1,000": {"link": "https://mpago.li/2Zeechq", "img": "gracias_1000.png"},
    "$1,500": {"link": "https://mpago.li/2E5Rjr1", "img": "gracias_1500.png"}
}

# 4. Selección del Regalo
st.write("---")
st.write("### 🎁 Elige el monto de tu regalo")
monto = st.radio(
    "Selecciona una opción:",
    options=["$500", "$1,000", "$1,500"],
    horizontal=True,
    label_visibility="collapsed"
)

# Mostrar la tarjeta centrada y con tamaño controlado
col1, col2, col3 = st.columns([1, 2, 1])
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
                    color: #090A0F; padding: 15px; border-radius: 30px; 
                    text-align: center; font-weight: bold; font-size: 20px; 
                    margin: 10px 0px; box-shadow: 0px 4px 15px rgba(0,0,0,0.3);">
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
            st.info("Aún no hay mensajes.")
