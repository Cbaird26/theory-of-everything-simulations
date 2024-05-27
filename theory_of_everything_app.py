import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

st.title("Theory of Everything Fun and Wild Simulations")

st.sidebar.title("Choose a Simulation")
simulation = st.sidebar.selectbox("Select a Simulation", list(range(1, 41)))

def simulation_1():
    st.write("### Simulation 1: Quantum Particle in a Box")
    x = np.linspace(0, 1, 1000)
    n = random.randint(1, 5)
    psi = np.sqrt(2) * np.sin(n * np.pi * x)
    plt.plot(x, psi)
    plt.title("Quantum Particle in a Box (n={})".format(n))
    st.pyplot(plt)

def simulation_2():
    st.write("### Simulation 2: Relativistic Effects on a Moving Object")
    v = st.slider("Velocity (as a fraction of the speed of light)", 0.1, 0.99, 0.5)
    gamma = 1 / np.sqrt(1 - v**2)
    st.write(f"Gamma Factor: {gamma}")
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, gamma], label=f'v={v}c')
    plt.title("Relativistic Time Dilation")
    plt.xlabel("Proper Time")
    plt.ylabel("Dilated Time")
    plt.legend()
    st.pyplot(fig)

def simulation_3():
    st.write("### Simulation 3: String Vibrations")
    x = np.linspace(0, 2*np.pi, 1000)
    y = np.sin(5*x) + np.sin(7*x)
    plt.plot(x, y)
    plt.title("String Vibrations")
    st.pyplot(plt)

def simulation_4():
    st.write("### Simulation 4: Black Hole Event Horizon")
    r = np.linspace(1, 10, 1000)
    g = 1 / (r**2)
    plt.plot(r, g)
    plt.title("Gravitational Force Near a Black Hole")
    st.pyplot(plt)

def simulation_5():
    st.write("### Simulation 5: Quantum Entanglement")
    q1 = random.choice(['Up', 'Down'])
    q2 = 'Down' if q1 == 'Up' else 'Up'
    st.write(f"Particle 1: {q1}")
    st.write(f"Particle 2: {q2}")

def simulation_6():
    st.write("### Simulation 6: Multiverse Theory")
    universes = ['Universe {}'.format(i) for i in range(1, 11)]
    chosen_universe = random.choice(universes)
    st.write(f"You are now in {chosen_universe}!")

def simulation_7():
    st.write("### Simulation 7: Holographic Principle")
    x = np.linspace(-5, 5, 1000)
    y = np.sinc(x)
    plt.plot(x, y)
    plt.title("Holographic Principle Representation")
    st.pyplot(plt)

def simulation_8():
    st.write("### Simulation 8: Dark Matter Distribution")
    theta = np.linspace(0, 2*np.pi, 1000)
    r = np.abs(np.sin(5*theta))
    plt.polar(theta, r)
    plt.title("Dark Matter Distribution in a Galaxy")
    st.pyplot(plt)

def simulation_9():
    st.write("### Simulation 9: Gravitational Waves")
    t = np.linspace(0, 4*np.pi, 1000)
    h = np.sin(t) * np.sin(10*t)
    plt.plot(t, h)
    plt.title("Gravitational Waves Propagation")
    st.pyplot(plt)

def simulation_10():
    st.write("### Simulation 10: Quantum Field Fluctuations")
    x = np.linspace(0, 10, 1000)
    y = np.random.normal(size=1000)
    plt.plot(x, y)
    plt.title("Quantum Field Fluctuations")
    st.pyplot(plt)

def simulation_11():
    st.write("### Simulation 11: Cosmic Inflation")
    t = np.linspace(0, 10, 100)
    a = np.exp(t)
    plt.plot(t, a)
    plt.title("Cosmic Inflation")
    st.pyplot(plt)

def simulation_12():
    st.write("### Simulation 12: Supersymmetry Particles")
    particles = ['Squark', 'Slepton', 'Gluino', 'Neutralino']
    discovered_particle = random.choice(particles)
    st.write(f"Discovered Supersymmetry Particle: {discovered_particle}")

def simulation_13():
    st.write("### Simulation 13: Loop Quantum Gravity Spin Networks")
    nodes = np.random.rand(10, 2)
    edges = np.random.randint(0, 10, (15, 2))
    for edge in edges:
        plt.plot(nodes[edge, 0], nodes[edge, 1], 'k-')
    plt.scatter(nodes[:, 0], nodes[:, 1])
    plt.title("Spin Networks in Loop Quantum Gravity")
    st.pyplot(plt)

