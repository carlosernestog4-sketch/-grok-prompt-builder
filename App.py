
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
st.markdown("<p style='text-align: center; color: #aaa;'>Por Carlos Ernesto - Prompts Cortos (~300-400 palabras) + Resumen Automático</p>", unsafe_allow_html=True)

# Texto fijo al inicio
TEXTO_FIJO_INICIO = "Generate a hyperrealistic 8K image without changing facial features, hair, or skin tone of the subject in the image I show you. Firma en la parte inferior derecha de Carlos Ernesto. "

# Firma obligatoria
FIRMA_OBLIGATORIA = ', signature "Carlos Ernesto" in Cormorant Garamond Italic 48 pt, 78% opacity, pure white (#FFFFFF) on dark backgrounds / pure black (#000000) on light, positioned exactly 40 px from right edge and 40 px from bottom edge, drop shadow 15% opacity radius 2 px'

# Negative nuclear (corto)
NEGATIVE_NUCLEAR = "worst quality, low quality, lowres, blurry, out of focus, fake sharpness, halation artifacts, plastic skin, airbrushed skin, doll skin, waxy texture, beauty filter, over-smoothed details, digital noise, posterization, banding, compression artifacts, uncanny valley, deformed hands, extra fingers, deformed pores, low detail skin, over-sharpening halos, AI artifacts"

# FORMULA NUCLEAR CORTA (para ~300-400 palabras)
FORMULA_NUCLEAR_CORTA = ("Ultra photorealistic 8K portrait, 1000% identity lock no drift, extreme sharpness razor-sharp micro-details perfect micro-contrast high dynamic range, cinematic lighting with rich deep blacks bright highlights, natural skin texture visible pores subtle imperfections, shot on Canon EOS R5 Mark II + RF 85mm f/1.2 at f/2.8, 3-point lighting key 45° fill 2:1 rim, rule of thirds eye-level, clean seamless dark background, maximum clarity Adobe RGB vibrant colors")

# Identity lock (corto, sin tatuajes)
IDENTIDAD_LOCK = ("Exact same person, 31 years old, 1.65m, slim lean body, rectangular face, strong jaw high cheekbones, dark green eyes almond shape, thick dark eyebrows, short military buzzcut dark brown, Fitzpatrick II-III skin visible pores subtle freckles two small moles, clean-shaven, neutral expression direct gaze")

# ===============================
# PROMPT PRINCIPAL
# ===============================

st.markdown("### Prompt Principal")

# Checkboxes principales (Fórmula Nuclear corta ON por defecto)
nitidez_extrema_main = st.checkbox("Activar nitidez extrema profesional (principal)", value=True)
contraste_extremo_main = st.checkbox("Activar contraste extremo profesional (principal)", value=True)
usar_lock_absoluto_main = st.checkbox("Activar IDENTIDAD LOCK ABSOLUTO v7 (principal)", value=True)

nitidez_texto_main = "extreme sharpness razor-sharp micro-details perfect micro-contrast high dynamic range, " if nitidez_extrema_main else ""
contraste_color_texto_main = "rich deep blacks bright vibrant highlights cinematic contrast curve, " if contraste_extremo_main else ""

# Identidad principal
if usar_lock_absoluto_main:
    identidad_main = IDENTIDAD_LOCK
else:
    masculino_main = st.checkbox("Sujeto Masculino (principal)", value=True)
    tipo_cuerpo_main = st.selectbox("Tipo de Cuerpo (principal)", ["Delgado (slim)", "Atlético (athletic)", "Medio (average)", "Curvy (curvy)", "Reloj de arena (hourglass)", "Triángulo invertido (inverted triangle)", "Rectangular (rectangle)", "Pera (pear)"])
    cuerpo_str_main = tipo_cuerpo_main.lower().replace(' (slim)', '').replace(' (athletic)', '').replace(' (average)', '').replace(' (curvy)', '').replace(' (hourglass)', '').replace(' (inverted triangle)', '').replace(' (rectangle)', '').replace(' (pear)', '')
    identidad_main = f"attractive man with {cuerpo_str_main} body" if masculino_main else f"attractive woman with {cuerpo_str_main} body"

