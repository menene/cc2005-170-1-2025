import streamlit as st
import pandas as pd

st.title("Mi primera página 😜")

opcion = st.sidebar.selectbox(
    "Seleccione una opcion", 
    ["Agregar estudiante", "Datos"]
)

if opcion == "Agregar estudiante":
    st.header("Nuevo estudiante")
    
    nombre = st.text_input("Ingresa tu nombre:")
    edad = st.number_input("Ingresa tu edad:", min_value=0)
    
    opcion = st.radio("Selecciona tu lenguaje favorito:",
                        ["Python", "R", "JavaScript"]
    )

    nivel = st.select_slider(
        "Selecciona tu nivel de experiencia:",
        options=["Principiante", "Intermedio", "Avanzado"],
        value="Intermedio"
    )
    
elif opcion == "Datos":
    
    datos = {
        "Actividad": ["HT1", "HT2", "HT3", "HT4"],
        "Promedio": [75, 80, 68, 90]
    }

    df = pd.DataFrame(datos)

    st.bar_chart(df.set_index("Actividad"))
    
    st.dataframe(df)
    
