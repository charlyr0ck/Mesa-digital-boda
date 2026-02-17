st.markdown("""
    <style>
    /* ... (Mantenemos el resto del CSS anterior igual) ... */

    /* SECCIÓN DE BOTONES CORREGIDA */
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
        padding: 0 !important; /* Quitamos el padding para controlar el centro */
        color: white !important;
        flex: 1 !important;
        height: 50px !important; /* Altura fija para centrado vertical */
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        cursor: pointer !important;
    }

    /* Centrado del texto dentro de la etiqueta */
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
        padding: 0 !important;
        line-height: 1 !important;
    }

    /* Ocultar el círculo de selección por completo */
    div[data-testid="stRadio"] input {
        position: absolute !important;
        opacity: 0 !important;
        width: 0 !important;
        height: 0 !important;
    }
    
    /* Efecto cuando el botón está seleccionado */
    div[data-testid="stRadio"] label:has(input:checked) {
        background-color: rgba(212, 175, 55, 0.4) !important;
        box-shadow: 0px 0px 10px rgba(212, 175, 55, 0.5) !important;
    }
    </style>
    """, unsafe_allow_html=True)