# Configuración principal
col1_main, col2_main = st.columns(2)
with col1_main:
    tipo_plano_main = st.selectbox("Tipo de Plano (principal)", [
        "Plano extremo (face 95-100% height, extreme close-up crop mid-forehead to chin, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
        "Primerisimo primer plano (face 95-100% height, extreme close-up crop mid-forehead to chin, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
        "Primer plano (head to just below clavicle, face 90% height, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
        "Plano medio corto (top of head to waist, subject 70-80% height, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
        "Plano americano (top of head to waist, subject 70-80% height, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
        "Plano medio (top of head to mid-torso, subject 75% height, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
        "Plano general (full body head to toe + 10-15 cm space for feet, --ar 9:16, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
        "Gran plano general (full body head to toe + 10-15 cm space for feet, --ar 9:16, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)"
    ])
    lente_main = st.selectbox("Lente (principal)", [
        "Canon RF 85mm f/1.2 L USM @ f/1.8 (primer plano extremo)",
        "Canon RF 85mm f/1.2 L USM @ f/2.8 (retrato clasico)",
        "Canon RF 50mm f/1.2 L USM @ f/4 (plano medio)",
        "Canon RF 35mm f/1.4 L USM @ f/5.6 (plano completo)",
        "Sony FE 85mm f/1.4 GM @ f/1.8",
        "Sony FE 50mm f/1.2 GM @ f/4",
        "Sony FE 35mm f/1.4 GM @ f/5.6",
        "iPhone 16 Pro Max 48MP main 1x, simulated f/1.6, Dolby Vision HDR"
    ])
    iluminacion_main = st.selectbox("Iluminacion Profesional (principal)", [
        "3-point + rim + hair light: 120cm octabox key 45 degree + silver fill 2:1 + 30cm stripbox rim + hair light top-back, all 5600K CRI 98+",
        "soft diffused daylight golden hour wrap-around",
        "neutral daylight HDR",
        "overcast soft light",
        "studio softbox high-CRI",
        "soft window light 1940-1970 vintage"
    ])

with col2_main:
    composicion_main = st.selectbox("Composicion (principal)", ["rule of thirds golden ratio eye-level, subject 75% height (85% full body)", "centred symmetric", "low-angle dramatic", "high-angle natural"])

# Prioridad principal
prioridad_texto_main = st.text_area("Prioridad (principal)", value="", height=100)
prioridad_final_main = f"(PRIORITISE WITH MAXIMUM RESPONSIBILITY: {prioridad_texto_main.upper()})" if prioridad_texto_main.strip() else ""

# Detalles extra principal
expandir_detalles_main = st.checkbox("Activar Detalles Extra Pro (principal)", value=False)
detalles_base_main = st.text_area("Detalles Extra base (principal)", value="", height=150, placeholder="Ej: mirada intensa directa, camiseta negra ajustada, fondo oscuro con luces bokeh")

detalles_final_main = detalles_base_main + ", intense emotional depth natural asymmetry visible pores micro-imperfections cinematic mood razor-sharp details" if expandir_detalles_main else detalles_base_main

fondo_final_main = detalles_base_main if "fondo" in detalles_base_main.lower() else "clean seamless dark studio background with subtle gradient"

sujeto_final_main = f"photorealistic portrait of {identidad_main}, "

prompt_en_main = f"{TEXTO_FIJO_INICIO}{FORMULA_NUCLEAR_CORTA} {nitidez_texto_main}{contraste_color_texto_main}{sujeto_final_main}{tipo_plano_main}, shot on {lente_main}, {iluminacion_main}, {composicion_main}, natural skin texture visible pores micro-details realistic imperfections, {fondo_final_main}, {detalles_final_main}, ultra HD 8K maximum clarity Adobe RGB vibrant colors, {prioridad_final_main}, {FIRMA_OBLIGATORIA}"

full_en_main = prompt_en_main + f"\n\nNegative prompt: {NEGATIVE_NUCLEAR}"

