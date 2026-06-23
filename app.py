import streamlit as st

# Configuración de página base
st.set_page_config(page_title="Cuadro de Mando - Inicio", page_icon="🏢", layout="wide")

st.title("🏢 Consolidado Gerencial de la Empresa")
st.markdown("## Bienvenido al Sistema de Soporte de Decisiones")
st.write("---")

st.info("👈 Utiliza el menú de la barra lateral para navegar de forma multidimensional entre los distintos departamentos.")

# Simulación de KPI general de la corporación
col1, col2 = st.columns(2)
with col1:
    st.metric(label="MÁRGEN NETO CORPORATIVO", value="24.5 %", delta="+1.2 %")
with col2:
    st.metric(label="VALOR DE LA MARCA (EST.)", value="$2.4 M", delta="Estable")
