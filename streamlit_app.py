import streamlit as st
import pandas as pd


st.set_page_config(page_title="MEP progress report", layout="wide")

st.title("MEP progress report")


# Create tabs
tab_home, tab_benchmark = st.tabs(["🏠 Home", "📈 Benchmark"])

# ----------------- Home Tab -----------------
with tab_home:
    st.header("Welcome")
    st.write("In this report the progress on the MEP project is summarized.")
    st.write("Use the tabs above to navigate through different sections of the report.")
    st.write("current tabs: Home, Benchmark")



# ----------------- Benchmark Tab -----------------
with tab_benchmark:
    st.header("Benchmark Data")
    st.write("This section contains benchmark data for the MEP project.")

    st.subheader("Computational resources")
    st.image("figures/CompTimeBench.png", caption="Computation Time")
    st.image("figures/CompResBench.png", caption="Computation Resources")

    st.subheader("Accuracy Analysis")
    st.image("figures/RDF_benchmark_kimEAM.png", caption="RDF with the Kim EAM potential")
    st.image("figures/RDF_benchmark.png", caption="RDF only with the ML potentials")
    st.image("figures/TotEnergyBench.png", caption="MD sim stability based on total energy")





