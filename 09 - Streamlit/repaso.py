import pandas as pd
import streamlit as st

opcion = st.sidebar.radio(
    "Seleccine una opción",
    ("Cargar Archivo", "Análisis Exploratorio")
)

st.title("Titulo")

if "student_habits" not in st.session_state:
    st.session_state.student_habits = None


if opcion == "Cargar Archivo":
    file_path = st.file_uploader(
        "Seleccione la fuente de datos", accept_multiple_files=False
    )
    
    if file_path:
        st.success(f"Path: {file_path}")
        
        df = pd.read_csv(file_path)
        
        st.session_state.student_habits = df
        
        st.success("Archivo cargado correctamente.")
        
        
        
elif opcion == "Análisis Exploratorio":
    shape = st.session_state.student_habits.shape
    average = st.session_state.student_habits["exam_score"].mean()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Estudiantes", shape[0])
    col2.metric("Variables", shape[1])
    col3.metric("Promedio", average)

    
    st.write("Primeras 5 filas:")
    st.dataframe(st.session_state.student_habits.head())
    
    ganadores = st.session_state.student_habits.loc[st.session_state.student_habits['exam_score'] >= 61]
    perdedores = st.session_state.student_habits.loc[st.session_state.student_habits['exam_score'] < 61]
    
    #st.dataframe(ganadores)
    #st.dataframe(perdedores)
    
    horas_estudio_ganadores = ganadores["study_hours_per_day"].mean()
    st.write(f"Promedio de horas de estudio de los ganadores: {horas_estudio_ganadores}")
    
    horas_estudio_perdedores = perdedores["study_hours_per_day"].mean()
    st.write(f"Promedio de horas de estudio de los perdedores: {horas_estudio_perdedores}")
    
    st.write("Trabajo ganadores:")
    trabajang = ganadores["part_time_job"].value_counts()
    st.table(trabajang)
    
    st.write("Trabajo perdedores:")
    trabajan = perdedores["part_time_job"].value_counts()
    st.table(trabajan)
    
    st.write("Comida ganadores:")
    comidag = ganadores["diet_quality"].value_counts()
    st.table(comidag)
    
    st.write("Comida perdedores:")
    comidap = perdedores["diet_quality"].value_counts()
    st.table(comidap)
        
    horas_suenio_ganadores = ganadores["sleep_hours"].mean()
    st.write(f"Promedio de horas de sueño de los ganadores: {horas_suenio_ganadores}")
    
    horas_suenio_perdedores = perdedores["sleep_hours"].mean()
    st.write(f"Promedio de horas de sueño de los perdedores: {horas_suenio_perdedores}")
    
    horas_sm_ganadores = ganadores["social_media_hours"].mean()
    st.write(f"Promedio de horas de redes sociales de los ganadores: {horas_sm_ganadores}")
    
    horas_sm_perdedores = perdedores["social_media_hours"].mean()
    st.write(f"Promedio de horas de redes sociales de los perdedores: {horas_sm_perdedores}")
    
    st.write("Estudiantes que ganaron vs trabajo")
    st.bar_chart(trabajang)
    
    st.write("Estudiantes que perdieron vs trabajo")
    st.bar_chart(trabajan)
        
        
        
        
        
        