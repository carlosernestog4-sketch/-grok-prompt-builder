
import streamlit as st
from io import BytesIO

st.set_page_config(page_title="Grok Prompt Builder v7.9 Nuclear 2025", layout="centered")

# Estilo v7.9
st.markdown("""
<style>
    .main {background-color: #0a0e17; color: #e0e0e0;}
    h1 {color: #00d4ff; text-align: center; font-size: 2.8rem;}
    .stButton>button {background-color: #00d4ff; color: black; font-weight: bold; border-radius: 10px; height: 3em;}
    .stDownloadButton>button {background-color: #1f77b4; color: white;}
    .footer {text-align: center; margin-top: 60px; font-size: 0.9rem; color: #666;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>Grok Prompt Builder v7.9 Nuclear Ultimate 2025</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>Por Carlos Ernesto - Nitidez, Contraste e Identity Siempre ON</p>", unsafe_allow_html=True)

# Texto fijo obligatorio al inicio
texto_fijo_inicio = "Generate a hyperrealistic 8K image without changing facial features, hair, or skin tone of the subject in the image I show you. Firma en la parte inferior derecha de Carlos Ernesto. "

# Botones siempre activos por defecto
nitidez_extrema = st.checkbox("Activar nitidez extrema profesional (siempre ON)", value=True)
contraste_extremo = st.checkbox("Activar contraste extremo profesional (siempre ON)", value=True)
usar_lock_absoluto = st.checkbox("Activar IDENTIDAD LOCK ABSOLUTO v7 (1000% inviolable - siempre ON)", value=True)

nitidez_texto = "extreme sharpness, razor-sharp micro-details, perfect micro-contrast, high dynamic range throughout, " if nitidez_extrema else ""
contraste_texto = "perfect shadow/highlight recovery, rich deep blacks, bright highlights, cinematic contrast curve, " if contraste_extremo else ""

# Género y tipo de cuerpo (solo si desactivas lock)
if not usar_lock_absoluto:
    masculino = st.checkbox("Sujeto Masculino", value=True)
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
else:
    masculino = True
    tipo_cuerpo = "Delgado (slim)"

if usar_lock_absoluto:
    identidad_final = ("Exact same person, 31 years old, 1.650 m barefoot height, 59-61 kg, BMI 21.8, lean ectomorph body, zero visible muscle definition, flat stomach, narrow shoulders 39 cm biacromial, long slim arms (arm span 1.70 m), narrow wrists 16 cm, long legs, visible thigh gap. "
                       "Face: perfect rectangle 19.5 cm length x 14 cm width, strong square jaw 120 degree gonial angle, high defined cheekbones, straight medium nose 5.2 cm length, thin upper lip 8 mm, medium lower lip, philtrum 1.4 cm. "
                       "Eyes: dark green (hex #1A3C34), almond shape 3.2 cm width, slightly hooded upper lid, subtle lower eye bags, very dark limbal ring, inter-pupillary distance 6.3 cm, slight downward outer canthus. "
                       "Eyebrows: thick, dark brown #1C110A, straight with natural arch, 0.9 cm thickness. "
                       "Hair: military high & tight buzzcut 1-2 mm all over, dark brown #1C110A, receding temples NW2, sharp widow's peak. "
                       "Skin: Fitzpatrick II-III, warm Mediterranean undertone, L*a*b* = L68 a+10 b+18, visible pores especially nose/cheeks, subtle freckles on shoulders, two small moles (left cheekbone + right jawline). "
                       "Tattoos: large detailed blackwork sacred geometry + lion on left pectoral (exact reference preserved), small minimalist coordinates tattoo inner left forearm. "
                       "Always clean-shaven, zero stubble, neutral closed-mouth expression, direct gaze to camera.")
    st.success("IDENTIDAD LOCK ABSOLUTO v7 ACTIVADO - 1000% no drift ever")
else:
    if masculino:
        identidad_final = f"attractive man with {tipo_cuerpo.lower().replace(' (slim)', '').replace(' (athletic)', '').replace(' (average)', '')} body"
    else:
        identidad_final = f"attractive woman with {tipo_cuerpo.lower().replace(' (slim)', '').replace(' (athletic)', '').replace(' (average)', '')} body"
    st.info("Modo flexible activado - solo género y tipo de cuerpo")

# Firma obligatoria
firma_obligatoria = ', signature "Carlos Ernesto" in Cormorant Garamond Italic 48 pt, 78% opacity, pure white (#FFFFFF) on dark backgrounds / pure black (#000000) on light, positioned exactly 40 px from right edge and 40 px from bottom edge, drop shadow 15% opacity radius 2 px'

# Negative nuclear
negative_nuclear = ("worst quality, low quality, normal quality, lowres, bad anatomy, bad hands, missing fingers, extra digits, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry, out of focus, censorship, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, bad proportions, extra limbs, cloned face, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, cross-eyed, mutated, bad body, bad feet, disfigured, gross proportions, modern makeup, perfect teeth, airbrushed skin, doll skin, barbie look, waxy texture, beauty filter, over-smoothed details, fake sharpness, halation artifacts, deformed hands, extra fingers, uncanny valley, lens flare, digital noise, posterization, banding, compression artifacts, plastic skin, glossy skin, porcelain skin, mannequin look, cgi render, 3d model, illustration, cartoon, painting, heavy retouch, skin smoothing, deformed pores, blurry texture, low detail skin, over-sharpening halos, AI artifacts, symmetry excess, doll eyes, text, logo, watermark, overexposed, underexposed")

# Configuración Nuclear v7
st.markdown("### Configuracion Nuclear v7")

col1, col2 = st.columns(2)
with col1:
    tipo_plano = st.selectbox("Tipo de Plano v7", [
        "Plano extremo (face 95-100%)", "Primerisimo primer plano", "Primer plano", "Plano medio corto", "Plano americano", "Plano medio (70-80% height)", "Plano general", "Gran plano general (full body + space feet)"
    ])
    lente_exacta = st.selectbox("Variacion Lente Exacta v7", [
        "RF 85mm f/1.2 @ f/1.8 (primer plano extremo)",
        "RF 85mm f/1.2 @ f/2.8 (retrato clasico)",
        "RF 50mm f/1.2 @ f/4 (plano medio)",
        "RF 35mm f/1.4 @ f/5.6 (plano completo)",
        "iPhone 16 Pro Max 48MP main 1x, simulated f/1.6, Dolby Vision HDR"
    ])
    iluminacion_pro = st.selectbox("Iluminacion Profesional v7", [
        "3-point + rim + hair light: 120cm octabox key 45 degree + silver fill 2:1 + 30cm stripbox rim + hair light top-back, all 5600K CRI 98+",
        "soft diffused daylight golden hour wrap-around",
        "neutral daylight HDR",
        "overcast soft light",
        "studio softbox high-CRI",
        "soft window light 1940-1970 vintage"
    ])

with col2:
    composicion_pro = st.selectbox("Composicion v7", ["rule of thirds golden ratio eye-level, subject 75% height (85% full body)", "centred symmetric", "low-angle dramatic", "high-angle natural"])
    fondo = st.text_input("Fondo v7", "clean seamless dark studio background")
    usar_formula_nuclear = st.checkbox("Activar FORMULA NUCLEAR 2025 base (nunca falla)", value=False)  # Apagado por defecto

# Detalles Extra Pro v7 (apagado por defecto)
expandir_detalles = st.checkbox("Activar Detalles Extra Pro v7", value=False)
detalles_base = st.text_area("Detalles Extra base v7", value="mirada intensa directa, pose frontal relajada, camiseta negra ajustada, brillo natural en piel")

if expandir_detalles:
    detalles_final = f"{detalles_base}, intense emotional depth confident direct gaze natural asymmetry, visible pores subtle sweat highlights micro-wrinkles fabric grain realistic imperfections, cinematic serene moody atmosphere, razor-sharp micro-details high dynamic range, 1000% exact facial identity lock no drift ever"
    st.success("Detalles Pro v7 ACTIVADOS")
else:
    detalles_final = detalles_base

# FORMULA NUCLEAR 2025
if usar_formula_nuclear:
    base_nuclear = ("Ultra photorealistic 8K 16-bit RAW museum-grade portrait of exact same 31-year-old slim man 1.65m as identity reference, 1000% identity lock no drift ever, shot on Canon EOS R5 Mark II + RF 85mm f/1.2 L USM at f/1.8 (or f/4 full body), 1/250s, ISO 100, 14-bit CR3, "
                    "3-point professional studio lighting: 120cm octabox key light 45 degree camera right at eye height + 20 degree grid, silver fill reflector left side 2:1 ratio, subtle 30cm stripbox rim light 160 degree behind, hair light 20 degree grid top-back, all Profoto B10X+ 5600K CRI 98+, "
                    "soft wrap-around shadows with visible micro-shadows under cheekbones and jaw, natural rectangular catchlights, rule of thirds golden ratio, eye-level angle, subject exactly 75% vertical frame height (85% full body), creamy bokeh, micro-contrast preserved, "
                    "output sharpening radius 0.65px 300 DPI, subtle Kodak Tri-X 400 grain 3.5%, color graded custom Adobe RGB LUT \"Portra 400 Golden Hour v3\", hyperrealistic visible pores even at 1:1, zero plastic skin, zero beauty retouch")
else:
    base_nuclear = "Generate a hyperrealistic 8K image without changing facial features hair or skin tone of the subject, extreme sharpness perfect micro-contrast high dynamic range razor-sharp details throughout"

# Prompt principal
sujeto_final = f"photorealistic portrait of {identidad_final}, "

prompt_en = f"{texto_fijo_inicio}{base_nuclear} {nitidez_texto}{contraste_texto}{sujeto_final}{tipo_plano}, shot on Canon EOS R5 Mark II + {lente_exacta}, {iluminacion_pro}, {composicion_pro}, prioritise natural skin texture visible pores micro-details realistic imperfections subtle wrinkles fabric grain, {fondo}, {detalles_final}, ultra HD 8K photorealistic maximum clarity detail Adobe RGB, {firma_obligatoria}"

prompt_es = f"{texto_fijo_inicio}{base_nuclear} {nitidez_texto}{contraste_texto}Retrato fotorealista de {identidad_final}, {tipo_plano}, tomado con Canon EOS R5 Mark II + {lente_exacta}, {iluminacion_pro}, {composicion_pro}, priorizar textura piel natural poros visibles micro-detalles imperfecciones realistas arrugas sutiles grano tela, {fondo}, {detalles_final}, ultra HD 8K fotorealista maximo detalle claridad Adobe RGB, {firma_obligatoria}"

negative_full = f"\n\nNegative prompt: {negative_nuclear}"

full_en = prompt_en + negative_full
full_es = prompt_es + negative_full

# Salida principal
st.markdown("### Prompt Ingles Nuclear v7.9")
st.code(full_en, language="text")
col1, col2 = st.columns(2)
with col1:
    if st.button("Copiar Ingles"):
        st.markdown(f"""
        <script>
        navigator.clipboard.writeText(`{full_en}`);
        </script>
        """, unsafe_allow_html=True)
        st.success("Prompt Ingles copiado al portapapeles!")
with col2:
    buffer_en = BytesIO(full_en.encode())
    st.download_button("Descargar .txt Ingles", buffer_en, "prompt_ingles_v7.9.txt", "text/plain")

st.markdown("### Prompt Espanol Nuclear v7.9")
st.code(full_es, language="text")
col3, col4 = st.columns(2)
with col3:
    if st.button("Copiar Espanol"):
        st.markdown(f"""
        <script>
        navigator.clipboard.writeText(`{full_es}`);
        </script>
        """, unsafe_allow_html=True)
        st.success("Prompt Espanol copiado al portapapeles!")
with col4:
    buffer_es = BytesIO(full_es.encode())
    st.download_button("Descargar .txt Espanol", buffer_es, "prompt_espanol_v7.9.txt", "text/plain")

# Perfeccionador profesional
st.markdown("### Perfeccionador de Prompt Profesional v7.9")
prompt_crudo = st.text_area("Pega aquí cualquier prompt crudo para aumentarlo con palabras técnicas profesionales", height=150, placeholder="Ej: un hombre mirando a cámara...")

if st.button("Aumentar con palabras técnicas profesionales"):
    if prompt_crudo.strip():
        prompt_perfeccionado = f"{texto_fijo_inicio}{base_nuclear} {nitidez_texto}{contraste_texto}{prompt_crudo.strip()}, shot on Canon EOS R5 Mark II + RF 85mm f/1.2 L USM, {iluminacion_pro}, {composicion_pro}, prioritise natural skin texture visible pores micro-details realistic imperfections subtle wrinkles fabric grain, {fondo}, {detalles_final}, ultra HD 8K photorealistic maximum clarity detail Adobe RGB, {firma_obligatoria}"
        full_perfeccionado = prompt_perfeccionado + negative_full
        st.code(full_perfeccionado, language="text")
        st.markdown(f"""
        <script>
        navigator.clipboard.writeText(`{full_perfeccionado}`);
        </script>
        """, unsafe_allow_html=True)
        st.success("Prompt aumentado y copiado al portapapeles!")
    else:
        st.warning("Pega un prompt primero")

# Restauracion v7
if st.button("Generar Plantilla Restauracion Nuclear v7"):
    restauracion_nuclear = (
        f"{texto_fijo_inicio}"
        "Museum-grade restoration of this damaged historical photograph to 8K 16-bit: surgically remove every dust speck, scratch, fold, crease, chemical stain, water damage, silvering, yellowing and fading while preserving 100% original film grain structure and chemical fingerprint. "
        "Forensic pixel-perfect reconstruction of missing areas. Frequency separation sharpening radius 0.7px, local contrast +8, full dynamic range recovery. "
        "If B&W -> colorize only with 1940-1970 Kodak Portra 400 / Ektachrome E100 calibrated tones, otherwise keep authentic sepia/silver gelatin. "
        "Re-photographed with Hasselblad 503CW + Carl Zeiss Planar 80mm f/2.8 T* on Portra 400VC, soft north window light 1940-1970 era, 1000% identity lock, no modern retouch, signature \"Carlos Ernesto\" bottom-right"
    )
    st.code(restauracion_nuclear + negative_full, language="text")

st.markdown("<div class='footer'>Grok Prompt Builder v7.9 Nuclear Ultimate 2025 - 1000% Inviolable - (c) Carlos Ernesto 2025</div>", unsafe_allow_html=True)
