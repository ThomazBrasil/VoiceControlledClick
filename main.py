import sounddevice as sd
import numpy as np
import keyboard
import customtkinter
import threading

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

running = False  # Set to False initially

app = customtkinter.CTk()
app.geometry("400x400")
app.title("Voice Controlled Click")
app.resizable(False, False)
app.iconbitmap("icon.ico")

var = customtkinter.IntVar()

mic_thingy = 10

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
        with sd.InputStream(callback=print_volume):
            sd.sleep(500)  # Keeps the stream alive and updates the volume every 0.5 second

def stop_callback():
    global running
    running = False

def slider_callback(value):
    global mic_thingy
    mic_thingy = value

def on_closing():
    global running
    running = False
    app.destroy()

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame_1, text="Mic Volume for Trigger")
label.pack(pady=10, padx=10)

slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, variable=var, from_=0, to=100)
slider_1.pack(pady=10, padx=10, side="top")
slider_1.set(10)

label2 = customtkinter.CTkLabel(master=frame_1, textvariable=var)
label2.pack(pady=10, padx=10)

label2 = customtkinter.CTkLabel(master=frame_1, text=f"Microphone Volume: 0")
label2.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=start_callback, text="Start")
button_1.pack(pady=10, padx=10, side="left")
button_2 = customtkinter.CTkButton(master=frame_1, command=stop_callback, text="Stop")
button_2.pack(pady=10, padx=10, side="left")

def print_volume(indata, frames, time, status):
    global volume_norm
    volume_norm = np.linalg.norm(indata) * 10
    print(f'Microphone Volume: {volume_norm:.2f}')
    if volume_norm > mic_thingy:
        keyboard.press('space')
    else:
        keyboard.release('space')

# Bind the custom close function to the window close event
app.protocol("WM_DELETE_WINDOW", on_closing)

app.mainloop()