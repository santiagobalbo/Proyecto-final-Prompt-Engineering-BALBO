import openai
import streamlit as st

# Crear el cliente de OpenAI correctamente
client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

def generar_plan_alimentacion(edad, peso, altura, actividad, objetivo):
    prompt = (f"Genera un plan de alimentación semanal para una persona de {edad} años, {peso} kg, "
              f"{altura} m de altura, que hace ejercicio {actividad} veces por semana y quiere {objetivo}. "
              "Incluye desayuno, almuerzo, merienda y cena con opciones variadas.")

    respuesta = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un experto en nutrición."},
            {"role": "user", "content": prompt}
        ]
    )

    return respuesta.choices[0].message.content

# Interfaz de Streamlit
st.title("NutriAI - Planificación de Alimentación Personalizada")
st.write("Ingrese sus datos para recibir un plan de alimentación adecuado a sus necesidades.")

# Entrada de datos del usuario
edad = st.number_input("Edad", min_value=1, max_value=120, value=25)
peso = st.number_input("Peso (kg)", min_value=30, max_value=200, value=70)
altura = st.number_input("Altura (m)", min_value=1.0, max_value=2.5, value=1.75)
actividad = st.slider("Frecuencia de ejercicio (veces por semana)", 0, 7, 3)
objetivo = st.selectbox("Objetivo", ["mantener peso", "perder peso", "ganar masa muscular"])

# Botón para generar el plan
if st.button("Generar Plan de Alimentación"):
    plan = generar_plan_alimentacion(edad, peso, altura, actividad, objetivo)
    st.subheader("Tu Plan de Alimentación:")
    st.write(plan)

# Sección "Cómo funciona"
st.markdown("## Cómo funciona")
st.write("1. Ingrese sus datos personales: edad, peso, altura y nivel de actividad.")
st.write("2. Seleccione su objetivo nutricional.")
st.write("3. Haga clic en 'Generar Plan de Alimentación'.")
st.write("4. La IA generará un plan de comidas personalizado basado en su información.")

# Footer
st.write("NutriAI utiliza inteligencia artificial para proporcionar recomendaciones generales. Consulte a un profesional para asesoramiento personalizado.")

