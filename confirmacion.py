import streamlit as st

# 1. Configuración de Estilo "Noche Estrellada Minimalista"
st.set_page_config(page_title="Confirmación - Joseline & Carlos", page_icon="📅", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@400;700&display=swap');

    .stApp {
        background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
        background-attachment: fixed;
    }
    
    [data-testid="stAppViewBlockContainer"] {
        max-width: 500px !important;
        margin: auto !important;
    }
    
    .header-container { text-align: center; padding-bottom: 20px; }
    .logo-text {
        font-family: 'Great Vibes', cursive !important;
        color: #E6BE8A !important;
        font-size: 100px !important;
        margin: 0 !important;
        line-height: 1.1 !important;
    }
    .names-text {
        font-family: 'Great Vibes', cursive !important;
        color: #D4AF37 !important;
        font-size: 65px !important;
    }

    .form-label {
        color: #D4AF37 !important;
        font-family: 'Playfair Display', serif;
        font-weight: bold;
        display: block;
        margin-top: 20px;
        text-align: left;
    }
    
    .form-input {
        width: 100%;
        padding: 12px;
        margin-bottom: 10px;
        border-radius: 12px;
        border: 1px solid #D4AF37;
        background: rgba(255, 255, 255, 0.05);
        color: white;
    }
    
    .form-button {
        background: linear-gradient(90deg, #D4AF37 0%, #F4D03F 100%);
        color: #090A0F;
        border: none;
        padding: 18px;
        border-radius: 40px;
        font-weight: bold;
        font-size: 20px;
        width: 100%;
        cursor: pointer;
        margin-top: 30px;
        box-shadow: 0px 5px 15px rgba(212, 175, 55, 0.3);
    }

    h3, p {
        color: #F5F5F5 !important;
        text-align: center !important;
        font-family: 'Playfair Display', serif;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Encabezado
st.markdown('''
    <div class="header-container">
        <p class="names-text">Nos casamos</p>
        <p class="names-text">Joseline & Carlos</p>
    </div>
    ''', unsafe_allow_html=True)

st.subheader("📅 Confirmación de Asistencia")
st.write("Es un honor para nosotros que nos acompañes en este día tan especial.")
# 3. Formulario Simplificado (Limpiado de indentación para evitar el cuadro de texto)
ID_FORMSPREE_RSVP = "xqedlwwn" 

form_html = f"""
<form action="https://formspree.io/f/{ID_FORMSPREE_RSVP}" method="POST">
<label class="form-label">Tu Nombre:</label>
<input type="text" name="Nombre_Invitado" class="form-input" placeholder="Escribe tu nombre aquí" required>
<label class="form-label">¿Contamos con tu presencia?</label>
<select name="Asistencia" class="form-input" style="background: #1B2735; color: white; display: block; width: 100%;">
<option value="Confirmado">¡Ahí estaré! ✨</option>
<option value="Declinado">Lamentablemente no podré ir</option>
</select>
<button type="submit" class="form-button">Confirmar Asistencia 🥂</button>
</form>
"""

# Usamos unsafe_allow_html=True para que se ejecute el código
st.markdown(form_html, unsafe_allow_html=True)

# --- ENLACE A MESA DE REGALOS ---
st.divider()
st.write("### 🎁 ¿Deseas ver nuestra mesa de regalos?")
st.write("Si quieres tener un detalle con nosotros, puedes visitar nuestra mesa digital haciendo clic abajo:")

# REEMPLAZA ESTE LINK con la URL de tu aplicación de Mesa de Regalos en Streamlit Cloud
LINK_MESA_REGALOS = "https://tu-app-de-regalos.streamlit.app"

st.markdown(f'''
    <a href="{LINK_MESA_REGALOS}" target="_blank" style="text-decoration: none;">
        <div style="background-color: rgba(212, 175, 55, 0.2); 
                    color: #D4AF37; 
                    padding: 15px; 
                    border-radius: 30px; 
                    text-align: center; 
                    font-weight: bold; 
                    border: 2px solid #D4AF37;
                    transition: 0.3s;">
            Ver Mesa de Regalos 💍
        </div>
    </a>
    ''', unsafe_allow_html=True)
