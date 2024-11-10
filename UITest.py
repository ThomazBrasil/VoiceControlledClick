import customtkinter




customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x400")
app.title("From the screen to the ring to the pen to the king")
app.resizable(False, False)


def start_callback():
    print("start click")

def stop_callback():
    print("stop click")

def slider_callback(value):
    
    print(value)


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame_1, text="Mic Volume for Trigger")
label.pack(pady=10, padx=10)

slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=30)
slider_1.pack(pady=10, padx=10)
slider_1.set(10)

label_2 = customtkinter.CTkLabel(master=frame_1, text="Microphone Volume: 0")
label.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=start_callback, text="Start")
button_1.pack(pady=10, padx=10, side="left")
button_2 = customtkinter.CTkButton(master=frame_1, command=stop_callback, text="Stop")
button_2.pack(pady=10, padx=10, side="left")




text_1 = customtkinter.CTkTextbox(master=frame_1, width=200, height=70)
text_1.pack(pady=10, padx=10)
text_1.insert("0.0", "CTkTextbox\n\n\n\n")



app.mainloop()