import numpy as np
import soundfile as sf
import os

# Create folder
os.makedirs("golden_set", exist_ok=True)

# Audio settings
sr = 22050
duration = 5

# Frequencies
frequencies = [220, 330, 440]

# Generate clips
for i, freq in enumerate(frequencies, start=3):

    t = np.linspace(0, duration, int(sr * duration))

    # Generate sine wave
    y = 0.5 * np.sin(2 * np.pi * freq * t)

    # Save file
    sf.write(
        f"golden_set/golden{i}.wav",
        y,
        sr
    )

print("3 golden clips generated successfully.")