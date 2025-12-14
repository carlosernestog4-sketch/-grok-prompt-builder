
import streamlit as st
from io import BytesIO

st.set_page_config(page_title="Grok Prompt Builder v22.0 Nuclear 2025", layout="centered")

# Estilo v22.0
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

st.markdown("<h1>Grok Prompt Builder v22.0 Nuclear Ultimate 2025</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>Por Carlos Ernesto - Perfeccionador Independiente + NameError Corregido</p>", unsafe_allow_html=True)

# Texto fijo al inicio
texto_fijo_inicio = "Generate a hyperrealistic 8K image without changing facial features, hair, or skin tone of the subject in the image I show you. Firma en la parte inferior derecha de Carlos Ernesto. "

# Firma obligatoria
firma_obligatoria = ', signature "Carlos Ernesto" in Cormorant Garamond Italic 48 pt, 78% opacity, pure white (#FFFFFF) on dark backgrounds / pure black (#000000) on light, positioned exactly 40 px from right edge and 40 px from bottom edge, drop shadow 15% opacity radius 2 px'

# Negative nuclear
negative_nuclear = ("worst quality, low quality, normal quality, lowres, bad anatomy, bad hands, missing fingers, extra digits, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry, out of focus, censorship, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, bad proportions, extra limbs, cloned face, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, cross-eyed, mutated, bad body, bad feet, disfigured, gross proportions, modern makeup, perfect teeth, airbrushed skin, doll skin, barbie look, waxy texture, beauty filter, over-smoothed details, fake sharpness, halation artifacts, deformed hands, extra fingers, uncanny valley, lens flare, digital noise, posterization, banding, compression artifacts, plastic skin, glossy skin, porcelain skin, mannequin look, cgi render, 3d model, illustration, cartoon, painting, heavy retouch, skin smoothing, deformed pores, blurry texture, low detail skin, over-sharpening halos, AI artifacts, symmetry excess, doll eyes, text, logo, watermark, overexposed, underexposed")

# FORMULA NUCLEAR 2025
FORMULA_NUCLEAR_BASE = ("Ultra photorealistic 8K 16-bit RAW museum-grade portrait of exact same 31-year-old slim man 1.65m as identity reference, 1000% identity lock no drift ever, shot on Canon EOS R5 Mark II + RF 85mm f/1.2 L USM at f/1.8 (or f/4 full body), 1/250s, ISO 100, 14-bit CR3, "
                        "3-point professional studio lighting: 120cm octabox key light 45 degree camera right at eye height + 20 degree grid, silver fill reflector left side 2:1 ratio, subtle 30cm stripbox rim light 160 degree behind, hair light 20 degree grid top-back, all Profoto B10X+ 5600K CRI 98+, "
                        "soft wrap-around shadows with visible micro-shadows under cheekbones and jaw, natural rectangular catchlights, rule of thirds golden ratio, eye-level angle, subject exactly 75% vertical frame height (85% full body), creamy bokeh, micro-contrast preserved, "
                        "output sharpening radius 0.65px 300 DPI, subtle Kodak Tri-X 400 grain 3.5%, color graded custom Adobe RGB LUT \"Portra 400 Golden Hour v3\" with rich vibrant colors and cinematic tone mapping, hyperrealistic visible pores even at 1:1, zero plastic skin, zero beauty retouch")

FORMULA_SIMPLE = "Generate a hyperrealistic 8K image without changing facial features hair or skin tone of the subject, extreme sharpness perfect micro-contrast high dynamic range razor-sharp details throughout"

IDENTIDAD_LOCK = ("Exact same person, 31 years old, 1.650 m barefoot height, 59-61 kg, BMI 21.8, lean ectomorph body, zero visible muscle definition, flat stomach, narrow shoulders 39 cm biacromial, long slim arms (arm span 1.70 m), narrow wrists 16 cm, long legs, visible thigh gap. "
                  "Face: perfect rectangle 19.5 cm length x 14 cm width, strong square jaw 120 degree gonial angle, high defined cheekbones, straight medium nose 5.2 cm length, thin upper lip 8 mm, medium lower lip, philtrum 1.4 cm. "
                  "Eyes: dark green (hex #1A3C34), almond shape 3.2 cm width, slightly hooded upper lid, subtle lower eye bags, very dark limbal ring, inter-pupillary distance 6.3 cm, slight downward outer canthus. "
                  "Eyebrows: thick, dark brown #1C110A, straight with natural arch, 0.9 cm thickness. "
                  "Hair: military high & tight buzzcut 1-2 mm all over, dark brown #1C110A, receding temples NW2, sharp widow's peak. "
                  "Skin: Fitzpatrick II-III, warm Mediterranean undertone, L*a*b* = L68 a+10 b+18, visible pores especially nose/cheeks, subtle freckles on shoulders, two small moles (left cheekbone + right jawline). "
                  "Always clean-shaven, zero stubble, neutral closed-mouth expression, direct gaze to camera.")

# ===============================
# PROMPT PRINCIPAL
# ===============================

