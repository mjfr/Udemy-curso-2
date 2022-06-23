# TODO 1 - Build a watermarking software.
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

images_files = None
watermark_file = None

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
    watermark = Image.open(watermark_file)
    return ImageTk.PhotoImage(watermark)


# Image(s) Upload
def upload_images():
    global images_files
    images_files = filedialog.askopenfilenames(title="Choose your image(s)")
    # Image canvas
    for img in images_files:
        image = Image.open(img)
        image_canvas_sized = image.resize((500, 500), Image.Resampling.LANCZOS)
        canvas_image = ImageTk.PhotoImage(image_canvas_sized)
        window.canvas_image = canvas_image
        canvas.create_image((0, 0), image=canvas_image, anchor="nw")
    return images_files


def apply_watermark():
    for img in images_files:
        image = Image.open(img)
        watermark = Image.open(watermark_file)
        image.paste(watermark, (image.size[0]//3, image.size[1]//3), watermark)
        image.save(f"{img}_watermarked.png", "PNG")


def reset_uploads():
    global watermark_file, images_files, canvas
    watermark_file = None
    images_files = None
    canvas.delete("all")


# Screen
# Buttons
upload_watermark_button = tk.Button(text="Upload Watermark", command=lambda: watermark_file == upload_watermark())
upload_watermark_button.grid(column=0, row=1)

# To assign a value to watermark_file using lambda we need to use == instead of = when using lambda expression.
upload_images_button = tk.Button(text="Upload your image(s)", command=lambda: images_files == upload_images())
upload_images_button.grid(column=3, row=1)

reset_uploads = tk.Button(text="Reset all", command=reset_uploads)
reset_uploads.grid(column=2, row=3)

# If the watermark_entry is still the same: "Or you can type a watermark text", it will consider only the upload
# It will only be used if there is no uploaded watermark image.
watermark_button = tk.Button(text="Watermark it!", command=apply_watermark)
watermark_button.grid(column=3, row=3)

# Entry
watermark_entry = tk.Entry(width=50)
watermark_entry.insert(0, "Or you can type a watermark text")
watermark_entry.bind("<FocusIn>", lambda args: watermark_entry.delete("0", "end"))
watermark_entry.grid(column=1, row=1)

# Empty Canvas
canvas = tk.Canvas(width=500, height=500, bg=None, highlightthickness=0)
canvas.grid(column=0, row=2, columnspan=2, rowspan=2, padx=20, pady=20, sticky=tk.E)

window.mainloop()
