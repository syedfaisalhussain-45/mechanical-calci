
import math

def get_input(msg):
    while True:
        try:
            x = float(input(msg))
            if x < 0:
                print("Enter a valid positive value.")
            else:
                return x
        except ValueError:
            print("Invalid input. Enter a number.")

def force():
    m = get_input("Enter mass (kg): ")
    a = get_input("Enter acceleration (m/s^2): ")
    print("Force =", m * a, "N")

def work():
    f = get_input("Enter force (N): ")
    d = get_input("Enter distance (m): ")
    print("Work =", f * d, "J")

def power():
    w = get_input("Enter work (J): ")
    t = get_input("Enter time (s): ")
    if t > 0:
        print("Power =", w / t, "W")
    else:
        print("Time must be greater than zero.")

def kinetic_energy():
    m = get_input("Enter mass (kg): ")
    v = get_input("Enter velocity (m/s): ")
    print("Kinetic Energy =", 0.5 * m * v ** 2, "J")

def stress():
    f = get_input("Enter force (N): ")
    a = get_input("Enter area (m^2): ")
    if a > 0:
        print("Stress =", f / a, "Pa")
    else:
        print("Area must be greater than zero.")

def strain():
    change = get_input("Enter change in length (m): ")
    length = get_input("Enter original length (m): ")
    if length > 0:
        print("Strain =", change / length)
    else:
        print("Length must be greater than zero.")

def young_modulus():
    s = get_input("Enter stress (Pa): ")
    e = get_input("Enter strain: ")
    if e > 0:
        print("Young's Modulus =", s / e, "Pa")
    else:
        print("Strain must be greater than zero.")

def heat_transfer():
    m = get_input("Enter mass (kg): ")
    c = get_input("Enter specific heat (J/kg K): ")
    dt = get_input("Enter temperature change (K): ")
    print("Heat Transfer =", m * c * dt, "J")

def thermo_work():
    p = get_input("Enter pressure (Pa): ")
    v1 = get_input("Enter initial volume (m^3): ")
    v2 = get_input("Enter final volume (m^3): ")
    print("Work Done =", p * (v2 - v1), "J")

def thermal_efficiency():
    w = get_input("Enter useful work (J): ")
    q = get_input("Enter heat supplied (J): ")
    if q > 0:
        print("Efficiency =", w / q * 100, "%")
    else:
        print("Heat supplied must be greater than zero.")

def pressure():
    f = get_input("Enter force (N): ")
    a = get_input("Enter area (m^2): ")
    if a > 0:
        print("Pressure =", f / a, "Pa")
    else:
        print("Area must be greater than zero.")

def reynolds_number():
    rho = get_input("Enter density (kg/m^3): ")
    v = get_input("Enter velocity (m/s): ")
    d = get_input("Enter diameter (m): ")
    mu = get_input("Enter viscosity (Pa s): ")
    if mu > 0:
        print("Reynolds Number =", rho * v * d / mu)
    else:
        print("Viscosity must be greater than zero.")

def flow_velocity():
    q = get_input("Enter discharge (m^3/s): ")
    a = get_input("Enter area (m^2): ")
    if a > 0:
        print("Flow Velocity =", q / a, "m/s")
    else:
        print("Area must be greater than zero.")

def discharge():
    a = get_input("Enter area (m^2): ")
    v = get_input("Enter velocity (m/s): ")
    print("Discharge =", a * v, "m^3/s")

def heat_conduction():
    k = get_input("Enter conductivity (W/m K): ")
    a = get_input("Enter area (m^2): ")
    dt = get_input("Enter temperature difference (K): ")
    l = get_input("Enter wall thickness (m): ")
    if l > 0:
        print("Heat Conduction Rate =", k * a * dt / l, "W")
    else:
        print("Thickness must be greater than zero.")

def cop():
    q = get_input("Enter cooling effect (J): ")
    w = get_input("Enter work input (J): ")
    if w > 0:
        print("COP =", q / w)
    else:
        print("Work input must be greater than zero.")

def heat_engine_efficiency():
    q1 = get_input("Enter heat supplied (J): ")
    q2 = get_input("Enter heat rejected (J): ")
    if q1 > 0:
        print("Efficiency =", (q1 - q2) / q1 * 100, "%")
    else:
        print("Heat supplied must be greater than zero.")

def torque():
    f = get_input("Enter force (N): ")
    r = get_input("Enter perpendicular distance (m): ")
    print("Torque =", f * r, "N m")

def shaft_power():
    t = get_input("Enter torque (N m): ")
    n = get_input("Enter speed (rpm): ")
    p = 2 * math.pi * n * t / 60
    print("Shaft Power =", p, "W")
    print("Shaft Power =", p / 1000, "kW")

def shaft_diameter():
    t = get_input("Enter torque (N m): ")
    s = get_input("Enter allowable shear stress (Pa): ")
    if s > 0:
        d = (16 * t / (math.pi * s)) ** (1 / 3)
        print("Shaft Diameter =", d * 1000, "mm")
    else:
        print("Shear stress must be greater than zero.")

def submenu(title, names, funcs):
    while True:
        print("\n", title)
        for i in range(len(names)):
            print(i + 1, names[i])
        print("0. Back")

        ch = input("Enter choice: ")

        if ch == "0":
            break
        elif ch.isdigit() and 1 <= int(ch) <= len(funcs):
            funcs[int(ch) - 1]()
        else:
            print("Invalid choice.")

def main():
    while True:
        print("\nMECHANICAL ENGINEERING CALCULATOR")
        print("1. Mechanics")
        print("2. Strength of Materials")
        print("3. Thermodynamics")
        print("4. Fluid Mechanics")
        print("5. Thermal Engineering")
        print("6. Machine Design")
        print("0. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            submenu("MECHANICS",
                    ["Force", "Work", "Power", "Kinetic Energy"],
                    [force, work, power, kinetic_energy])

        elif ch == "2":
            submenu("STRENGTH OF MATERIALS",
                    ["Stress", "Strain", "Young's Modulus"],
                    [stress, strain, young_modulus])

        elif ch == "3":
            submenu("THERMODYNAMICS",
                    ["Heat Transfer", "Work Done", "Thermal Efficiency"],
                    [heat_transfer, thermo_work, thermal_efficiency])

        elif ch == "4":
            submenu("FLUID MECHANICS",
                    ["Pressure", "Reynolds Number",
                     "Flow Velocity", "Discharge"],
                    [pressure, reynolds_number, flow_velocity, discharge])

        elif ch == "5":
            submenu("THERMAL ENGINEERING",
                    ["Heat Conduction", "COP", "Heat Engine Efficiency"],
                    [heat_conduction, cop, heat_engine_efficiency])

        elif ch == "6":
            submenu("MACHINE DESIGN",
                    ["Torque", "Shaft Power", "Shaft Diameter"],
                    [torque, shaft_power, shaft_diameter])

        elif ch == "0":
            print("Thank you for using the calculator.")
            break

        else:
            print("Invalid choice.")

main()