st.markdown("### Prompt Principal")

# Checkboxes principales
nitidez_extrema_main = st.checkbox("Activar nitidez extrema profesional (principal)", value=True)
contraste_extremo_main = st.checkbox("Activar contraste extremo profesional (principal)", value=True)
usar_lock_absoluto_main = st.checkbox("Activar IDENTIDAD LOCK ABSOLUTO v7 (principal)", value=True)

nitidez_texto_main = "extreme sharpness, razor-sharp micro-details, perfect micro-contrast, high dynamic range throughout, " if nitidez_extrema_main else ""
contraste_color_texto_main = "perfect shadow/highlight recovery, rich deep blacks, bright vibrant highlights, cinematic contrast curve with rich saturated colors, no dull tones, " if contraste_extremo_main else ""

# Identidad principal
if usar_lock_absoluto_main:
    identidad_main = IDENTIDAD_LOCK
else:
    masculino_main = st.checkbox("Sujeto Masculino (principal)", value=True)
    tipo_cuerpo_main = st.selectbox("Tipo de Cuerpo (principal)", [
        "Delgado (slim)", "Atlético (athletic)", "Medio (average)", "Curvy (curvy)", 
        "Reloj de arena (hourglass)", "Triángulo invertido (inverted triangle)", 
        "Rectangular (rectangle)", "Pera (pear)"
    ])
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
    usar_formula_main = st.checkbox("Activar FORMULA NUCLEAR 2025 base (principal)", value=False)

# Prioridad principal
prioridad_texto_main = st.text_area("Prioridad (principal)", value="", height=100)
prioridad_final_main = f"(PRIORITISE WITH MAXIMUM RESPONSIBILITY: {prioridad_texto_main.upper()})" if prioridad_texto_main.strip() else ""

# Detalles extra principal
expandir_detalles_main = st.checkbox("Activar Detalles Extra Pro (principal)", value=False)
detalles_base_main = st.text_area("Detalles Extra base (principal)", value="", height=150, placeholder="Ej: mirada intensa directa, camiseta negra ajustada, fondo oscuro con luces bokeh")

if expandir_detalles_main:
    detalles_final_main = f"{detalles_base_main}, intense emotional depth confident direct gaze natural asymmetry, visible pores subtle sweat highlights micro-wrinkles fabric grain realistic imperfections, cinematic serene moody atmosphere, razor-sharp micro-details high dynamic range, 1000% exact facial identity lock no drift ever"
else:
    detalles_final_main = detalles_base_main

fondo_final_main = detalles_base_main if "fondo" in detalles_base_main.lower() else "clean seamless dark studio background with subtle gradient"

base_nuclear_main = FORMULA_NUCLEAR_BASE if usar_formula_main else FORMULA_SIMPLE

sujeto_final_main = f"photorealistic portrait of {identidad_main}, "

prompt_en_main = f"{texto_fijo_inicio}{base_nuclear_main} {nitidez_texto_main}{contraste_color_texto_main}{prioridad_final_main}{sujeto_final_main}{tipo_plano_main}, shot on {lente_main}, {iluminacion_main}, {composicion_main}, prioritise natural skin texture visible pores micro-details realistic imperfections subtle wrinkles fabric grain, {fondo_final_main}, {detalles_final_main}, ultra HD 8K photorealistic maximum clarity detail Adobe RGB vibrant rich colors, {firma_obligatoria}"

prompt_es_main = f"{texto_fijo_inicio}{base_nuclear_main} {nitidez_texto_main}{contraste_color_texto_main}{prioridad_final_main}Retrato fotorealista de {identidad_main}, {tipo_plano_main}, tomado con {lente_main}, {iluminacion_main}, {composicion_main}, priorizar textura piel natural poros visibles micro-detalles imperfecciones realistas arrugas sutiles grano tela, {fondo_final_main}, {detalles_final_main}, ultra HD 8K fotorealista maximo detalle claridad Adobe RGB colores ricos vibrantes, {firma_obligatoria}"

full_en_main = prompt_en_main + f"\n\nNegative prompt: {negative_nuclear}"
full_es_main = prompt_es_main + f"\n\nNegative prompt: {negative_nuclear}"

# Salida principal
st.markdown("### Prompt Principal Ingles")
st.code(full_en_main, language="text")
col1, col2 = st.columns(2)
with col1:
    if st.button("Copiar Ingles (principal)"):
        st.markdown(f"<script>navigator.clipboard.writeText(`{full_en_main}`);</script>", unsafe_allow_html=True)
        st.success("Prompt Ingles (principal) copiado al portapapeles!")
with col2:
    buffer_en_main = BytesIO(full_en_main.encode())
    st.download_button("Descargar .txt Ingles (principal)", buffer_en_main, "prompt_principal_ingles_v22.0.txt", "text/plain")

