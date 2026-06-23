import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Módulo de Costos", page_icon="📈", layout="wide")

st.title("📈 Estructura Financiera y Costos Operativos")
st.write("---")

# Base de datos orientada a costos
datos_costos = {
    "Concepto": ["Logística", "Planilla", "Infraestructura Cloud", "Marketing"],
    "Gasto_USD": [8500, 15000, 3200, 4100]
}
df_costos = pd.DataFrame(datos_costos)

# Métricas rápidas financieras
total_gasto = df_costos["Gasto_USD"].sum()
st.metric(label="📉 COSTOS OPERATIVOS TOTALES (OPEX)", value=f"${total_gasto:,} USD")

# Gráfico de distribución de gastos
fig_costos = px.pie(df_costos, values="Gasto_USD", names="Concepto", hole=0.5, title="Distribución de Costos Mensuales", color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig_costos, use_container_width=True)
