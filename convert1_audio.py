import ffmpeg

# Convert clip1
ffmpeg.input(
    "clips/clip1.mp4"
).output(
    "clips/clip1.wav"
).run()

# Convert clip2
ffmpeg.input(
    "clips/clip2.mp4"
).output(
    "clips/clip2.wav"
).run()

print("Week1 audio conversion completed.")