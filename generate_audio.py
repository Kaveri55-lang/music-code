import numpy as np
import soundfile as sf
import os

# Create clips folder
os.makedirs("clips", exist_ok=True)

# Audio settings
sr = 22050
duration = 5

# Frequencies for 5 clips
frequencies = [220, 262, 330, 392, 440]

# Generate clips
for i, freq in enumerate(frequencies):
    t = np.linspace(0, duration, int(sr * duration))

    # Create sine wave
    y = 0.5 * np.sin(2 * np.pi * freq * t)

    # Save audio
    sf.write(f"clips/clip{i+1}.wav", y, sr)

print("5 audio clips generated successfully.")