# Resumen automático principal
resumen_main = f"""
**Resumen Prompt Principal:**
- Plano: {tipo_plano_main.split(' (')[0]}
- Lente: {lente_main}
- Iluminación: {iluminacion_main.split(':')[0] if ':' in iluminacion_main else iluminacion_main}
- Composición: {composicion_main}
- Fondo: {fondo_final_main}
- Prioridad: {prioridad_texto_main if prioridad_texto_main else 'Ninguna'}
- Detalles extra: {detalles_final_main if detalles_final_main else 'Ninguno'}
"""

# Salida principal
st.markdown("### Prompt Principal Ingles")
st.code(full_en_main, language="text")
st.markdown(resumen_main)

col1, col2 = st.columns(2)
with col1:
    if st.button("Copiar Ingles (principal)"):
        st.markdown(f"<script>navigator.clipboard.writeText(`{full_en_main}`);</script>", unsafe_allow_html=True)
        st.success("Prompt Ingles (principal) copiado al portapapeles!")
with col2:
    buffer_en_main = BytesIO(full_en_main.encode())
    st.download_button("Descargar .txt Ingles (principal)", buffer_en_main, "prompt_principal_ingles_v25.0.txt", "text/plain")

# ===============================
# PERFECCIONADOR INDEPENDIENTE
# ===============================

st.markdown('<div class="perfeccionador-block">', unsafe_allow_html=True)
st.markdown('<h2 class="perfeccionador-title">Perfeccionador de Prompt Profesional (Totalmente Independiente)</h2>', unsafe_allow_html=True)

nitidez_extrema_perf = st.checkbox("Activar nitidez extrema profesional (perfeccionador)", value=True)
contraste_extremo_perf = st.checkbox("Activar contraste extremo profesional (perfeccionador)", value=True)

nitidez_texto_perf = "extreme sharpness razor-sharp micro-details perfect micro-contrast high dynamic range, " if nitidez_extrema_perf else ""
contraste_color_texto_perf = "rich deep blacks bright vibrant highlights cinematic contrast curve, " if contraste_extremo_perf else ""

tipo_plano_perf = st.selectbox("Tipo de Plano (perfeccionador)", [
    "Plano extremo (face 95-100% height, extreme close-up crop mid-forehead to chin, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
    "Primerisimo primer plano (face 95-100% height, extreme close-up crop mid-forehead to chin, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
    "Primer plano (head to just below clavicle, face 90% height, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
    "Plano medio corto (top of head to waist, subject 70-80% height, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
    "Plano americano (top of head to waist, subject 70-80% height, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
    "Plano medio (top of head to mid-torso, subject 75% height, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
    "Plano general (full body head to toe + 10-15 cm space for feet, --ar 9:16, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)",
    "Gran plano general (full body head to toe + 10-15 cm space for feet, --ar 9:16, STRICTLY CROP EXACTLY AS SPECIFIED, NO DEVIATION)"
])

lente_perf = st.selectbox("Lente (perfeccionador)", [
    "Canon RF 85mm f/1.2 L USM @ f/1.8 (primer plano extremo)",
    "Canon RF 85mm f/1.2 L USM @ f/2.8 (retrato clasico)",
    "Canon RF 50mm f/1.2 L USM @ f/4 (plano medio)",
    "Canon RF 35mm f/1.4 L USM @ f/5.6 (plano completo)",
    "Sony FE 85mm f/1.4 GM @ f/1.8",
    "Sony FE 50mm f/1.2 GM @ f/4",
    "Sony FE 35mm f/1.4 GM @ f/5.6",
    "iPhone 16 Pro Max 48MP main 1x, simulated f/1.6, Dolby Vision HDR"
])

iluminacion_perf = st.selectbox("Iluminacion Profesional (perfeccionador)", [
    "3-point + rim + hair light: 120cm octabox key 45 degree + silver fill 2:1 + 30cm stripbox rim + hair light top-back, all 5600K CRI 98+",
    "soft diffused daylight golden hour wrap-around",
    "neutral daylight HDR",
    "overcast soft light",
    "studio softbox high-CRI",
    "soft window light 1940-1970 vintage"
])

