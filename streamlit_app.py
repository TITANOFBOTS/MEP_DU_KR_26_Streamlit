import streamlit as st
import pandas as pd
# import nglview as nv
# from ase.io import read, write


st.set_page_config(page_title="MEP progress report", layout="wide")

st.title("MEP progress report")


# Create tabs
tab_home, tab_benchmark, tab_geometry_convergence, tab_ml_training, tab_force_accuracy = st.tabs(["🏠 Home", "📈 Benchmark", "📐 Geometry Convergence", " 🤖 ML training", " ⚙️ Force accuracy benchmarks"])

# ----------------- Home Tab -----------------
with tab_home:
    st.header("Welcome")
    st.write("In this report the progress on the MEP project is summarized.")
    st.write("Use the tabs above to navigate through different sections of the report.")
    st.write("current tabs: Home, Benchmark, Geometry Convergence, ML training, Force accuracy benchmarks")



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
    st.image("figures/AccForceMagParity_1em7SCF.svg", caption="The parity plot between the ML FF calculated forces and DFT forces (SCF convergence < 1e-7)")
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



with tab_ml_training:
    st.header("Training of Machine Learning Force Fields")
    st.write("see wandb projects: https://wandb.ai/dullersma-tu-delft/projects")



with tab_force_accuracy:
    st.header("Force Accuracy Benchmarks of Machine Learning Force Fields (CP2K)")

    st.subheader("Gallium Nanoparticle MD trajectory")
    st.image('figures/FF_bench/CP2K/MD/Ga_NP/parity_plot_force_MACE-matpes-r2scan-omat-ft.png', caption="force parity plot MACE vs DFT for Ga NP MD CP2K trajectory")
    st.image('figures/FF_bench/CP2K/MD/Ga_NP/parity_plot_force_MACE_Ga_omat24_subset_scratch_trained.png', caption="force parity plot MACE vs DFT for Ga NP MD CP2K trajectory")
    st.image('figures/FF_bench/CP2K/MD/Ga_NP/parity_plot_force_MACE_Ga_omat24_subset_finetuned_ema_high_lr.png', caption="force parity plot MACE vs DFT for Ga NP MD CP2K trajectory (finetuned with replay and with high learning rate)")   
    st.image('figures/FF_bench/CP2K/MD/Ga_NP/net_forces_DFT_benchmark_base_atoms57_stableF.png', caption="net forces DFT for Ga NP MD CP2K trajectory") 

    # md_traj = read('figures/FF_bench/CP2K/MD/Ga_NP/DFT_benchmark_base_atoms57_stableF.traj', index=':')
    # view = nv.show_ase(md_traj)
    # st.html(view._repr_html_())

    st.subheader('Bulk Ga MD CP2K trajectory')
    st.image('figures/FF_bench/CP2K/MD/Ga_bulk/parity_plot_force_MACE-matpes-r2scan-omat-ft.png', caption='force parity plot MACE vs DFT for Ga bulk MD CP2K trajectory')
    st.image('figures/FF_bench/CP2K/MD/Ga_bulk/net_forces_MD_sim_calc_CP2K_PBE_T350_atoms64_Ga_bulk.png')


    st.subheader('Bulk Cu and Au MD trajectories')
    st.image('figures/FF_bench/CP2K/MD/Cu_bulk/parity_plot_force_MACE-matpes-r2scan-omat-ft.png', caption='force parity plot MACE vs DFT for Cu bulk MD CP2K trajectory')
    st.image('figures/FF_bench/CP2K/MD/Cu_bulk/net_forces_MD_sim_calc_CP2K_PBE_T1450_atoms32_Cu_bulk.png')
    st.image('figures/FF_bench/CP2K/MD/Au_bulk/parity_plot_force_MACE-matpes-r2scan-omat-ft.png', caption='force parity plot MACE vs DFT for Au bulk MD CP2K trajectory')
    st.image('figures/FF_bench/CP2K/MD/Au_bulk/net_forces_MD_sim_calc_CP2K_PBE_T1450_atoms32_Au_bulk.png')

    st.subheader('In and Sn NP MD CP2K trajectories')
    st.image('figures/FF_bench/CP2K/MD/In_NP/parity_plot_force_MACE-matpes-r2scan-omat-ft.png', caption='force parity plot MACE vs DFT for In NP MD CP2K trajectory')
    st.image('figures/FF_bench/CP2K/MD/In_NP/net_forces_MD_sim_calc_CP2K_PBE_T500_atoms55_In_nanoparticle.png', caption='net forces DFT for In NP MD CP2K trajectory')
    st.image('figures/FF_bench/CP2K/MD/Sn_NP/parity_plot_force_MACE-matpes-r2scan-omat-ft.png', caption='force parity plot MACE vs DFT for Sn NP MD CP2K trajectory')
    st.image('figures/FF_bench/CP2K/MD/Sn_NP/net_forces_MD_sim_calc_CP2K_PBE_T600_atoms57_Sn_nanoparticle.png', caption='net forces DFT for Sn NP MD CP2K trajectory')


    st.subheader("Gallium Nanoparticle Rattle trajectory")
    st.image('figures/FF_bench/CP2K/Rattle/Ga_NP/parity_plot_force_MACE-matpes-r2scan-omat-ft.png', caption="force parity plot MACE-R2SCAN vs DFT for Ga NP Rattle CP2K trajectory")
    st.image('figures/FF_bench/CP2K/Rattle/Ga_NP/parity_plot_force_MACE_Ga_omat24_subset_finetuned.png', caption="force parity plot MACE vs DFT for Ga NP Rattle CP2K trajectory (finetuned with replay)")
    st.image('figures/FF_bench/CP2K/Rattle/Ga_NP/parity_plot_force_orb-v3-conservative-inf-omat-finetuned-v2.png', caption="force parity plot ORBv3-conservative vs DFT for Ga NP Rattle CP2K trajectory (finetuned without replay!)")
    st.image('figures/FF_bench/CP2K/Rattle/Ga_NP/net_forces_Ga_NP_atoms57_rattled.png', caption="net forces DFT for Ga NP Rattle CP2K trajectory")

    # rattle_traj = read('figures/FF_bench/CP2K/Rattle/Ga_NP/Ga_NP_atoms57_rattled_subset.xyz', index=':')
    # view = nv.show_ase(rattle_traj)
    # st.html(view._repr_html_())

    st.header('Force Accuracy Benchmarks of Machine Learning Force Fields (VASP)')
    st.image('figures/FF_bench/CP2K/VASP/Rattle/Ga_NP/parity_plot_force_MACE-matpes-r2scan-omat-ft.png', caption="force parity plot MACE-R2SCAN vs DFT for Ga NP Rattle VASP trajectory")
    st.image('figures/FF_bench/CP2K/VASP/Rattle/Ga_NP/parity_plot_force_MACE_Ga_matpes_r2scan_replay_VASP_finetuned_ema_high_lr.png', caption="force parity plot MACE vs DFT for Ga NP Rattle VASP trajectory (finetuned with replay and with high learning rate)")
    st.image('figures/FF_bench/CP2K/VASP/Rattle/Ga_NP/net_forces_vasp_concat.png', caption='net forces DFT for Ga NP paper dataset VASP trajectory')
    st.image('figures/FF_bench/CP2K/VASP/Rattle/Ga_NP/net_forces_rattled_Ga_NP_pool_copy_0611.png', caption='net forces DFT for Ga NP Rattle VASP trajectory')

        



