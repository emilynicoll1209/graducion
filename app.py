import streamlit as st
import joblib
import numpy as np

# Cargar modelo entrenado
modelo = joblib.load("primermillon.joblib")

# Configuración de la página
st.set_page_config(page_title="Predictor de Éxito Académico", page_icon="🎓")

# Título
st.title("Predictor de Éxito Académico")
st.write("**Autor:** EMILY DAVID")

# Imagen
st.image("https://buscacarrera.com.co/public/content/articulos/la-clave-del-exito-academico-como-crear-un-plan-de-estudio-efectivo.jpg", use_container_width=True)

# Introducción
st.markdown("""
Esta aplicación predice si una estudiante logrará graduarse y tener éxito en la Universidad  
a partir de dos variables: **Nota IA** y **GPA**.  
Para usarla:
1. Ajusta los valores usando los controles deslizantes.
2. Haz clic en el botón para obtener la predicción.
""")

# Sliders para entrada
nota_ia = st.slider("Nota IA", 0.0, 1.0, 0.5, step=0.1)
gpa = st.slider("GPA", 0.0, 1.0, 0.5, step=0.1)

# Botón de predicción
if st.button("Predecir"):
    entrada = np.array([[nota_ia, gpa]])
    prediccion = modelo.predict(entrada)[0]

    if prediccion == 0:
        st.markdown(
            "<p style='color:red; font-size:20px;'>❌ No se graduará</p>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<p style='color:green; font-size:20px;'>🎉 Felicitaciones, te vas a graduar con honores</p>",
            unsafe_allow_html=True
        )

# Pie de página
st.markdown("---")
st.markdown("© UNAB 2025")
