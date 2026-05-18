import librosa
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Create output folders
os.makedirs("artifacts/week2/plots", exist_ok=True)
os.makedirs("artifacts/week2/exports", exist_ok=True)

# Golden clips
audio_files = [
    "golden_set/golden1.wav",
    "golden_set/golden2.wav",
    "golden_set/golden3.wav",
    "golden_set/golden4.wav",
    "golden_set/golden5.wav"
]

# Process clips
for index, audio_path in enumerate(audio_files):

    print(f"Processing: {audio_path}")

    # Load audio
    y, sr = librosa.load(audio_path)

    # Pitch extraction
    f0, voiced_flag, voiced_probs = librosa.pyin(
        y,
        fmin=librosa.note_to_hz('C2'),
        fmax=librosa.note_to_hz('C7'),
        hop_length=256
    )

    # Time axis
    times = librosa.times_like(f0)

    # -------- Pitch Trace --------
    plt.figure(figsize=(10,3))

    plt.plot(times, f0)

    plt.title(f"Pitch Trace {index+1}")
    plt.xlabel("Time")
    plt.ylabel("Frequency (Hz)")

    plt.savefig(
        f"artifacts/week2/plots/pitch_trace_{index+1}.png"
    )

    plt.close()

    # -------- Note Candidate Export --------
    notes = []

    for t, pitch, conf in zip(times, f0, voiced_probs):

        if pitch is not None and not np.isnan(pitch):

            notes.append({
                "start_s": round(float(t), 3),
                "end_s": round(float(t + 0.1), 3),
                "midi_or_hz": round(float(pitch), 2),
                "confidence": round(float(conf), 2)
            })

    df = pd.DataFrame(notes)

    # Export CSV
    df.to_csv(
        f"artifacts/week2/exports/note_candidates_{index+1}.csv",
        index=False
    )

    # Export JSON
    df.to_json(
        f"artifacts/week2/exports/note_candidates_{index+1}.json",
        orient="records",
        indent=2
    )

print("Week2 pipeline completed successfully.")