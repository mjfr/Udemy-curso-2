# TODO 1 - Build a watermarking software.
import os.path
import tkinter as tk
from tkinter import filedialog, messagebox
import PIL
from PIL import ImageTk, Image, ImageFont, ImageDraw

images_files = ""
watermark_file = ""

window = tk.Tk()
window.title("WmM - Watermark Marker")
window.config(padx=10, bg="gray")


# Logo
logo_canvas = tk.Canvas(width=420, height=200, bg="gray", highlightthickness=0)
logo_path = tk.PhotoImage(file="logo.png")
logo_canvas.create_image(205, 100, image=logo_path)
logo_canvas.grid(column=0, row=0, columnspan=4, pady=30)


# Uploads
# Watermark Upload
def upload_watermark():
    global watermark_file
    watermark_file = filedialog.askopenfilename(title="Choose your watermark file")


# Image(s) Upload
def upload_images():
    global images_files
    images_files = filedialog.askopenfilenames(title="Choose your image(s)")
    # Image canvas
    error_aux = 1
    for img in images_files:
        try:
            image = Image.open(img)
        except PIL.UnidentifiedImageError:
            if error_aux == 1:
                messagebox.showerror(title="Error",
                                     message="Only images are accepted. Any other formats like .mp3, .pdf, etc."
                                             " Will cause errors.")
                error_aux = 0
            continue
        finally:
            image_canvas_sized = image.resize((500, 500), Image.Resampling.LANCZOS)
            canvas_image = ImageTk.PhotoImage(image_canvas_sized)
            window.canvas_image = canvas_image
            canvas.create_image((0, 0), image=canvas_image, anchor="nw")


def check_entry():
    if watermark_entry.get() == "":
        return False
    if watermark_entry.get() == "Or you can type a watermark text":
        return False
    if watermark_entry.get() is None:
        return False
    return True


def apply_watermark():
    if check_entry():
        for img in images_files:
            try:
                image = Image.open(img)
            except PIL.UnidentifiedImageError:
                continue
            text_font = ImageFont.truetype("segoesc.ttf", 50)
            text = watermark_entry.get()
            watermark_image = ImageDraw.Draw(image)
            watermark_image.text((image.size[0]/3, image.size[1]/2.5), text, "#FF0000D9", font=text_font, angle=45)
            image.save(f"{img[:img.rfind('.')]}_watermarked.png")
        messagebox.showinfo(title="Done!",
                            message="All images were watermarked. Check them in the same directory of the "
                                    "original images.")
        os.startfile(os.path.realpath(img[:img.rfind("/")]))
        return None

    for img in images_files:
        try:
            image = Image.open(img)
        except PIL.UnidentifiedImageError:
            continue
        while True:
            try:
                watermark = Image.open(watermark_file)
            except AttributeError:
                messagebox.showwarning(title="No watermark selected",
                                       message="You need to upload or type your watermark first")
                upload_watermark()
                watermark = Image.open(watermark_file)
            finally:
                image.paste(watermark, (image.size[0]//3, image.size[1]//3), watermark)
                image.save(f"{img[:img.rfind('.')]}_watermarked.png")
                break
    messagebox.showinfo(title="Done!", message="All images were watermarked. Check them in the same directory of the "
                                               "original images.")
    os.startfile(os.path.realpath(img[:img.rfind("/")]))
    return None


def reset_uploads():
    global watermark_file, images_files, canvas
    watermark_file = ""
    images_files = ""
    canvas.delete("all")
    watermark_entry.delete(0, tk.END)
    messagebox.showinfo(title="Data reseted", message="The following items were reseted:\n-Upload Watermark (if any);"
                                                      "\n-Watermark textfield;\n-Any uploaded image.")


# Screen
# Buttons
upload_watermark_button = tk.Button(text="Upload Watermark", command=upload_watermark)
upload_watermark_button.grid(column=0, row=1, padx=30)

upload_images_button = tk.Button(text="Upload your image(s)", command=upload_images)
upload_images_button.grid(column=3, row=1, padx=30)

reset_uploads = tk.Button(text="Reset all", command=reset_uploads)
reset_uploads.grid(column=0, row=4, pady=20)

# If still with placeholder or empty, it will be ignored. It has priority over the watermark uploaded image.
watermark_button = tk.Button(text="Watermark it!", command=apply_watermark)
watermark_button.grid(column=3, row=4, pady=20)

# Entry
watermark_entry = tk.Entry(width=50, justify="center")
watermark_entry.insert(0, "Or you can type a watermark text")
watermark_entry.bind("<Button-1>",
                     lambda args: watermark_entry.delete(0, tk.END)
                     if(watermark_entry.get() == "Or you can type a watermark text") else None)
watermark_entry.grid(column=1, row=1, columnspan=2)

# Empty Canvas
canvas = tk.Canvas(width=500, height=500, highlightthickness=0)
canvas.grid(column=1, row=2, columnspan=2, rowspan=2, padx=20, pady=20)

window.mainloop()
