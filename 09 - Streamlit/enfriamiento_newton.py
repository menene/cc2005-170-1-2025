import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Enfriamiento según la Ley de Newton")

st.markdown("Este modelo predice cómo disminuye la temperatura de un objeto en función del tiempo:")
st.latex(r"T(t) = T_{\text{a}} + (T_0 - T_{\text{a}}) \cdot e^{-k t}")

T0 = st.number_input("Temperatura inicial del objeto (T₀)", value=90.0)
Ta = st.number_input("Temperatura ambiente (Tₐ)", value=25.0)
k = st.number_input("Constante de enfriamiento (k)", value=0.1, min_value=0.01)
t_max = st.slider("Minutos de observación", min_value=10, max_value=120, value=60)

t_vals = np.linspace(0, t_max, 200)
T_vals = Ta + (T0 - Ta) * np.exp(-k * t_vals)

st.latex(
    rf"T(t) = {Ta} + ({T0} - {Ta}) \cdot e^{{-{k} \cdot t}}"
)

st.subheader("Temperatura vs Tiempo")
fig, ax = plt.subplots()
ax.plot(t_vals, T_vals, color='orange', label="Temperatura")
ax.set_xlabel("Tiempo (min)")
ax.set_ylabel("Temperatura (°C)")
ax.set_title("Enfriamiento de un objeto según la ley de Newton")
ax.grid(True)
ax.legend()
st.pyplot(fig)
