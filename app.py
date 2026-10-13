
import streamlit as st

st.title("Mechanical Engineering Calculator")

subject = st.selectbox(
    "Select Subject",
    [
        "Mechanics",
        "Strength of Materials",
        "Thermodynamics",
        "Fluid Mechanics",
        "Thermal Engineering",
        "Machine Design"
    ]
)

def force():
    m = st.number_input("Mass (kg)", min_value=0.0)
    a = st.number_input("Acceleration (m/s²)")
    if st.button("Calculate Force"):
        st.success(f"Force = {m * a:.2f} N")

def work():
    f = st.number_input("Force (N)", min_value=0.0)
    d = st.number_input("Distance (m)", min_value=0.0)
    if st.button("Calculate Work"):
        st.success(f"Work = {f * d:.2f} J")

def power():
    w = st.number_input("Work (J)", min_value=0.0)
    t = st.number_input("Time (s)", min_value=0.0)
    if st.button("Calculate Power"):
        if t > 0:
            st.success(f"Power = {w / t:.2f} W")
        else:
            st.error("Time must be greater than zero.")

def kinetic_energy():
    m = st.number_input("Mass (kg)", min_value=0.0)
    v = st.number_input("Velocity (m/s)")
    if st.button("Calculate Kinetic Energy"):
        st.success(f"Kinetic Energy = {0.5 * m * v**2:.2f} J")

if subject == "Mechanics":
    operation = st.selectbox(
        "Select Calculation",
        ["Force", "Work", "Power", "Kinetic Energy"]
    )

    if operation == "Force":
        force()
    elif operation == "Work":
        work()
    elif operation == "Power":
        power()
    elif operation == "Kinetic Energy":
        kinetic_energy()
else:
    st.info("This module will be added next.")
