import sounddevice as sd
import numpy as np
import keyboard
import customtkinter
import threading

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

running = False  # Set to False initially
mic_thingy = 10


app = customtkinter.CTk()
app.geometry("400x400")
app.title("From the screen to the ring to the pen to the king")
app.resizable(False, False)

var = customtkinter.IntVar()

def start_callback():
    global running
    print("start click")
    running = True
    # Start the while loop in a new thread
    thread = threading.Thread(target=monitor_microphone)
    thread.start()

def monitor_microphone():
    global running
    while running:
        print("OK!")
        with sd.InputStream(callback=print_volume):
            sd.sleep(500)  # Keeps the stream alive and updates the volume every 0.5 second

def stop_callback():
    global running
    print("stop click")
    running = False

def slider_callback(value):
    global mic_thingy
    mic_thingy = value

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame_1, text="Mic Volume for Trigger")
label.pack(pady=10, padx=10)

slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, variable=var, from_=0, to=30)
slider_1.pack(pady=10, padx=10, side="top")
slider_1.set(10)

label2 = customtkinter.CTkLabel(master=frame_1, textvariable=var)
label2.pack(pady=10, padx=10)

label2 = customtkinter.CTkLabel(master=frame_1, text="Microphone Volume: 0")
label2.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=start_callback, text="Start")
button_1.pack(pady=10, padx=10, side="left")
button_2 = customtkinter.CTkButton(master=frame_1, command=stop_callback, text="Stop")
button_2.pack(pady=10, padx=10, side="left")

text_1 = customtkinter.CTkTextbox(master=frame_1, width=200, height=70)
text_1.pack(pady=10, padx=10)
text_1.insert("0.0", "CTkTextbox\n\n\n\n")

def print_volume(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    print(f'Microphone Volume: {volume_norm:.2f}')
    if volume_norm > 10:
        keyboard.press('space')
    else:
        keyboard.release('space')

print("aaaa")
app.mainloop()
