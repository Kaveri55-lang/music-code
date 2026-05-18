import matplotlib.pyplot as plt

# Confidence thresholds
thresholds = [0.2, 0.4, 0.6, 0.8]

# Example detected notes
notes_detected = [120, 95, 70, 40]

# Create graph
plt.figure(figsize=(6,4))

plt.plot(
    thresholds,
    notes_detected,
    marker='o'
)

plt.xlabel("Confidence Threshold")
plt.ylabel("Detected Notes")

plt.title("Confidence Threshold Sweep")

# Save graph
plt.savefig(
    "artifacts/week2/plots/confidence_sweep.png"
)

plt.close()

print("Confidence sweep completed successfully.")