import tkinter as tk
from PIL import Image, ImageTk
import pyperclip as pc
import webbrowser

Height = 700
Width = 600

root = tk.Tk()
root.title("Location Search")
canvas_color = "#F0F0F0"
button_color = "#B8E82D"
entry_color = "#F2FECE"
font_ = ("Roboto", 16)

root.wm_attributes('-alpha', 1)

def search_function(search_term):
    webbrowser.open("https://google.com/maps/place/" + str(search_term))

def copy_to_clipboard():
    pc.copy(entry.get())
    show_notification("Copied to clipboard!")

def clear_entry():
    entry.delete(0, tk.END)
    show_notification("Entry cleared!")

def on_enter(event):
    search_function(entry.get())

def show_notification(message):
    notification_label.config(text=message)
    notification_label.after(2000, lambda: notification_label.config(text=""))

canvas = tk.Canvas(root, height=Height, width=Width, bg=canvas_color, highlightthickness=0)
canvas.pack()

frame = tk.Frame(root, bd=2)
frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

image_path = "Bangkok_city_map.png"
pil_image = Image.open("paris.png")
pil_image = pil_image.convert("RGBA")

# Resize the image to fit the frame
pil_image = pil_image.resize((int(Width*0.9), int(Height*0.8)), Image.Resampling.LANCZOS)
image = ImageTk.PhotoImage(pil_image)

image_label = tk.Label(frame, image=image)
image_label.place(relwidth=1, relheight=1)

entry = tk.Entry(frame, bg=entry_color, font=font_)
entry.place(relx=0.05, rely=0.15, relwidth=0.7, relheight=0.1)

search_button = tk.Button(frame, font=font_, bg=button_color, text="Search", command=lambda: search_function(entry.get()))
search_button.place(relx=0.78, rely=0.15, relwidth=0.17, relheight=0.1)

copy_button = tk.Button(frame, font=font_, bg=button_color, text="Copy", command=copy_to_clipboard)
copy_button.place(relx=0.05, rely=0.3, relwidth=0.4, relheight=0.1)

clear_button = tk.Button(frame, font=font_, bg=button_color, text="Clear", command=clear_entry)
clear_button.place(relx=0.55, rely=0.3, relwidth=0.4, relheight=0.1)

label = tk.Label(frame, bg=canvas_color, text="Enter location to search:", font=font_)
label.place(relx=0.05, rely=0.05)

entry.bind("<Return>", on_enter)

# Notification label
notification_label = tk.Label(root, text="", font=("Roboto", 12), fg="green")
notification_label.pack(pady=10)

root.mainloop()
