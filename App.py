import streamlit as st

st.set_page_config(page_title="Grok Prompt Builder Pro", layout="centered")
st.title("🔧 Grok Prompt Builder Pro - Por Carlos Ernesto")

# Bloqueo de identidad 100%
identidad = "Hombre de 31 años, 1.65m, delgado atractivo con poca masa muscular, ojos verdes oscuro almendrados ligeramente hundidos, cabello muy corto rapado militar oscuro, piel media bronceada Fitzpatrick II-III con poros visibles y microtextura realista, sin barba, afeitado limpio"

# Negative prompt completo
negative = "modern makeup, perfect teeth, airbrushed skin, doll skin, barbie look, waxy texture, beauty filter, over-smoothed details, fake sharpness, halation artifacts, deformed hands, extra fingers, uncanny valley, lens flare, digital noise, posterization, banding, compression artifacts, plastic skin, glossy skin, porcelain skin, mannequin look, cgi render, 3d model, illustration, cartoon, painting, heavy retouch, skin smoothing, deformed pores, blurry texture, low detail skin, over-sharpening halos, AI artifacts, symmetry excess, doll eyes"

# Firma obligatoria
firma = ', signature "Carlos Ernesto" in small elegant serif font bottom right corner'

st.header("Configura tu Prompt Profesional")

col1, col2 = st.columns(2)
with col1:
    tipo_plano = st.selectbox("Tipo de Plano", ["Primer Plano (Close-Up)", "Plano Medio (Medium Shot)", "Plano Completo (Full Shot)"])
    lente = st.selectbox("Lente/Cámara", ["85mm f/1.4", "50mm f/2.8", "35mm f/2.0", "iPhone 16 Pro Max"])
    iluminacion = st.selectbox("Iluminación", ["soft diffused daylight at golden hour, 3-point lighting", "neutral daylight", "overcast soft light", "studio softbox golden hour"])

with col2:
    composicion = st.selectbox("Composición", ["rule-of-thirds, eye-level framing", "centred portrait", "low-angle"])
    fondo = st.text_input("Fondo/Escenario", "clean seamless grey studio background")
    resolucion = st.selectbox("Calidad", ["hyperrealistic 8K", "ultra HD photorealistic 8K"])

detalles_extra = st.text_area("Detalles Extra (pose, expresión, vestuario, etc.)", "neutral expression, frontal pose, wearing casual t-shirt")

# Construir prompts
prompt_en = f"Photorealistic portrait of a {identidad}, {tipo_plano.lower()}, shot on {lente} with shallow depth of field and natural compression, {iluminacion}, {composicion}, prioritise natural skin texture with visible pores and subtle imperfections, {fondo}, {detalles_extra}, {resolucion}, no plastic skin{firma}"

prompt_es = f"Retrato fotorealista de un {identidad}, {tipo_plano}, tomado con {lente} con profundidad de campo superficial, {iluminacion}, {composicion}, priorizar textura de piel natural con poros visibles, {fondo}, {detalles_extra}, {resolucion}, sin piel plástica{firma}"

negative_completo = f"Negative prompt: {negative}"

st.markdown("### Prompt en Inglés (Copiar-Pegar para Gemini)")
st.code(prompt_en + "\n\n" + negative_completo, language="text")

st.markdown("### Prompt en Español")
st.code(prompt_es + "\n\n" + negative_completo, language="text")

st.success("¡Prompt listo! Copia y pega en Gemini. Cada cambio se actualiza al instante.")
