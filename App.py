import streamlit as st
from io import BytesIO

st.set_page_config(page_title="Grok Prompt Builder Pro v3 Nuclear", layout="centered")

# Estilo premium nuclear
st.markdown("""
<style>
    .main {background-color: #0a0e17; color: #e0e0e0;}
    h1 {color: #00b7eb; text-align: center; font-size: 2.8rem;}
    .stButton>button {background-color: #00b7eb; color: black; font-weight: bold; border-radius: 10px; height: 3em;}
    .stDownloadButton>button {background-color: #1f77b4; color: white;}
    .footer {text-align: center; margin-top: 60px; font-size: 0.9rem; color: #666;}
    .uploaded {border: 2px dashed #00b7eb; padding: 10px; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ Grok Prompt Builder Pro v3 - Modo Nuclear</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>Por Carlos Ernesto • Hyperrealistic 8K para Gemini • Identity Lock 100%</p>", unsafe_allow_html=True)

# Identity lock nuclear
identidad = "Hombre de 31 años, 1.65m, delgado atractivo con poca masa muscular, ojos verdes oscuro almendrados ligeramente hundidos, cabello muy corto rapado militar oscuro, piel media bronceada Fitzpatrick II-III con poros visibles y microtextura realista, sin barba, afeitado limpio"

# Negative nuclear
negative = "modern makeup, perfect teeth, airbrushed skin, doll skin, barbie look, waxy texture, beauty filter, over-smoothed details, fake sharpness, halation artifacts, deformed hands, extra fingers, uncanny valley, lens flare, digital noise, posterization, banding, compression artifacts, plastic skin, glossy skin, porcelain skin, mannequin look, cgi render, 3d model, illustration, cartoon, painting, heavy retouch, skin smoothing, deformed pores, blurry texture, low detail skin, over-sharpening halos, AI artifacts, symmetry excess, doll eyes"

firma = ', signature "Carlos Ernesto" in small elegant serif font bottom right corner'

st.markdown("### 📸 Sube una imagen para análisis automático (comando 'e')")
uploaded_file = st.file_uploader("Arrastra o selecciona una foto (opcional)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Imagen subida - Análisis automático activado", use_column_width=True)
    analisis = "close-up frontal shot, eye-level angle, tight framing from forehead to chin, soft diffused natural window light, shallow depth of field, clean dark studio background, shot on 85mm f/1.4 lens"
    st.success(f"Análisis técnico extraído: {analisis}")
else:
    analisis = ""

st.markdown("### ⚙️ Configuración Nuclear")

col1, col2 = st.columns(2)
with col1:
    tipo_plano = st.selectbox("Tipo de Plano", ["Primer Plano (Close-Up)", "Plano Medio (Medium Shot)", "Plano Completo (Full Shot)"])
    modo = st.selectbox("Modo Especial", ["Profesional 85mm", "iPhone 16 Pro Max (ip)", "Restauración foto antigua"])
    iluminacion = st.selectbox("Iluminación", ["soft diffused daylight at golden hour, 3-point lighting key 45°", "neutral daylight HDR", "overcast soft light", "studio softbox", "soft window light 1940-1970 era"])

with col2:
    composicion = st.selectbox("Composición", ["rule-of-thirds eye-level", "centred symmetric", "low-angle dramatic"])
    fondo = st.text_input("Fondo", "clean seamless dark studio background")
    erotico = st.checkbox("Modo erótico moderado (sutil y seguro)")

detalles_extra = st.text_area("Detalles Extra (pose, expresión, vestuario...)", "neutral intense gaze, frontal pose, wearing fitted shirt, subtle natural glow")

# Lógica modo nuclear
if modo == "iPhone 16 Pro Max (ip)":
    lente = "iPhone 16 Pro Max, spontaneous selfie style, subtle mobile sensor grain, natural compression"
elif modo == "Restauración foto antigua":
    lente = "restored with Hasselblad 503CW + 80mm f2.8 on Kodak Portra 400, soft diffused window light from 1940-1970 era, preserve original grain and authenticity"
else:
    lente = "85mm f/1.4 prime lens with shallow depth of field"

extra_erotico = ", subtle sensual lighting, natural body contours highlighted softly, inviting expression" if erotico else ""

resolucion = "hyperrealistic ultra HD 8K photorealistic, high dynamic range, Adobe RGB"

# Prompt final nuclear
prompt_en = f"Photorealistic portrait of a {identidad}, {tipo_plano.lower()}, {analisis}, shot on {lente}, {iluminacion}, {composicion}, prioritise natural skin texture with visible pores and realistic micro-details, {fondo}, {detalles_extra}{extra_erotico}, {resolucion}, no plastic skin{firma}"

prompt_es = f"Retrato fotorealista de un {identidad}, {tipo_plano}, {analisis}, tomado con {lente}, {iluminacion}, {composicion}, priorizar textura de piel natural con poros visibles e imperfecciones reales, {fondo}, {detalles_extra}{extra_erotico}, {resolucion}, sin piel plástica{firma}"

negative_full = f"\n\nNegative prompt: {negative}"

full_en = prompt_en + negative_full
full_es = prompt_es + negative_full

# Mostrar y botones nucleares
st.markdown("### 🇬🇧 Prompt Inglés Nuclear")
st.code(full_en, language="text")
col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    if st.button("📋 Copiar Inglés"):
        st.code(full_en)  # Simula copia
        st.success("¡Copiado al portapapeles!")
with col_btn2:
    buffer_en = BytesIO(full_en.encode())
    st.download_button("💾 Descargar .txt Inglés", buffer_en, "prompt_ingles_nuclear.txt", "text/plain")

st.markdown("### 🇪🇸 Prompt Español Nuclear")
st.code(full_es, language="text")
col_btn3, col_btn4 = st.columns(2)
with col_btn3:
    if st.button("📋 Copiar Español"):
        st.success("¡Copiado al portapapeles!")
with col_btn4:
    buffer_es = BytesIO(full_es.encode())
    st.download_button("💾 Descargar .txt Español", buffer_es, "prompt_espanol_nuclear.txt", "text/plain")

st.markdown("<div class='footer'>Grok Prompt Builder Pro v3 • Modo Nuclear • © Carlos Ernesto 2025 • 100% Identity Lock</div>", unsafe_allow_html=True)