st.markdown("### Prompt Principal Espanol")
st.code(full_es_main, language="text")
col3, col4 = st.columns(2)
with col3:
    if st.button("Copiar Espanol (principal)"):
        st.markdown(f"<script>navigator.clipboard.writeText(`{full_es_main}`);</script>", unsafe_allow_html=True)
        st.success("Prompt Espanol (principal) copiado al portapapeles!")
with col4:
    buffer_es_main = BytesIO(full_es_main.encode())
    st.download_button("Descargar .txt Espanol (principal)", buffer_es_main, "prompt_principal_espanol_v22.0.txt", "text/plain")

# ===============================
# PERFECCIONADOR INDEPENDIENTE
# ===============================

st.markdown('<div class="perfeccionador-block">', unsafe_allow_html=True)
st.markdown('<h2 class="perfeccionador-title">Perfeccionador de Prompt Profesional (Totalmente Independiente)</h2>', unsafe_allow_html=True)

# Opciones independientes para el perfeccionador
nitidez_extrema_perf = st.checkbox("Activar nitidez extrema profesional (perfeccionador)", value=True)
contraste_extremo_perf = st.checkbox("Activar contraste extremo profesional (perfeccionador)", value=True)
usar_formula_perf = st.checkbox("Activar FORMULA NUCLEAR 2025 base (perfeccionador)", value=False)  # NUEVA checkbox independiente

nitidez_texto_perf = "extreme sharpness, razor-sharp micro-details, perfect micro-contrast, high dynamic range throughout, " if nitidez_extrema_perf else ""
contraste_color_texto_perf = "perfect shadow/highlight recovery, rich deep blacks, bright vibrant highlights, cinematic contrast curve with rich saturated colors, no dull tones, " if contraste_extremo_perf else ""

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

if expandir_detalles_perf:
    detalles_final_perf = f"{detalles_base_perf}, intense emotional depth confident direct gaze natural asymmetry, visible pores subtle sweat highlights micro-wrinkles fabric grain realistic imperfections, cinematic serene moody atmosphere, razor-sharp micro-details high dynamic range, 1000% exact facial identity lock no drift ever"
else:
    detalles_final_perf = detalles_base_perf

fondo_final_perf = detalles_base_perf if "fondo" in detalles_base_perf.lower() else "clean seamless dark studio background with subtle gradient"

prompt_crudo = st.text_area("Prompt crudo a perfeccionar", height=150, placeholder="Ej: un hombre mirando a cámara...")

if st.button("Generar Prompt Perfeccionado Independiente"):
    if prompt_crudo.strip():
        base_nuclear_perf = FORMULA_NUCLEAR_BASE if usar_formula_perf else FORMULA_SIMPLE  # Usa su propia checkbox
        prompt_perfeccionado_en = f"{texto_fijo_inicio}{base_nuclear_perf} {nitidez_texto_perf}{contraste_color_texto_perf}{prioridad_final_perf}{prompt_crudo.strip()}, {tipo_plano_perf}, shot on {lente_perf}, {iluminacion_perf}, {composicion_perf}, prioritise natural skin texture visible pores micro-details realistic imperfections subtle wrinkles fabric grain, {fondo_final_perf}, {detalles_final_perf}, ultra HD 8K photorealistic maximum clarity detail Adobe RGB vibrant rich colors, {firma_obligatoria}"
        full_perfeccionado_en = prompt_perfeccionado_en + f"\n\nNegative prompt: {negative_nuclear}"
        st.code(full_perfeccionado_en, language="text")
        st.markdown(f"<script>navigator.clipboard.writeText(`{full_perfeccionado_en}`);</script>", unsafe_allow_html=True)
        st.success("Prompt perfeccionado independiente copiado al portapapeles!")
    else:
        st.warning("Pega un prompt crudo primero")

st.markdown('</div>', unsafe_allow_html=True)  # Cierre del bloque azul

# Restauracion
if st.button("Generar Plantilla Restauracion Nuclear v7"):
    restauracion_nuclear = (
        f"{texto_fijo_inicio}"
        "Museum-grade restoration of this damaged historical photograph to 8K 16-bit: surgically remove every dust speck, scratch, fold, crease, chemical stain, water damage, silvering, yellowing and fading while preserving 100% original film grain structure and chemical fingerprint. "
        "Forensic pixel-perfect reconstruction of missing areas. Frequency separation sharpening radius 0.7px, local contrast +8, full dynamic range recovery. "
        "If B&W -> colorize only with 1940-1970 Kodak Portra 400 / Ektachrome E100 calibrated tones, otherwise keep authentic sepia/silver gelatin. "
        "Re-photographed with Canon EOS R5 Mark II + RF 85mm f/1.2 L USM, soft north window light 1940-1970 era, 1000% identity lock, no modern retouch, signature \"Carlos Ernesto\" bottom-right"
    )
    st.code(restauracion_nuclear + f"\n\nNegative prompt: {negative_nuclear}", language="text")

st.markdown("<div class='footer'>Grok Prompt Builder v22.0 Nuclear Ultimate 2025 - NameError Corregido - Perfeccionador Independiente - (c) Carlos Ernesto 2025</div>", unsafe_allow_html=True)
