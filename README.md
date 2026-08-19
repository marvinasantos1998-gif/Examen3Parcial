Examen - Computación en la Nube ☁️

**Universidad Tecnológica de Honduras (UTH)**  
**Docente:** Ing. Asalia Zavala  
**Estudiante:** Marvin Josué Santos Rivera  
**Enlace Streamlit:** https://examen3parcial-marvinjosuesantos.streamlit.app/

## 🎯 Objetivo del Proyecto
Desarrollar e implementar en la nube un modelo básico de Machine Learning (Red Neuronal Convolucional - CNN) capaz de identificar objetos en imágenes proporcionadas por el usuario (subidas desde el dispositivo o capturadas con la cámara web).

## 🚀 Características
* **Clasificación en 10 categorías:** Avión, Auto, Pájaro, Gato, Ciervo, Perro, Rana, Caballo, Barco y Camión.
* **Interfaz interactiva:** Construida con Streamlit, intuitiva y fácil de usar.
* **Modelo de IA:** Entrenado con TensorFlow/Keras utilizando el famoso dataset **CIFAR-10**.
* **Despliegue en la Nube:** Aplicación alojada de forma pública y accesible mediante Streamlit Community Cloud.

## 🛠️ Tecnologías y Herramientas Utilizadas
* **Lenguaje:** Python
* **Librerías principales:** `tensorflow`, `streamlit`, `numpy`, `Pillow`
* **Entorno de Entrenamiento:** Google Colab (con aceleración por GPU)
* **Despliegue:** Streamlit Community Cloud conectado a GitHub

## 📂 Estructura del Repositorio
* `app.py`: Código principal de la interfaz web desarrollada en Streamlit.
* `modelo_cifar10.h5`: Archivo del modelo de Machine Learning pre-entrenado (generado en Google Colab).
* `requirements.txt`: Lista de librerías y dependencias necesarias para el correcto funcionamiento de la app.
* `README.md`: Archivo de documentación actual.

## 💻 Instrucciones de Ejecución Local
Si deseas probar este proyecto en tu propia computadora, sigue estos pasos:

1. Asegúrate de tener Python instalado en tu sistema.
2. Clona este repositorio o descarga los archivos en una misma carpeta.
3. Abre una terminal en esa carpeta e instala las dependencias ejecutando:
   ```bash
   pip install -r requirements.txt
