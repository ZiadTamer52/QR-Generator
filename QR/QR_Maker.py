import customtkinter as ctk
import qrcode
from tkinter import filedialog
from PIL import Image

def generate_qr_code():
    text = entry.get()
    if text:
        qr_image = qrcode.make(text)
        return qr_image
    return None

def save_image():
    qr_image = generate_qr_code()
    if qr_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                   filetypes=[("PNG files", "*.png"),
                                                              ("JPEG files", "*.jpg"),
                                                              ("All files", "*.*")])
        if file_path:
            qr_image.save(file_path)
            print(f"تم حفظ الصورة في: {file_path}")

root = ctk.CTk()
root.title("QR-Generator")
root.geometry("500x300+400+150")
root.resizable(False, False)
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")


frame = ctk.CTkFrame(root, width=590, height=500)
frame.place(x=0, y=0)

word= ctk.CTkLabel(frame, text="QR-Generator", font=("Algerian", 37, "bold"))
word.place(x=109, y=45)

entry = ctk.CTkEntry(frame, width=395)
entry.place(x=54, y=130)

save_button = ctk.CTkButton(frame, text="Choose where to save the image", command=save_image)
save_button.place(x=150, y=200)

root.mainloop()