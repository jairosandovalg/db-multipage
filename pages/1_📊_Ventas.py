import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Módulo de Ventas", page_icon="📊", layout="wide")

st.title("📊 Análisis Comercial y Ventas")
st.write("---")

# Base de datos local orientada a ventas
datos_ventas = {
    "Producto": ["Laptops", "Teclados", "Monitores", "Mouses"],
    "Ingresos_USD": [33500, 5400, 17200, 2300]
}
df_ventas = pd.DataFrame(datos_ventas)

# Filtro interactivo local de la página
producto_sel = st.multiselect("Filtrar Línea de Producto:", options=df_ventas["Producto"].unique(), default=df_ventas["Producto"].unique())
df_filtrado = df_ventas[df_ventas["Producto"].isin(producto_sel)]

# Gráfico de rendimiento comercial
if not df_filtrado.empty:
    fig = px.bar(df_filtrado, x="Producto", y="Ingresos_USD", title="Ingresos Brutos por Producto", color_discrete_sequence=["#58A6FF"])
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Selecciona al menos un producto.")
