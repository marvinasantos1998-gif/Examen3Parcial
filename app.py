import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Configuración inicial de la página
st.set_page_config(page_title="Examen - Identificador de Imagenes/Marvin Santos Rivera", page_icon="☁️")

# Nombres de las clases del dataset CIFAR-10 en español
class_names = ['Avión', 'Auto', 'Pájaro', 'Gato', 'Ciervo',
               'Perro', 'Rana', 'Caballo', 'Barco', 'Camión']

# Función para cargar el modelo en caché y optimizar rendimiento
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('modelo_cifar10.h5')

# Intentar cargar el modelo
try:
    model = load_model()
    modelo_cargado = True
except Exception as e:
    st.error("⚠️ No se pudo encontrar el archivo 'modelo_cifar10.h5'. Asegúrate de subirlo al repositorio.")
    modelo_cargado = False

# Encabezado principal (Cumpliendo requerimientos de la rúbrica)
st.title("Clasificador de Imágenes con IA")
st.markdown("### Examen – Computación en la Nube")
st.markdown("**Universidad Tecnológica de Honduras (UTH)**")
st.markdown("**Docente:** Ing. Asalia Zavala")
st.markdown("**Desarrollado por:** Marvin Josué Santos Rivera")
st.divider()

st.write("Sube una imagen desde tu dispositivo o toma una foto para que el modelo identifique de qué objeto se trata.")

# Pestañas para elegir el método de entrada de imagen
tab1, tab2 = st.tabs(["📁 Subir Imagen", "📷 Tomar Foto"])

img_file_buffer = None

with tab1:
    archivo_subido = st.file_uploader("Selecciona una imagen (JPG, PNG, JPEG)", type=["jpg", "png", "jpeg"])
    if archivo_subido:
        img_file_buffer = archivo_subido

with tab2:
    foto_tomada = st.camera_input("Captura una imagen con tu cámara")
    if foto_tomada:
        img_file_buffer = foto_tomada

# Procesamiento y Predicción
if img_file_buffer is not None and modelo_cargado:
    # Cargar y mostrar la imagen original
    image = Image.open(img_file_buffer)
    st.image(image, caption='Imagen a analizar', use_container_width=True)

    with st.spinner("La IA está analizando la imagen..."):
        # Preprocesar la imagen para que coincida con el input de CIFAR-10 (32x32 píxeles)
        img_resized = image.resize((32, 32))
        img_array = np.array(img_resized)
        
        # Eliminar canal alfa si la imagen es PNG (de 4 a 3 canales RGB)
        if img_array.shape[-1] == 4:
            img_array = img_array[..., :3]

        # Normalizar y expandir dimensiones
        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Realizar la predicción
        predictions = model.predict(img_array)
        predicted_class_idx = np.argmax(predictions[0])
        confidence = np.max(predictions[0])

    # Mostrar resultados en columnas
    st.divider()
    st.subheader("Resultados del Análisis")
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"**Predicción:** {class_names[predicted_class_idx]}")
    with col2:
        st.info(f"**Confianza:** {confidence:.2f}")

