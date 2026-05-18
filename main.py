import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os

# Create output folder
os.makedirs("artifacts/week1/audio", exist_ok=True)

# Audio clips
audio_files = [
    "clips/clip1.wav",
    "clips/clip2.wav",
]

# Process all clips
for index, audio_path in enumerate(audio_files):

    # Load audio
    y, sr = librosa.load(audio_path)

    # -------- WAVEFORM --------
    plt.figure(figsize=(10,3))

    librosa.display.waveshow(y, sr=sr)

    plt.title(f"Waveform Clip {index+1}")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")

    plt.savefig(
        f"artifacts/week1/audio/waveform_clip{index+1}.png"
    )

    plt.close()

    # -------- SPECTROGRAM --------
    D = librosa.amplitude_to_db(
        np.abs(librosa.stft(y)),
        ref=np.max
    )

    plt.figure(figsize=(10,4))

    librosa.display.specshow(
        D,
        sr=sr,
        x_axis='time',
        y_axis='log'
    )

    plt.colorbar(format='%+2.0f dB')

    plt.title(f"Spectrogram Clip {index+1}")

    plt.savefig(
        f"artifacts/week1/audio/spectrogram_clip{index+1}.png"
    )

    plt.close()

    # -------- PITCH TRACE --------
    f0, voiced_flag, voiced_probs = librosa.pyin(
        y,
        fmin=librosa.note_to_hz('C2'),
        fmax=librosa.note_to_hz('C7')
    )

    times = librosa.times_like(f0)

    plt.figure(figsize=(10,3))

    plt.plot(times, f0)

    plt.title(f"Pitch Trace Clip {index+1}")
    plt.xlabel("Time")
    plt.ylabel("Frequency (Hz)")

    plt.savefig(
        f"artifacts/week1/audio/pitch_trace_clip{index+1}.png"
    )

    plt.close()

print("Week1 audio processing completed successfully.")