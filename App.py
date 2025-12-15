
import streamlit as st
from io import BytesIO

st.set_page_config(page_title="Grok Prompt Builder v26.0 Nuclear 2025", layout="centered")

# Estilo v26.0
st.markdown("""
<style>
    .main {background-color: #0a0e17; color: #e0e0e0;}
    h1 {color: #00d4ff; text-align: center; font-size: 2.8rem;}
    .stButton>button {background-color: #00d4ff; color: black; font-weight: bold; border-radius: 10px; height: 3em;}
    .stDownloadButton>button {background-color: #1f77b4; color: white;}
    .footer {text-align: center; margin-top: 60px; font-size: 0.9rem; color: #666;}
    .perfeccionador-block {
        background-color: #001f3f;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #00d4ff;
        margin-top: 40px;
    }
    .perfeccionador-title {
        color: #00ffff;
        font-size: 1.8rem;
        text-align: center;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>Grok Prompt Builder v26.0 Nuclear Ultimate 2025</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>Por Carlos Ernesto - Prompts Ultra-Cortos (400-500 chars) + Sin Repeticiones</p>", unsafe_allow_html=True)

# Texto fijo
TEXTO_FIJO_INICIO = "Generate a hyperrealistic 8K image without changing facial features, hair, or skin tone of the subject in the image I show you. Firma en la parte inferior derecha de Carlos Ernesto. "

# Firma
FIRMA = ', signature "Carlos Ernesto" bottom right'

# Negative corto
NEGATIVE = "lowres, blurry, fake sharpness, halation, plastic skin, airbrushed, doll skin, waxy texture, over-smoothed, digital noise, posterization, banding, compression artifacts, uncanny valley, deformed hands, extra fingers, deformed pores, low detail skin, over-sharpening halos, AI artifacts"

# Fórmula ultra-corta (base para todos)
FORMULA_ULTRA = "Ultra photorealistic 8K, extreme sharpness razor-sharp micro-details perfect micro-contrast high dynamic range, cinematic lighting rich blacks bright highlights, natural skin texture visible pores subtle imperfections, shot on Canon RF 85mm f/2.8, 3-point lighting, rule of thirds eye-level, clean dark background, maximum clarity Adobe RGB vibrant colors"

# Identity lock corto
IDENTIDAD_LOCK = "Exact same person, 31yo slim man 1.65m, rectangular face strong jaw high cheekbones, dark green almond eyes, thick dark eyebrows, short military buzzcut dark brown, Fitzpatrick II-III skin visible pores two moles, clean-shaven neutral expression direct gaze"

# ===============================
# PROMPT PRINCIPAL
# ===============================

st.markdown("### Prompt Principal")

nitidez_main = st.checkbox("Nitidez extrema (principal)", value=True)
contraste_main = st.checkbox("Contraste cinematic (principal)", value=True)
lock_main = st.checkbox("Identity lock (principal)", value=True)

tipo_plano_main = st.selectbox("Plano (principal)", [
    "Extreme close-up face 95-100% height mid-forehead to chin STRICTLY CROP NO DEVIATION",
    "Close-up head to clavicle face 90% height STRICTLY CROP NO DEVIATION",
    "Medium close-up head to waist 70-80% height STRICTLY CROP NO DEVIATION",
    "Medium shot head to mid-torso 75% height STRICTLY CROP NO DEVIATION",
    "Full body head to toe + space feet --ar 9:16 STRICTLY CROP NO DEVIATION"
])

lente_main = st.selectbox("Lente (principal)", [
    "Canon RF 85mm f/1.8", "Canon RF 85mm f/2.8", "Canon RF 50mm f/4", "Canon RF 35mm f/5.6",
    "Sony FE 85mm f/1.8", "Sony FE 50mm f/4", "Sony FE 35mm f/5.6", "iPhone 16 Pro Max main 1x f/1.6"
])

prioridad_main = st.text_area("Prioridad (principal)", value="", height=80)
prioridad_final_main = f"(PRIORITISE WITH MAXIMUM RESPONSIBILITY: {prioridad_main.upper()})" if prioridad_main.strip() else ""

detalles_main = st.text_area("Detalles extra (principal)", value="", height=120, placeholder="Ej: camiseta negra ajustada, fondo playa atardecer")

fondo_main = detalles_main if "fondo" in detalles_main.lower() else "clean seamless dark studio background"

identidad_main = IDENTIDAD_LOCK if lock_main else "attractive slim man"

prompt_main = f"{TEXTO_FIJO_INICIO}{FORMULA_ULTRA} {identidad_main}, {tipo_plano_main}, shot on {lente_main}, {detalles_main}, {fondo_main}, {prioridad_final_main}{FIRMA}"

full_main = prompt_main + f"\n\nNegative prompt: {NEGATIVE}"

st.markdown("### Prompt Principal")
st.code(full_main, language="text")
col1, col2 = st.columns(2)
with col1:
    if st.button("Copiar Principal"):
        st.markdown(f"<script>navigator.clipboard.writeText(`{full_main}`);</script>", unsafe_allow_html=True)
        st.success("Prompt principal copiado!")
with col2:
    buffer_main = BytesIO(full_main.encode())
    st.download_button("Descargar .txt Principal", buffer_main, "prompt_principal_v26.0.txt", "text/plain")

# ===============================
# PERFECCIONADOR INDEPENDIENTE
# ===============================

st.markdown('<div class="perfeccionador-block">', unsafe_allow_html=True)
st.markdown('<h2 class="perfeccionador-title">Perfeccionador Independiente (2do Prompt)</h2>', unsafe_allow_html=True)

nitidez_perf = st.checkbox("Nitidez extrema (perfeccionador)", value=True)
contraste_perf = st.checkbox("Contraste cinematic (perfeccionador)", value=True)

tipo_plano_perf = st.selectbox("Plano (perfeccionador)", [
    "Extreme close-up face 95-100% height mid-forehead to chin STRICTLY CROP NO DEVIATION",
    "Close-up head to clavicle face 90% height STRICTLY CROP NO DEVIATION",
    "Medium close-up head to waist 70-80% height STRICTLY CROP NO DEVIATION",
    "Medium shot head to mid-torso 75% height STRICTLY CROP NO DEVIATION",
    "Full body head to toe + space feet --ar 9:16 STRICTLY CROP NO DEVIATION"
])

lente_perf = st.selectbox("Lente (perfeccionador)", [
    "Canon RF 85mm f/1.8", "Canon RF 85mm f/2.8", "Canon RF 50mm f/4", "Canon RF 35mm f/5.6",
    "Sony FE 85mm f/1.8", "Sony FE 50mm f/4", "Sony FE 35mm f/5.6", "iPhone 16 Pro Max main 1x f/1.6"
])

prioridad_perf = st.text_area("Prioridad (perfeccionador)", value="", height=80)
prioridad_final_perf = f"(PRIORITISE WITH MAXIMUM RESPONSIBILITY: {prioridad_perf.upper()})" if prioridad_perf.strip() else ""

detalles_perf = st.text_area("Detalles extra (perfeccionador)", value="", height=120, placeholder="Ej: mirada intensa, fondo playa atardecer")

fondo_perf = detalles_perf if "fondo" in detalles_perf.lower() else "clean seamless dark studio background"

prompt_crudo = st.text_area("Prompt crudo a perfeccionar", height=120, placeholder="Ej: hombre mirando a cámara...")

if st.button("Generar 2do Prompt"):
    if prompt_crudo.strip():
        prompt_perf = f"{TEXTO_FIJO_INICIO}{FORMULA_ULTRA} {prompt_crudo.strip()}, {tipo_plano_perf}, shot on {lente_perf}, {detalles_perf}, {fondo_perf}, {prioridad_final_perf}{FIRMA}"
        full_perf = prompt_perf + f"\n\nNegative prompt: {NEGATIVE}"
        st.code(full_perf, language="text")
        st.markdown(f"<script>navigator.clipboard.writeText(`{full_perf}`);</script>", unsafe_allow_html=True)
        st.success("2do prompt copiado!")
    else:
        st.warning("Pega un prompt crudo")

st.markdown('</div>', unsafe_allow_html=True)

# Restauracion corta
if st.button("Restauracion Nuclear"):
    restauracion = f"{TEXTO_FIJO_INICIO}Museum-grade 8K restoration: remove dust scratches fading, preserve grain, sharpen micro-details, recover dynamic range, re-photographed Canon R5 RF 85mm soft window light, 1000% identity lock, {FIRMA}"
    st.code(restauracion + f"\n\nNegative prompt: {NEGATIVE}", language="text")

st.markdown("<div class='footer'>Grok Prompt Builder v26.0 Nuclear Ultimate 2025 - Prompts Ultra-Cortos 400-500 chars - (c) Carlos Ernesto 2025</div>", unsafe_allow_html=True)