def simulation_14():
    st.write("### Simulation 14: Quantum Tunneling")
    E = st.slider("Energy of Particle", 0.1, 10.0, 5.0)
    V = 7.0
    if E > V:
        st.write("Particle Tunnels Through the Barrier")
    else:
        st.write("Particle Reflects Back")

def simulation_15():
    st.write("### Simulation 15: Schrödinger's Cat")
    cat_state = random.choice(['Alive', 'Dead'])
    st.write(f"Schrödinger's Cat is {cat_state}")

def simulation_16():
    st.write("### Simulation 16: Quantum Decoherence")
    coherence_time = np.linspace(0, 1, 100)
    decoherence = np.exp(-5 * coherence_time)
    plt.plot(coherence_time, decoherence)
    plt.title("Quantum Decoherence Over Time")
    st.pyplot(plt)

def simulation_17():
    st.write("### Simulation 17: Entropic Gravity")
    T = np.linspace(1, 10, 100)
    S = T**2
    plt.plot(T, S)
    plt.title("Entropic Gravity: Entropy vs. Temperature")
    st.pyplot(plt)

def simulation_18():
    st.write("### Simulation 18: Feynman Diagrams")
    vertices = np.random.rand(5, 2)
    lines = [(i, j) for i in range(5) for j in range(i+1, 5)]
    for line in lines:
        plt.plot(vertices[line, 0], vertices[line, 1], 'b-')
    plt.scatter(vertices[:, 0], vertices[:, 1], color='r')
    plt.title("Random Feynman Diagram")
    st.pyplot(plt)

def simulation_19():
    st.write("### Simulation 19: Noncommutative Geometry")
    theta = np.linspace(0, 2*np.pi, 1000)
    r = 1 + 0.5 * np.sin(5*theta)
    plt.polar(theta, r)
    plt.title("Noncommutative Geometry Visualization")
    st.pyplot(plt)

def simulation_20():
    st.write("### Simulation 20: Quantum Information Theory")
    bits = np.random.choice([0, 1], size=8)
    st.write(f"Random Quantum Bits: {bits}")

def simulation_21():
    st.write("### Simulation 21: Virtual Particles in a Vacuum")
    t = np.linspace(0, 10, 1000)
    fluctuations = np.sin(t) + np.random.normal(scale=0.1, size=1000)
    plt.plot(t, fluctuations)
    plt.title("Virtual Particles Fluctuations")
    st.pyplot(plt)

def simulation_22():
    st.write("### Simulation 22: Casimir Effect")
    d = np.linspace(0.1, 10, 100)
    force = 1 / (d**4)
    plt.plot(d, force)
    plt.title("Casimir Effect: Force vs. Distance")
    st.pyplot(plt)

def simulation_23():
    st.write("### Simulation 23: M-Theory Branes")
    branes = ['D1', 'D3', 'D5', 'M2', 'M5']
    selected_brane = random.choice(branes)
    st.write(f"Selected Brane: {selected_brane}")

def simulation_24():
    st.write("### Simulation 24: Quantum Computing Circuits")
    circuit = np.random.choice(['Hadamard', 'CNOT', 'Pauli-X', 'Pauli-Z'])
    st.write(f"Random Quantum Gate Applied: {circuit}")

def simulation_25():
    st.write("### Simulation 25: Quantum Double-Slit Experiment")
    x = np.linspace(-5, 5, 1000)
    I = np.sin(x)**2
    plt.plot(x, I)
    plt.title("Interference Pattern in Double-Slit Experiment")
    st.pyplot(plt)

def simulation_26():
    st.write("### Simulation 26: Bose-Einstein Condensate")
    T = np.linspace(0, 1, 100)
    N = 1 / (np.exp(1/T) - 1)
    plt.plot(T, N)
    plt.title("Bose-Einstein Condensate")
    st.pyplot(plt)

def simulation_27():
    st.write("### Simulation 27: Quark-Gluon Plasma")
    energy_density = np.random.rand(10, 10)
    plt.imshow(energy_density, cmap='hot', interpolation='nearest')
    plt.title("Quark-Gluon Plasma Energy Density")
    st.pyplot(plt)

def simulation_28():
    st.write("### Simulation 28: Quantum Cryptography")
    key = np.random.choice([0, 1], size=8)
    st.write(f"Generated Quantum Key: {key}")

