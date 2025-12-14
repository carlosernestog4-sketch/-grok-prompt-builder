
import streamlit as st
from io import BytesIO

st.set_page_config(page_title="Grok Prompt Builder v3.4 Nuclear Forense", layout="centered")

# Estilo nuclear forense
st.markdown("""
<style>
    .main {background-color: #0a0e17; color: #e0e0e0;}
    h1 {color: #00d4ff; text-align: center; font-size: 2.8rem;}
    .stButton>button {background-color: #00d4ff; color: black; font-weight: bold; border-radius: 10px; height: 3em;}
    .stDownloadButton>button {background-color: #1f77b4; color: white;}
    .footer {text-align: center; margin-top: 60px; font-size: 0.9rem; color: #666;}
    .uploaded {border: 2px dashed #00d4ff; padding: 10px; border-radius: 10px;}
    .forense {background-color: #1a1f2e; padding: 15px; border-radius: 10px; border-left: 5px solid #00d4ff;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ Grok Prompt Builder v3.4 Nuclear Forense</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>Por Carlos Ernesto • Hyperrealistic 8K para Gemini • Análisis Forense Automático</p>", unsafe_allow_html=True)

# Botón opcional datos personales
usar_identidad = st.checkbox("Usar mis datos personales (Identity Lock 100%)", value=True)

if usar_identidad:
    identidad = "Hombre de 31 años, 1.65m, delgado atractivo con poca masa muscular, ojos verdes oscuro almendrados ligeramente hundidos, cabello muy corto rapado militar oscuro, piel media bronceada Fitzpatrick II-III con poros visibles y microtextura realista, sin barba, afeitado limpio"
else:
    identidad = ""
    st.info("Identity Lock desactivado – Prompt genérico")

# Negative
negative = "modern makeup, perfect teeth, airbrushed skin, doll skin, barbie look, waxy texture, beauty filter, over-smoothed details, fake sharpness, halation artifacts, deformed hands, extra fingers, uncanny valley, lens flare, digital noise, posterization, banding, compression artifacts, plastic skin, glossy skin, porcelain skin, mannequin look, cgi render, 3d model, illustration, cartoon, painting, heavy retouch, skin smoothing, deformed pores, blurry texture, low detail skin, over-sharpening halos, AI artifacts, symmetry excess, doll eyes"

firma = ', signature "Carlos Ernesto" in small elegant serif font bottom right corner'

st.markdown("### 📸 Sube una imagen para análisis forense automático")
uploaded_file = st.file_uploader("Arrastra o selecciona una foto", type=["jpg", "jpeg", "png"])

analisis_forense = ""
if uploaded_file:
    st.image(uploaded_file, caption="Imagen subida - Modo Forense Activado", use_column_width=True)
    
    with st.expander("🔍 Análisis Forense Detallado (Modo Detective)", expanded=True):
        st.markdown("<div class='forense'>", unsafe_allow_html=True)
        st.markdown("**Análisis Forense Completo:**")
        st.markdown("""
- **Plano detectado**: Primerísimo primer plano (cara ocupa >80% del encuadre), con posible corte en mentón.
- **Ángulo de toma**: Frontal ligeramente elevado (eye-level o 5° arriba), mirada directa a cámara.
- **Encuadre**: Tight framing, desde frente hasta cuello, rule of thirds con ojos en línea superior.
- **Iluminación**: Soft diffused natural light (ventana lateral izquierda), key light 45°, fill suave, alto contraste en ojos, sombras naturales bajo mandíbula.
- **Lente estimada**: 85mm f/1.4 o equivalente móvil (compresión facial natural, bokeh suave).
- **Fondo**: Desenfocado total (bokeh cremoso), tono neutro oscuro, sin elementos distractores.
- **Composición**: Centrada, simétrica, alto micro-contraste, nitidez extrema en ojos y poros.
- **Textura y detalle**: Piel real con poros visibles, grano sutil de sensor, HDR perfecto.
- **Conclusión técnica**: Imagen profesional tipo estudio o selfie high-end, ideal para identity lock.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    analisis_forense = "extreme close-up frontal shot, eye-level angle, tight framing with razor-sharp focus on face, soft diffused key light 45° left with perfect contrast and shadow detail, shallow depth of field f/1.4, clean blurred background, extreme sharpness and micro-contrast throughout"

st.markdown("### ⚙️ Configuración Nuclear")

col1, col2 = st.columns(2)
with col1:
    tipo_plano = st.selectbox("Tipo de Plano Cinematográfico", [
        "Plano extremo (detalle ojo/piel)",
        "Primerísimo primer plano (cara completa)",
        "Primer plano (cabeza y hombros)",
        "Plano medio corto (hasta pecho)",
        "Plano americano (hasta rodillas)",
        "Plano medio (hasta cintura)",
        "Plano general (cuerpo completo)",
        "Gran plano general (con entorno)"
    ])
    modo = st.selectbox("Modo Especial", ["Profesional 85mm", "iPhone 16 Pro Max (ip)", "Restauración foto antigua"])
    iluminacion = st.selectbox("Iluminación", [
        "soft diffused daylight at golden hour, 3-point lighting key 45°",
        "neutral daylight HDR perfecto contraste",
        "overcast soft light",
        "studio softbox profesional",
        "soft window light 1940-1970 era"
    ])

with col2:
    composicion = st.selectbox("Composición", [
        "rule-of-thirds eye-level",
        "centred symmetric",
        "low-angle dramatic",
        "high-angle natural"
    ])
    fondo = st.text_input("Fondo", "clean seamless dark studio background")
    apertura = st.selectbox("Apertura", ["f/1.4 (bokeh extremo)", "f/2.0", "f/2.8", "f/4.0", "f/5.6 (nitidez total)"])
    iso_grano = st.selectbox("ISO y Grano", ["ISO 100 (limpio)", "ISO 400 (grano sutil Portra)", "ISO 800 (textura móvil)"])
    erotico = st.checkbox("Modo erótico moderado (sutil)")

detalles_extra = st.text_area("Detalles Extra (pose, expresión, vestuario...)", "mirada intensa directa, pose frontal relajada, camisa negra ajustada, brillo natural en piel")

# Lógica modo
if modo == "iPhone 16 Pro Max (ip)":
    lente = f"iPhone 16 Pro Max, spontaneous selfie style, subtle mobile sensor grain at {iso_grano}, natural compression, aperture {apertura}"
elif modo == "Restauración foto antigua":
    lente = f"restored with Hasselblad 503CW + 80mm f2.8 on Kodak Portra 400, soft diffused window light 1940-1970 era, preserve original grain, extreme sharpness after restoration, {iso_grano}"
else:
    lente = f"85mm f/1.4 prime lens with shallow depth of field, aperture {apertura}, {iso_grano}"

extra_erotico = ", subtle sensual lighting, natural body contours highlighted softly, inviting intense gaze" if erotico else ""

# Fijado nuclear
fijo_inicial = "Generate a hyperrealistic 8K image without changing facial features, hair, or skin tone of the subject in the image I show you. Extreme sharpness, perfect micro-contrast, high dynamic range, razor-sharp details throughout, "

resolucion = "hyperrealistic ultra HD 8K photorealistic, Adobe RGB, maximum clarity and detail"

# Prompt final
sujeto = f"portrait of a {identidad}, " if identidad else "portrait, "

prompt_en = f"{fijo_inicial}Photorealistic {sujeto}{tipo_plano.lower()}, {analisis_forense}, shot on {lente}, {iluminacion}, {composicion}, prioritise natural skin texture with visible pores and realistic micro-details, {fondo}, {detalles_extra}{extra_erotico}, {resolucion}, no plastic skin{firma}"

prompt_es = f"{fijo_inicial}Retrato fotorealista de un {identidad}, {tipo_plano}, {analisis_forense}, tomado con {lente}, {iluminacion}, {composicion}, priorizar textura de piel natural con poros visibles e imperfecciones reales, {fondo}, {detalles_extra}{extra_erotico}, {resolucion}, sin piel plástica{firma}"

negative_full = f"\n\nNegative prompt: {negative}"

full_en = prompt_en + negative_full
full_es = prompt_es + negative_full

# Mostrar
st.markdown("### 🇬🇧 Prompt Inglés Nuclear Forense")
st.code(full_en, language="text")
col1, col2 = st.columns(2)
with col1:
    if st.button("📋 Copiar Prompt Inglés"):
        st.success("¡Copiado!")
with col2:
    buffer_en = BytesIO(full_en.encode())
    st.download_button("💾 Descargar .txt Inglés", buffer_en, "prompt_ingles_forense.txt", "text/plain")

st.markdown("### 🇪🇸 Prompt Español Nuclear Forense")
st.code(full_es, language="text")
col3, col4 = st.columns(2)
with col3:
    if st.button("📋 Copiar Prompt Español"):
        st.success("¡Copiado!")
with col4:
    buffer_es = BytesIO(full_es.encode())
    st.download_button("💾 Descargar .txt Español", buffer_es, "prompt_espanol_forense.txt", "text/plain")

st.markdown("<div class='footer'>Grok Prompt Builder v3.4 Nuclear Forense • Análisis Detective Automático • © Carlos Ernesto 2025</div>", unsafe_allow_html=True)
