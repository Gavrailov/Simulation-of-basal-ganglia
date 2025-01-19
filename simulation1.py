import nest
import matplotlib.pyplot as plt

# Create 100 neurons of type iaf_psc_alpha
neurons = nest.Create("iaf_psc_alpha", 100)

# Set custom properties for all neurons at once (the dictionary should be inside a list)
nest.SetStatus(neurons, [{
    "C_m": 250.0,
    "tau_m": 20.0,
    "E_L": -70.0,
    "V_th": -55.0,
    "V_reset": -65.0
}])

# Create Poisson generator with rate of 2500 Hz
poisson_gen = nest.Create("poisson_generator", 1, params={"rate": 2500.0})

# Create spike recorder for recording spikes
spike_recorder = nest.Create("spike_recorder", 1)

# Connect the Poisson generator to the neurons with weight and delay
nest.Connect(poisson_gen, neurons, syn_spec={"weight": 1.0, "delay": 1.5})

# Connect neurons to spike recorder
nest.Connect(neurons, spike_recorder)

# Run the simulation for 500 ms
nest.Simulate(500.0)

# Retrieve spike data from the spike recorder
spikes = nest.GetStatus(spike_recorder, "events")[0]
times = spikes["times"]
senders = spikes["senders"]

print(times)
print(senders)
print(spikes)

# Plot the spike raster plot
plt.figure(figsize=(10, 6))
plt.plot(times, senders, ".")
plt.xlabel("Time (ms)")
plt.ylabel("Neuron ID")
plt.title("Spike Raster Plot")
plt.show()
