import sounddevice as sd
import numpy as np
import keyboard

def print_volume(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    print(f'Microphone Volume: {volume_norm:.2f}')
    if volume_norm > 10:
        keyboard.press('space')
    else:
        keyboard.release('space')


with sd.InputStream(callback=print_volume):
    while True:
        sd.sleep(1000)  # Keeps the stream alive and updates the volume every second

                                                                                                                                  

                                                                                                                                                                                                                                                                     