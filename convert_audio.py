import ffmpeg

# Convert first file
ffmpeg.input(
    "golden_set/golden1.mp4"
).output(
    "golden_set/golden1.wav"
).run()

# Convert second file
ffmpeg.input(
    "golden_set/golden2.mp4"
).output(
    "golden_set/golden2.wav"
).run()

print("Audio conversion completed.")