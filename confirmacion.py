import streamlit as st

# 1. Configuración de Estilo "Noche Estrellada RSVP"
st.set_page_config(page_title="RSVP - Joseline & Carlos", page_icon="📅", layout="centered")

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

    /* Limitador de ancho para mantener estética de invitación móvil */
    [data-testid="stAppViewBlockContainer"] {
        max-width: 550px !important;
        padding-top: 2rem !important;
        margin: auto !important;
    }
    
    .header-container { text-align: center; padding-bottom: 20px; }
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
        line-height: 1 !important;
    }

    /* Estilo del Formulario RSVP */
    .form-label {
        color: #D4AF37;
        font-family: 'Playfair Display', serif;
        font-weight: bold;
        margin-bottom: 8px;
        display: block;
        text-align: left;
    }
    
    .form-input {
        width: 100%;
        padding: 12px;
        margin-bottom: 20px;
        border-radius: 12px;
        border: 1px solid #D4AF37;
        background: rgba(255, 255, 255, 0.05);
        color: white;
        font-size: 16px;
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
        box-shadow: 0px 5px 15px rgba(212, 175, 55, 0.3);
        margin-top: 10px;
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
        <p class="logo-text">C & J</p>
        <p class="names-text">Joseline & Carlos</p>
    </div>
    ''', unsafe_allow_html=True)

st.subheader("📅 Confirmación de Asistencia")
st.write("Nos llena de alegría saber que nos acompañarán. Por favor, completen el formulario para asegurar su lugar.")

# 3. Formulario RSVP - Integración con Formspree
# RECOMIENDO: Usa un ID de Formspree nuevo para esta app
ID_FORMSPREE_RSVP = "TU_NUEVO_ID_AQUÍ" 

form_html = f"""
    <form action="https://formspree.io/f/{ID_FORMSPREE_RSVP}" method="POST">
        <label class="form-label">Nombre del Invitado Principal:</label>
        <input type="text" name="Nombre_Invitado" class="form-input" placeholder="Ej. Juan Pérez" required>
        
        <label class="form-label">¿Contamos con tu presencia?</label>
        <select name="Asistencia" class="form-input" style="background: #1B2735; color: white;">
            <option value="Confirmado">¡Ahí estaremos! ✨</option>
            <option value="Declinado">Lamentablemente no podremos ir</option>
        </select>
        
        <button type="submit" class="form-button">Confirmar Asistencia 🥂</button>
    </form>
"""

st.markdown(form_html, unsafe_allow_html=True)

st.divider()
st.caption("Al confirmar, los datos se enviarán directamente a nuestra lista de invitados.")
