
import streamlit as st
from io import BytesIO

st.set_page_config(page_title="Grok Prompt Builder v25.0 Nuclear 2025", layout="centered")

# Estilo v25.0
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

st.markdown("<h1>Grok Prompt Builder v25.0 Nuclear Ultimate 2025</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>Por Carlos Ernesto - Prompts Cortos y Potentes (300-400 palabras)</p>", unsafe_allow_html=True)

# Texto fijo
TEXTO_FIJO = "Generate a hyperrealistic 8K image without changing facial features, hair, or skin tone of the subject in the image I show you. Firma en la parte inferior derecha de Carlos Ernesto. "

FIRMA = ', signature "Carlos Ernesto" in Cormorant Garamond Italic 48 pt, 78% opacity, pure white (#FFFFFF) on dark backgrounds / pure black (#000000) on light, positioned exactly 40 px from right edge and 40 px from bottom edge, drop shadow 15% opacity radius 2 px'

NEGATIVE = ("worst quality, lowres, blurry, out of focus, over-sharpening halos, fake sharpness, plastic skin, doll skin, airbrushed skin, waxy texture, beauty filter, over-smoothed details, halation artifacts, digital noise, posterization, banding, compression artifacts, deformed pores, low detail skin, uncanny valley, deformed hands, extra fingers, AI artifacts")

# Fórmula Nuclear corta (ON por defecto)
FORMULA_NUCLEAR = ("Ultra photorealistic 8K museum-grade portrait, 1000% identity lock no drift, extreme sharpness razor-sharp micro-details perfect micro-contrast high dynamic range, rich deep blacks bright vibrant highlights cinematic contrast curve no dull tones, prioritise natural skin texture visible pores realistic imperfections, shot on Canon RF 85mm f/1.2 L USM at f/2.8, soft diffused golden hour 3-point lighting, rule of thirds eye-level, ultra HD 8K maximum clarity detail Adobe RGB vibrant rich colors")

# Identity lock (sin tatuajes)
IDENTIDAD_LOCK = ("Exact same person, 31 years old, 1.65m, lean slim body, flat stomach, narrow shoulders, long slim arms, long legs, visible thigh gap. Face: rectangular, strong square jaw, high cheekbones, straight medium nose, thin lips. Eyes: dark green almond shape, slightly hooded. Eyebrows: thick dark straight. Hair: military buzzcut dark brown, receding temples sharp widow's peak. Skin: Fitzpatrick II-III, visible pores, subtle freckles, two small moles left cheekbone right jawline. Always clean-shaven, neutral expression, direct gaze.")

# ===============================
# PROMPT PRINCIPAL
# ===============================

st.markdown("### Prompt Principal")

nitidez_main = st.checkbox("Nitidez extrema (principal)", value=True)
contraste_main = st.checkbox("Contraste extremo (principal)", value=True)
lock_main = st.checkbox("Identity lock (principal)", value=True)
formula_main = st.checkbox("Fórmula Nuclear base (principal)", value=True)

if lock_main:
    identidad_main = IDENTIDAD_LOCK
else:
    masculino_main = st.checkbox("Sujeto Masculino (principal)", value=True)
    cuerpo_main = st.selectbox("Cuerpo (principal)", ["Delgado (slim)", "Atlético (athletic)", "Medio (average)", "Curvy (curvy)", "Reloj de arena (hourglass)", "Triángulo invertido (inverted triangle)", "Rectangular (rectangle)", "Pera (pear)"])
    cuerpo_str = cuerpo_main.lower().replace(' (slim)', '').replace(' (athletic)', '').replace(' (average)', '').replace(' (curvy)', '').replace(' (hourglass)', '').replace(' (inverted triangle)', '').replace(' (rectangle)', '').replace(' (pear)', '')
    identidad_main = f"attractive man with {cuerpo_str} body" if masculino_main else f"attractive woman with {cuerpo_str} body"

col1, col2 = st.columns(2)
with col1:
    plano_main = st.selectbox("Plano (principal)", [
        "Plano extremo (face 95-100% height, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
        "Primer plano (head to clavicle, face 90% height, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
        "Plano medio (top head to mid-torso, subject 75% height, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
        "Plano completo (full body head to toe + space feet, --ar 9:16, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)"
    ])
    lente_main = st.selectbox("Lente (principal)", [
        "Canon RF 85mm f/1.2 L USM @ f/2.8",
        "Sony FE 85mm f/1.4 GM @ f/2.8",
        "iPhone 16 Pro Max main, simulated f/1.6"
    ])
with col2:
    iluminacion_main = st.selectbox("Iluminación (principal)", [
        "soft diffused golden hour 3-point",
        "neutral daylight HDR",
        "studio softbox high-CRI"
    ])

prioridad_main = st.text_area("Prioridad (principal)", value="", height=80)
prioridad_final_main = f"(PRIORITISE WITH MAXIMUM RESPONSIBILITY: {prioridad_main.upper()})" if prioridad_main.strip() else ""

