import streamlit as st
import pandas as pd


st.set_page_config(page_title="MEP progress report", layout="wide")

st.title("MEP progress report")


# Create tabs
tab_home, tab_benchmark, tab_geometry_convergence = st.tabs(["🏠 Home", "📈 Benchmark", "📐 Geometry Convergence"])

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
    st.image("figures/RDF_benchmark2.png", caption="RDF only with the ML potentials")
    # st.image("figures/TotEnergyBench.png", caption="MD sim stability based on total energy")
    st.image("figures/AccForceMagBench.svg", caption="The magnitude of the forces based on the AIMD trajectory (SCF convergence < 1e-6)")
    st.image("figures/AccForceMagBench_1em7SCF.svg", caption="The magnitude of the forces based on the AIMD trajectory (SCF convergence < 1e-7)")
    st.image("figures/AccForceDiffMagBench.svg", caption="The magnitude of the difference between the ML FF calculated forces and DFT forces (SCF convergence < 1e-6)")
    st.image("figures/AccForceDiffMagBench_1em7SCF.svg", caption="The magnitude of the difference between the ML FF calculated forces and DFT forces (SCF convergence < 1e-7)")
    st.image("figures/AccForceCosSimBench.svg", caption="The cosine similarity between the ML FF calculated forces and DFT forces (SCF convergence < 1e-6)")
    st.image("figures/AccForceCosSimBench_1em7SCF.svg", caption="The cosine similarity between the ML FF calculated forces and DFT forces (SCF convergence < 1e-7)")
    st.image("figures/AccForceMagAtomFacetBench.svg", caption="The magnitude of the forces faceted over all atoms (SCF convergence < 1e-6)")
    st.image("figures/AccForceMagAtomFacetBench_1em7SCF.svg", caption="The magnitude of the forces faceted over all atoms (SCF convergence < 1e-7)")


with tab_geometry_convergence:
    st.header("Nanoparticle Geometry Convergence Data")
    # st.write("This section contains data related to the nanoparticle convergence of geometries in the MEP project.")
    st.write("To investigate the nanoparticle geometry convergence, two different initial geometries were created: \
             a BCC nanoparticle and a Wulff constructed nanoparticle. " \
             "Both nanoparticles were created with approximately the same number of atoms (around 500-600 atoms). " \
             "The BCC structure was created by expanding a BCC cell evenly in the [100], [110], and [111] directions, " \
             "while the Wulff nanoparticle was generated using surface energies calculated with DFT from a paper." \
             " Both structures were then subjected to molecular dynamics simulations at 305 K (melting point) for 20 ps using the ORBv3 conservative uMILP. " \
             "Then the geometries were heated to 1000 K for 100 ps in order to stimulate the global reconstruction of the nanoparticle and finally cooled back down to 305 K for 20 ps. " \
             "The goal was to observe how each geometry evolves over time and to find the converged nanoparticle geometry.")
    
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("BCC Created Nanoparticle")
        st.video('https://youtu.be/DPnWprosEsc')

    with col2:
        st.subheader("Wulff Created Nanoparticle")
        st.video('https://youtu.be/-Z8JtEORtpM')


    col3, col4 = st.columns(2)
    with col3:
        st.subheader("RDF evolution")
        st.video('https://youtu.be/cSbXw3rtizQ')

    with col4:
        st.subheader("RDF difference evolution")
        st.video('https://youtu.be/6aH4MR-l3wE')

    st.image('figures/RDFdiffGeomConvergence.png', caption="RDF difference between the two geometries over time")

        



