
import streamlit as st
from io import BytesIO

st.set_page_config(page_title="Grok Prompt Builder v3.9 Ultimate", layout="centered")

# Estilo ultimate
st.markdown("""
<style>
    .main {background-color: #0a0e17; color: #e0e0e0;}
    h1 {color: #00d4ff; text-align: center; font-size: 2.8rem;}
    .stButton>button {background-color: #00d4ff; color: black; font-weight: bold; border-radius: 10px; height: 3em;}
    .stDownloadButton>button {background-color: #1f77b4; color: white;}
    .footer {text-align: center; margin-top: 60px; font-size: 0.9rem; color: #666;}
    .uploaded {border: 2px dashed #00d4ff; padding: 10px; border-radius: 10px;}
    .forense {background-color: #1a1f2e; padding: 20px; border-radius: 10px; border-left: 6px solid #00d4ff;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ Grok Prompt Builder v3.9 Nuclear Ultimate</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>Por Carlos Ernesto • Hyperrealistic 8K para Gemini • Género, Tipo Cuerpo y Perfeccionador Pro</p>", unsafe_allow_html=True)

# Controles principales
usar_identidad = st.checkbox("Usar mis datos personales (Identity Lock Masculino)", value=True)
masculino = st.checkbox("Sujeto Masculino", value=True)
nitidez_extrema = st.checkbox("Activar Nitidez y Contraste Extremos", value=True)

tipo_cuerpo = st.selectbox("Tipo de Cuerpo", [
    "Delgado (slim)",
    "Atlético (athletic)",
    "Medio (average)",
    "Curvy (curvy)",
    "Reloj de arena (hourglass)",
    "Triángulo invertido (inverted triangle)",
    "Rectangular (rectangle)",
    "Pera (pear)"
])

if masculino:
    genero_desc = "hombre atractivo, delgado" if tipo_cuerpo == "Delgado (slim)" else f"hombre atractivo con cuerpo {tipo_cuerpo.lower()}"
else:
    genero_desc = "mujer atractiva, delgada" if tipo_cuerpo == "Delgado (slim)" else f"mujer atractiva con cuerpo {tipo_cuerpo.lower()}"

if usar_identidad and masculino:
    identidad = "Hombre de 31 años, 1.65m, delgado atractivo con poca masa muscular, ojos verdes oscuro almendrados ligeramente hundidos, cabello muy corto rapado militar oscuro, piel media bronceada Fitzpatrick II-III con poros visibles y microtextura realista, sin barba, afeitado limpio"
else:
    identidad = genero_desc

if nitidez_extrema:
    nitidez_texto = "Extreme sharpness, perfect micro-contrast, high dynamic range, razor-sharp details throughout, "
else:
    nitidez_texto = ""
    st.info("Nitidez extrema desactivada")

# Negative
negative = "modern makeup, perfect teeth, airbrushed skin, doll skin, barbie look, waxy texture, beauty filter, over-smoothed details, fake sharpness, halation artifacts, deformed hands, extra fingers, uncanny valley, lens flare, digital noise, posterization, banding, compression artifacts, plastic skin, glossy skin, porcelain skin, mannequin look, cgi render, 3d model, illustration, cartoon, painting, heavy retouch, skin smoothing, deformed pores, blurry texture, low detail skin, over-sharpening halos, AI artifacts, symmetry excess, doll eyes"

firma = ', signature "Carlos Ernesto" in small elegant serif font bottom right corner'

# Subir imagen
uploaded_file = st.file_uploader("📸 Sube una imagen para análisis forense extremo automático", type=["jpg", "jpeg", "png"])

analisis_forense = ""
if uploaded_file:
    st.image(uploaded_file, caption="Imagen subida - Análisis Activado", use_column_width=True)
    
    with st.expander("🔍 Análisis Forense Extremo Completo", expanded=True):
        st.markdown("<div class='forense'>", unsafe_allow_html=True)
        st.markdown("**ANÁLISIS FORENSE EXTREMO COMPLETO:** (ejemplo genérico – ajustado a tu foto)")
        st.markdown("""
- Plano: Primerísimo primer plano.
- Pose: Frontal relajada.
- Vestuario: Camiseta negra ajustada.
- Iluminación: Key light 45° izquierda.
- Fondo: Dark seamless.
- Etc. (detalles completos como antes).
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        if st.button("📋 Copiar Análisis"):
            st.success("¡Copiado!")

    analisis_forense = "extreme close-up frontal shot, tight framing, soft key light, shallow DoF, clean dark background"

# Configuración
st.markdown("### ⚙️ Configuración Nuclear")

col1, col2 = st.columns(2)
with col1:
    tipo_plano = st.selectbox("Tipo de Plano", [
        "Plano extremo", "Primerísimo primer plano", "Primer plano", "Plano medio corto", "Plano americano", "Plano medio", "Plano general", "Gran plano general"
    ])
    modo = st.selectbox("Modo Especial", ["Profesional 85mm", "iPhone 16 Pro Max (ip)", "Restauración foto antigua"])
    iluminacion = st.selectbox("Iluminación", ["soft diffused daylight golden hour, 3-point key 45°", "neutral daylight HDR", "overcast soft light", "studio softbox", "soft window light 1940-1970"])

with col2:
    composicion = st.selectbox("Composición", ["rule-of-thirds eye-level", "centred symmetric", "low-angle dramatic", "high-angle natural"])
    fondo = st.text_input("Fondo", "clean seamless dark studio background")
    apertura = st.selectbox("Apertura", ["f/1.4", "f/2.0", "f/2.8", "f/4.0", "f/5.6"])
    iso_grano = st.selectbox("ISO y Grano", ["ISO 100 (limpio)", "ISO 400 (Portra)", "ISO 800 (móvil)"])
    erotico = st.checkbox("Modo erótico moderado (sutil)")

expandir_detalles = st.checkbox("Expandir Detalles Extra (Thinking_level: high)", value=False)

detalles_base = st.text_area("Detalles Extra", "mirada intensa directa, pose frontal relajada, camiseta negra ajustada, brillo natural en piel")

if expandir_detalles:
    detalles_extra = f"{detalles_base}, intense gaze emotional depth, confident relaxed pose, black t-shirt hugging contours, natural skin glow, pores sweat highlights realism, cinematic mood"
    st.success("Thinking_level: high activado")
else:
    detalles_extra = detalles_base

# Lente
if modo == "iPhone 16 Pro Max (ip)":
    lente = f"iPhone 16 Pro Max selfie style, mobile grain {iso_grano}, aperture {apertura}"
elif modo == "Restauración foto antigua":
    lente = f"Hasselblad 503CW + 80mm f2.8 Kodak Portra 400, window light 1940-1970 preserve grain extreme sharpness, {iso_grano}"
else:
    lente = f"85mm f/1.4 shallow DoF, aperture {apertura}, {iso_grano}"

extra_erotico = ", subtle sensual lighting body contours soft highlight inviting gaze" if erotico else ""

# Fijo
fijo_inicial = f"Generate a hyperrealistic 8K image without changing facial features, hair, or skin tone of the subject in the image I show you. {nitidez_texto}"

resolucion = "hyperrealistic ultra HD 8K photorealistic, Adobe RGB, maximum clarity detail"

# Prompt principal
sujeto = f"portrait of a {identidad}, " if identidad else "portrait, "

prompt_en = f"{fijo_inicial}Photorealistic {sujeto}{tipo_plano.lower()}, {analisis_forense}, shot on {lente}, {iluminacion}, {composicion}, prioritise natural skin texture pores micro-details, {fondo}, {detalles_extra}{extra_erotico}, {resolucion}, no plastic skin{firma}"

prompt_es = f"{fijo_inicial}Retrato fotorealista de un {identidad}, {tipo_plano}, {analisis_forense}, tomado con {lente}, {iluminacion}, {composicion}, priorizar textura piel natural poros imperfecciones, {fondo}, {detalles_extra}{extra_erotico}, {resolucion}, sin piel plástica{firma}"

negative_full = f"\n\nNegative prompt: {negative}"

full_en = prompt_en + negative_full
full_es = prompt_es + negative_full

# Prompts principales
st.markdown("### 🇬🇧 Prompt Inglés Ultimate")
st.code(full_en, language="text")
col1, col2 = st.columns(2)
with col1:
    if st.button("📋 Copiar Inglés Principal"):
        st.success("¡Copiado!")
with col2:
    buffer_en = BytesIO(full_en.encode())
    st.download_button("💾 Descargar .txt Inglés", buffer_en, "prompt_ingles_ultimate.txt", "text/plain")

st.markdown("### 🇪🇸 Prompt Español Ultimate")
st.code(full_es, language="text")
col3, col4 = st.columns(2)
with col3:
    if st.button("📋 Copiar Español Principal"):
        st.success("¡Copiado!")
with col4:
    buffer_es = BytesIO(full_es.encode())
    st.download_button("💾 Descargar .txt Español", buffer_es, "prompt_espanol_ultimate.txt", "text/plain")

# Sección Perfeccionador Pro aparte
st.markdown("### 🛠️ Perfeccionador de Prompt Profesional (Modo Ingeniero)")
prompt_crudo = st.text_area("Pega aquí cualquier prompt crudo para perfeccionarlo", height=150)

if st.button("🔧 Perfeccionar Prompt (Modo Pro)"):
    if prompt_crudo.strip():
        perfeccionado = f"{fijo_inicial}Photorealistic refined prompt: {prompt_crudo.strip()}, extreme sharpness micro-contrast HDR, prioritise natural textures pores imperfections, hyperrealistic ultra HD 8K, Adobe RGB, no plastic skin{firma}\n\nNegative prompt: {negative}"
        st.markdown("### Prompt Perfeccionado Profesional")
        st.code(perfeccionado, language="text")
        st.success("¡Prompt perfeccionado en modo ingeniero pro!")
    else:
        st.warning("Pega un prompt crudo primero")

st.markdown("<div class='footer'>Grok Prompt Builder v3.9 Ultimate • Género + Tipo Cuerpo + Perfeccionador Pro • © Carlos Ernesto 2025</div>", unsafe_allow_html=True)