detalles_main = st.text_area("Detalles extra + fondo (principal)", value="", height=120, placeholder="Ej: camiseta negra ajustada, fondo playa atardecer")

fondo_main = detalles_main if "fondo" in detalles_main.lower() else "clean seamless dark studio background"

nitidez_contraste_main = "extreme sharpness razor-sharp micro-details perfect micro-contrast high dynamic range rich deep blacks bright vibrant highlights cinematic contrast curve no dull tones, " if nitidez_main and contraste_main else ""

base_main = FORMULA_NUCLEAR if formula_main else "Hyperrealistic 8K portrait, extreme sharpness high dynamic range, "

prompt_en_main = f"{TEXTO_FIJO}{base_main}{nitidez_contraste_main}{identidad_main}, {plano_main}, shot on {lente_main}, {iluminacion_main}, prioritise natural skin texture visible pores realistic imperfections, {fondo_main}, {detalles_main}, ultra HD 8K maximum clarity detail Adobe RGB vibrant rich colors, {prioridad_final_main}, {FIRMA}"

full_en_main = prompt_en_main + f"\n\nNegative prompt: {NEGATIVE}"

st.markdown("### Prompt Principal")
st.code(full_en_main, language="text")
if st.button("Copiar Principal"):
    st.markdown(f"<script>navigator.clipboard.writeText(`{full_en_main}`);</script>", unsafe_allow_html=True)
    st.success("Prompt Principal copiado!")

# ===============================
# PERFECCIONADOR INDEPENDIENTE
# ===============================

st.markdown('<div class="perfeccionador-block">', unsafe_allow_html=True)
st.markdown('<h2 class="perfeccionador-title">Perfeccionador Independiente (Prompt 2)</h2>', unsafe_allow_html=True)

nitidez_perf = st.checkbox("Nitidez extrema (perfeccionador)", value=True)
contraste_perf = st.checkbox("Contraste extremo (perfeccionador)", value=True)
formula_perf = st.checkbox("Fórmula Nuclear base (perfeccionador)", value=True)

nitidez_contraste_perf = "extreme sharpness razor-sharp micro-details perfect micro-contrast high dynamic range rich deep blacks bright vibrant highlights cinematic contrast curve no dull tones, " if nitidez_perf and contraste_perf else ""

plano_perf = st.selectbox("Plano (perfeccionador)", [
    "Plano extremo (face 95-100% height, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
    "Primer plano (head to clavicle, face 90% height, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
    "Plano medio (top head to mid-torso, subject 75% height, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
    "Plano completo (full body head to toe + space feet, --ar 9:16, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)"
])

lente_perf = st.selectbox("Lente (perfeccionador)", [
    "Canon RF 85mm f/1.2 L USM @ f/2.8",
    "Sony FE 85mm f/1.4 GM @ f/2.8",
    "iPhone 16 Pro Max main, simulated f/1.6"
])

iluminacion_perf = st.selectbox("Iluminación (perfeccionador)", [
    "soft diffused golden hour 3-point",
    "neutral daylight HDR",
    "studio softbox high-CRI"
])

prioridad_perf = st.text_area("Prioridad (perfeccionador)", value="", height=80)
prioridad_final_perf = f"(PRIORITISE WITH MAXIMUM RESPONSIBILITY: {prioridad_perf.upper()})" if prioridad_perf.strip() else ""

detalles_perf = st.text_area("Detalles extra + fondo (perfeccionador)", value="", height=120, placeholder="Ej: camiseta negra ajustada, fondo playa atardecer")

fondo_perf = detalles_perf if "fondo" in detalles_perf.lower() else "clean seamless dark studio background"

prompt_crudo = st.text_area("Prompt crudo a perfeccionar", height=150, placeholder="Ej: un hombre mirando a cámara...")

if st.button("Generar 2do Prompt Independiente"):
    if prompt_crudo.strip():
        base_perf = FORMULA_NUCLEAR if formula_perf else "Hyperrealistic 8K portrait, extreme sharpness high dynamic range, "
        prompt_perf = f"{TEXTO_FIJO}{base_perf}{nitidez_contraste_perf}{prompt_crudo.strip()}, {plano_perf}, shot on {lente_perf}, {iluminacion_perf}, prioritise natural skin texture visible pores realistic imperfections, {fondo_perf}, {detalles_perf}, ultra HD 8K maximum clarity detail Adobe RGB vibrant rich colors, {prioridad_final_perf}, {FIRMA}"
        full_perf = prompt_perf + f"\n\nNegative prompt: {NEGATIVE}"
        st.code(full_perf, language="text")
        st.markdown(f"<script>navigator.clipboard.writeText(`{full_perf}`);</script>", unsafe_allow_html=True)
        st.success("2do Prompt independiente copiado!")
    else:
        st.warning("Pega un prompt crudo")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div class='footer'>Grok Prompt Builder v25.0 Nuclear Ultimate 2025 - Prompts Cortos y Potentes - (c) Carlos Ernesto 2025</div>", unsafe_allow_html=True)