def simulation_29():
    st.write("### Simulation 29: Quantum Teleportation")
    state = np.random.choice(['|0>', '|1>', '|+>', '|->'])
    st.write(f"State Teleported: {state}")

def simulation_30():
    st.write("### Simulation 30: Quantum Zeno Effect")
    decay_time = np.linspace(0, 10, 100)
    survival_probability = np.exp(-decay_time)
    plt.plot(decay_time, survival_probability)
    plt.title("Quantum Zeno Effect: Survival Probability")
    st.pyplot(plt)

def simulation_31():
    st.write("### Simulation 31: Quantum Hall Effect")
    B = np.linspace(0, 10, 100)
    R = B % 2
    plt.plot(B, R)
    plt.title("Quantum Hall Effect")
    st.pyplot(plt)

def simulation_32():
    st.write("### Simulation 32: Topological Insulators")
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.cos(2*x)
    plt.plot(x, y)
    plt.title("Edge States in Topological Insulators")
    st.pyplot(plt)

def simulation_33():
    st.write("### Simulation 33: Wormholes")
    theta = np.linspace(0, 2*np.pi, 1000)
    r = 1 + 0.3 * np.sin(3*theta)
    plt.polar(theta, r)
    plt.title("Wormhole Visualization")
    st.pyplot(plt)

def simulation_34():
    st.write("### Simulation 34: White Holes")
    r = np.linspace(1, 10, 1000)
    g = -1 / (r**2)
    plt.plot(r, g)
    plt.title("Gravitational Repulsion Near a White Hole")
    st.pyplot(plt)

def simulation_35():
    st.write("### Simulation 35: Kaluza-Klein Theory")
    x = np.linspace(0, 10, 1000)
    y = np.sin(x) + np.cos(x)
    plt.plot(x, y)
    plt.title("Extra Dimensions in Kaluza-Klein Theory")
    st.pyplot(plt)

def simulation_36():
    st.write("### Simulation 36: Quantum Chromodynamics")
    qcd = np.random.rand(10, 10)
    plt.imshow(qcd, cmap='viridis', interpolation='nearest')
    plt.title("Quantum Chromodynamics")
    st.pyplot(plt)

def simulation_37():
    st.write("### Simulation 37: Quantum Gravity Gravitons")
    x = np.linspace(0, 2*np.pi, 1000)
    y = np.sin(10*x)
    plt.plot(x, y)
    plt.title("Gravitons in Quantum Gravity")
    st.pyplot(plt)

def simulation_38():
    st.write("### Simulation 38: Quantum Electrodynamics")
    qed = np.random.normal(size=1000)
    plt.hist(qed, bins=30)
    plt.title("Quantum Electrodynamics")
    st.pyplot(plt)

def simulation_39():
    st.write("### Simulation 39: Gauge Symmetry Breaking")
    x = np.linspace(0, 10, 100)
    y = x**2 - 10*x + 25
    plt.plot(x, y)
    plt.title("Gauge Symmetry Breaking Potential")
    st.pyplot(plt)

def simulation_40():
    st.write("### Simulation 40: Quantum Consciousness Interactions")
    state = random.choice(['Superposition', 'Entanglement', 'Collapse'])
    st.write(f"Quantum Consciousness State: {state}")

simulations = {
    1: simulation_1,
    2: simulation_2,
    3: simulation_3,
    4: simulation_4,
    5: simulation_5,
    6: simulation_6,
    7: simulation_7,
    8: simulation_8,
    9: simulation_9,
    10: simulation_10,
    11: simulation_11,
    12: simulation_12,
    13: simulation_13,
    14: simulation_14,
    15: simulation_15,
    16: simulation_16,
    17: simulation_17,
    18: simulation_18,
    19: simulation_19,
    20: simulation_20,
    21: simulation_21,
    22: simulation_22,
    23: simulation_23,
    24: simulation_24,
    25: simulation_25,
    26: simulation_26,
    27: simulation_27,
    28: simulation_28,
    29: simulation_29,
    30: simulation_30,
    31: simulation_31,
    32: simulation_32,
    33: simulation_33,
    34: simulation_34,
    35: simulation_35,
    36: simulation_36,
    37: simulation_37,
    38: simulation_38,
    39: simulation_39,
    40: simulation_40,
}

st.write("### Welcome to the Theory of Everything Simulations!")
st.write("Choose a simulation from the sidebar to see it in action.")

if simulation in simulations:
    simulations[simulation]()
