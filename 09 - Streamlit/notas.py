import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Análisis de Estudiantes", layout="wide")
st.title("Notas++")

opcion = st.sidebar.radio("Selecciona una opción:", [
    "Cargar archivo",
    "Ver contenido del archivo",
    "Analizar archivo",
    "Registrar estudiante",
    "Ver notas de un estudiante"
])

if "df" not in st.session_state:
    st.session_state.df = None

# Cargar archivo
if opcion == "Cargar archivo":
    archivo = st.file_uploader("Sube el archivo CSV", type=["csv"])
    if archivo:
        try:
            df = pd.read_csv(archivo)
            st.session_state.df = df
            st.success("Archivo cargado correctamente.")
        except Exception as e:
            st.error(f"Ocurrió un error al leer el archivo: {e}")

# Ver contenido
elif opcion == "Ver contenido del archivo":
    if st.session_state.df is not None:
        st.dataframe(st.session_state.df)
    else:
        st.warning("Primero debes cargar un archivo.")

# Análisis
elif opcion == "Analizar archivo":
    if st.session_state.df is not None:
        df = st.session_state.df
        st.subheader("Dimensiones del archivo")
        st.write(f"El archivo tiene {df.shape[0]} filas y {df.shape[1]} columnas.")

        st.subheader("Estadísticas descriptivas")
        st.dataframe(df.select_dtypes(include='number').describe().transpose())

        st.subheader("Promedio por actividad")
        columnas_notas = [
            col for col in df.columns
            if col.startswith("HT") or "proyecto" in col.lower() or "quiz" in col.lower()
        ]
        promedios = df[columnas_notas].mean().sort_index()

        fig, ax = plt.subplots(figsize=(10, 5))
        promedios.plot(kind='bar', ax=ax, color='skyblue')
        ax.axhline(61, color='red', linestyle='--', label='Nota mínima (61)')
        ax.set_ylabel("Promedio")
        ax.set_title("Promedio por actividad")
        ax.set_xticklabels(promedios.index, rotation=45)
        ax.legend()
        st.pyplot(fig)
    else:
        st.warning("Primero debes cargar un archivo.")

# Registro
elif opcion == "Registrar estudiante":
    if st.session_state.df is not None:
        with st.form("form_nuevo_estudiante"):
            st.subheader("Registro de nuevo estudiante")
            nuevo_id = st.text_input("ID del estudiante")
            nuevo_nombre = st.text_input("Nombre completo")
            nuevo_email = st.text_input("Correo electrónico")

            st.markdown("Ingresa las notas (de 0 a 100):")
            notas_ht = [st.number_input(f"HT{i}", 0, 100, 0, 1) for i in range(1, 8)]
            notas_proyectos = [st.number_input(f"Proyecto{i}", 0, 100, 0, 1) for i in range(1, 6)]
            notas_quizzes = [st.number_input(f"Quiz{i}", 0, 100, 0, 1) for i in range(1, 13)]

            enviado = st.form_submit_button("Registrar")

            if enviado:
                nueva_fila = {
                    "id": nuevo_id,
                    "nombre": nuevo_nombre,
                    "email": nuevo_email
                }
                for i in range(1, 8):
                    nueva_fila[f"HT{i}"] = notas_ht[i - 1]
                for i in range(1, 6):
                    nueva_fila[f"proyecto{i}"] = notas_proyectos[i - 1]
                for i in range(1, 13):
                    nueva_fila[f"quiz{i}"] = notas_quizzes[i - 1]

                st.session_state.df = pd.concat([st.session_state.df, pd.DataFrame([nueva_fila])], ignore_index=True)
                st.success("Estudiante registrado exitosamente.")
    else:
        st.warning("Primero debes cargar un archivo para poder registrar estudiantes.")

# Ver notas individuales
elif opcion == "Ver notas de un estudiante":
    if st.session_state.df is not None:
        df = st.session_state.df
        st.subheader("Consulta de notas por estudiante")
        nombres = df["nombre"].tolist()
        seleccionado = st.selectbox("Selecciona un estudiante", nombres)

        estudiante = df[df["nombre"] == seleccionado].iloc[0]
        notas = {col: estudiante[col] for col in df.columns if col.startswith("HT") or "proyecto" in col.lower() or "quiz" in col.lower()}
        st.write(f"Notas de {estudiante['nombre']} (ID: {estudiante['id']})")
        notas_df = pd.DataFrame.from_dict(notas, orient='index', columns=["Nota"])
        st.dataframe(notas_df)
    else:
        st.warning("Primero debes cargar un archivo.")