composicion_perf = st.selectbox("Composicion (perfeccionador)", ["rule of thirds golden ratio eye-level, subject 75% height (85% full body)", "centred symmetric", "low-angle dramatic", "high-angle natural"])

prioridad_texto_perf = st.text_area("Prioridad (perfeccionador)", value="", height=100)
prioridad_final_perf = f"(PRIORITISE WITH MAXIMUM RESPONSIBILITY: {prioridad_texto_perf.upper()})" if prioridad_texto_perf.strip() else ""

expandir_detalles_perf = st.checkbox("Activar Detalles Extra Pro (perfeccionador)", value=False)
detalles_base_perf = st.text_area("Detalles Extra base (perfeccionador)", value="", height=150, placeholder="Ej: mirada intensa directa, camiseta negra ajustada, fondo oscuro con luces bokeh")

detalles_final_perf = detalles_base_perf + ", intense emotional depth natural asymmetry visible pores micro-imperfections cinematic mood razor-sharp details" if expandir_detalles_perf else detalles_base_perf

fondo_final_perf = detalles_base_perf if "fondo" in detalles_base_perf.lower() else "clean seamless dark studio background with subtle gradient"

prompt_crudo = st.text_area("Prompt crudo a perfeccionar", height=150, placeholder="Ej: un hombre mirando a cámara...")

if st.button("Generar 2do Prompt (Totalmente Diferente)"):
    if prompt_crudo.strip():
        prompt_perfeccionado_en = f"{TEXTO_FIJO_INICIO}{FORMULA_NUCLEAR_CORTA} {nitidez_texto_perf}{contraste_color_texto_perf}{prioridad_final_perf}{prompt_crudo.strip()}, {tipo_plano_perf}, shot on {lente_perf}, {iluminacion_perf}, {composicion_perf}, natural skin texture visible pores micro-details realistic imperfections, {fondo_final_perf}, {detalles_final_perf}, ultra HD 8K maximum clarity Adobe RGB vibrant colors, {FIRMA_OBLIGATORIA}"
        full_perfeccionado_en = prompt_perfeccionado_en + f"\n\nNegative prompt: {NEGATIVE_NUCLEAR}"

        # Resumen automático perfeccionador
        resumen_perf = f"""
**Resumen 2do Prompt:**
- Plano: {tipo_plano_perf.split(' (')[0]}
- Lente: {lente_perf}
- Iluminación: {iluminacion_perf.split(':')[0] if ':' in iluminacion_perf else iluminacion_perf}
- Composición: {composicion_perf}
- Fondo: {fondo_final_perf}
- Prioridad: {prioridad_texto_perf if prioridad_texto_perf else 'Ninguna'}
- Detalles extra: {detalles_final_perf if detalles_final_perf else 'Ninguno'}
"""

        st.code(full_perfeccionado_en, language="text")
        st.markdown(resumen_perf)
        st.markdown(f"<script>navigator.clipboard.writeText(`{full_perfeccionado_en}`);</script>", unsafe_allow_html=True)
        st.success("2do Prompt (independiente) copiado al portapapeles!")
    else:
        st.warning("Pega un prompt crudo primero")

st.markdown('</div>', unsafe_allow_html=True)

# Restauracion
if st.button("Generar Plantilla Restauracion Nuclear v7"):
    restauracion_nuclear = (
        f"{TEXTO_FIJO_INICIO}"
        "Museum-grade restoration of this damaged historical photograph to 8K 16-bit: surgically remove dust, scratches, stains, fading while preserving original grain. Sharpen micro-details, recover dynamic range. Colorize with 1940-1970 Kodak Portra tones if B&W. Re-photographed with Canon EOS R5 Mark II + RF 85mm f/1.2 L USM, soft window light, 1000% identity lock, signature \"Carlos Ernesto\" bottom-right"
    )
    st.code(restauracion_nuclear + f"\n\nNegative prompt: {NEGATIVE_NUCLEAR}", language="text")

st.markdown("<div class='footer'>Grok Prompt Builder v25.0 Nuclear Ultimate 2025 - Prompts Cortos + Resumen Automático - (c) Carlos Ernesto 2025</div>", unsafe_allow_html=True)
