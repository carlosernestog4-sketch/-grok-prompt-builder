
import streamlit as st
from io import BytesIO

st.set_page_config(page_title="Grok Prompt Builder v5.0 Pro 2025", layout="centered")

# Estilo nuclear pro
st.markdown("""
<style>
    .main {background-color: #0a0e17; color: #e0e0e0;}
    h1 {color: #00d4ff; text-align: center; font-size: 2.8rem;}
    .stButton>button {background-color: #00d4ff; color: black; font-weight: bold; border-radius: 10px; height: 3em;}
    .stDownloadButton>button {background-color: #1f77b4; color: white;}
    .footer {text-align: center; margin-top: 60px; font-size: 0.9rem; color: #666;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ Grok Prompt Builder v5.0 Nuclear Pro 2025</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>Por Carlos Ernesto • Hyperrealistic 8K Gemini 2025 • Identity Lock Extremo</p>", unsafe_allow_html=True)

# Controles principales
usar_identidad = st.checkbox("Usar mis datos personales (Identity Lock 100%)", value=True)
masculino = st.checkbox("Sujeto Masculino", value=True)
nitidez_extrema = st.checkbox("Activar Nitidez y Contraste Extremos (recomendado ON)", value=True)

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

aspect_ratio = st.selectbox("Aspect Ratio (Gemini 2025)", ["1:1", "9:16 (vertical)", "16:9 (horizontal)", "3:4", "4:3"])

if masculino:
    genero_desc = "hombre atractivo, delgado" if tipo_cuerpo == "Delgado (slim)" else f"hombre atractivo con cuerpo {tipo_cuerpo.lower()}"
else:
    genero_desc = "mujer atractiva, delgada" if tipo_cuerpo == "Delgado (slim)" else f"mujer atractiva con cuerpo {tipo_cuerpo.lower()}"

if usar_identidad and masculino:
    identidad = "Hombre de 31 años, 1.65m, delgado atractivo con poca masa muscular, ojos verdes oscuro almendrados ligeramente hundidos, cabello muy corto rapado militar oscuro, piel media bronceada Fitzpatrick II-III con poros visibles y microtextura realista, sin barba, afeitado limpio"
else:
    identidad = genero_desc

nitidez_texto = "Extreme sharpness, perfect micro-contrast, high dynamic range, razor-sharp details throughout, " if nitidez_extrema else ""

# Negative pro 2025
negative = "modern makeup, perfect teeth, airbrushed skin, doll skin, barbie look, waxy texture, beauty filter, over-smoothed details, fake sharpness, halation artifacts, deformed hands, extra fingers, uncanny valley, lens flare, digital noise, posterization, banding, compression artifacts, plastic skin, glossy skin, porcelain skin, mannequin look, cgi render, 3d model, illustration, cartoon, painting, heavy retouch, skin smoothing, deformed pores, blurry texture, low detail skin, over-sharpening halos, AI artifacts, AI glow, exaggerated highlights, symmetry excess, doll eyes"

firma = ', signature "Carlos Ernesto" in small elegant serif font bottom right corner'

# Configuración Nuclear
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
    erotico = st.checkbox("Modo erótico moderado (sutil 2025)")

# Detalles Extra Pro 2025
st.markdown("### ✨ Detalles Extra Pro (Thinking_level: high - recomendado ON)")
expandir_detalles = st.checkbox("Activar Detalles Extra Pro", value=True)

detalles_base = st.text_area(
    "Detalles Extra (base)",
    value="mirada intensa directa, pose frontal relajada, camiseta negra ajustada, brillo natural en piel",
    height=100,
    help="Al activar Pro se upsamples con capas 2025: emotional depth, pores, identity lock extremo..."
)

if expandir_detalles:
    detalles_final = (
        f"{detalles_base}, "
        "intense emotional depth confident direct gaze, relaxed natural pose, "
        "black t-shirt hugging subtle contours, natural skin glow with visible pores subtle sweat highlights micro-wrinkles fabric grain, "
        "cinematic serene mood, razor-sharp micro-details, "
        "100% facial identity lock no drift preserve exact proportions eye shape hairline skin undertones, "
        "prioritise natural imperfections realistic textures high dynamic range"
    )
    if erotico:
        detalles_final += ", subtle sensual soft lighting on skin contours inviting warm atmosphere"
    st.success("✅ Detalles Pro ACTIVADOS – Máximo realismo Gemini 2025 (+50% consistency)")
else:
    detalles_final = detalles_base
    st.info("Detalles básicos – Activa Pro para resultados nucleares")

# Lente
if modo == "iPhone 16 Pro Max (ip)":
    lente = f"iPhone 16 Pro Max selfie style, mobile grain {iso_grano}, aperture {apertura}"
elif modo == "Restauración foto antigua":
    lente = f"Hasselblad 503CW + 80mm f2.8 Kodak Portra 400, window light 1940-1970 preserve grain extreme sharpness, {iso_grano}"
else:
    lente = f"85mm f/1.4 shallow DoF, aperture {apertura}, {iso_grano}"

# Fijo inicial + resolución
fijo_inicial = f"Generate a hyperrealistic 8K image without changing facial features, hair, or skin tone of the subject. {nitidez_texto}"
resolucion = f"hyperrealistic ultra HD 8K photorealistic, Adobe RGB, maximum clarity detail, aspect ratio {aspect_ratio}"

# Prompt reordenado óptimo 2025
sujeto = f"portrait of a {identidad}, " if identidad else "portrait, "

prompt_en = f"{fijo_inicial} Photorealistic {sujeto}{tipo_plano.lower()}, shot on {lente}, {iluminacion}, {composicion}, prioritise natural skin texture pores micro-details realistic imperfections, {fondo}, {detalles_final}, {resolucion}, no plastic skin{firma}"

prompt_es = f"{fijo_inicial} Retrato fotorealista de un {identidad}, {tipo_plano}, tomado con {lente}, {iluminacion}, {composicion}, priorizar textura piel natural poros imperfecciones realistas, {fondo}, {detalles_final}, {resolucion}, sin piel plástica{firma}"

negative_full = f"\n\nNegative prompt: {negative}"

full_en = prompt_en + negative_full
full_es = prompt_es + negative_full

# Salida
st.markdown("### 🇬🇧 Prompt Inglés Nuclear Pro 2025")
st.code(full_en, language="text")
col1, col2 = st.columns(2)
with col1:
    if st.button("📋 Copiar Inglés"):
        st.success("¡Copiado!")
with col2:
    buffer_en = BytesIO(full_en.encode())
    st.download_button("💾 Descargar .txt Inglés", buffer_en, "prompt_ingles_pro2025.txt", "text/plain")

st.markdown("### 🇪🇸 Prompt Español Nuclear Pro 2025")
st.code(full_es, language="text")
col3, col4 = st.columns(2)
with col3:
    if st.button("📋 Copiar Español"):
        st.success("¡Copiado!")
with col4:
    buffer_es = BytesIO(full_es.encode())
    st.download_button("💾 Descargar .txt Español", buffer_es, "prompt_espanol_pro2025.txt", "text/plain")

# Perfeccionador
st.markdown("### 🛠️ Perfeccionador de Prompt Profesional 2025")
prompt_crudo = st.text_area("Pega aquí cualquier prompt crudo para perfeccionarlo", height=150)

if st.button("🔧 Perfeccionar Prompt"):
    if prompt_crudo.strip():
        perfeccionado = f"{fijo_inicial} Photorealistic refined prompt 2025: {prompt_crudo.strip()}, extreme sharpness micro-contrast HDR, prioritise natural textures pores imperfections realistic skin, hyperrealistic ultra HD 8K, Adobe RGB, 100% identity lock no drift, no plastic skin{firma}\n\nNegative prompt: {negative}"
        st.code(perfeccionado, language="text")
        st.success("¡Prompt perfeccionado nuclear 2025!")
    else:
        st.warning("Pega un prompt primero")

st.markdown("<div class='footer'>Grok Prompt Builder v5.0 Nuclear Pro 2025 • Gemini Optimized • © Carlos Ernesto 2025</div>", unsafe_allow_html=True)
