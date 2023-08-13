import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ImageToPdfConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to PDF Converter")

        self.select_folder_button = tk.Button(self.root, text="Select Image Folder", command=self.select_image_folder)
        self.select_folder_button.pack()

        self.select_output_button = tk.Button(self.root, text="Select Output Folder", command=self.select_output_folder)
        self.select_output_button.pack()

        self.convert_button = tk.Button(self.root, text="Convert to PDF", command=self.convert_to_pdf)
        self.convert_button.pack()

        self.image_folder = ""
        self.output_folder = ""

    def select_image_folder(self):
        self.image_folder = filedialog.askdirectory(title="Select Image Folder")

    def select_output_folder(self):
        self.output_folder = filedialog.askdirectory(title="Select Output Folder")

    def merge_images_to_pdf(self):
        folder_name = os.path.basename(self.image_folder)
        pdf_filename = os.path.join(self.output_folder, f"{folder_name}.pdf")

        image_files = [f for f in os.listdir(self.image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        image_files.sort()

        c = canvas.Canvas(pdf_filename, pagesize=letter)

        for image_file in image_files:
            image_path = os.path.join(self.image_folder, image_file)
            img = Image.open(image_path)
            img_width, img_height = img.size

            c.setPageSize((img_width, img_height))
            c.drawImage(image_path, 0, 0, width=img_width, height=img_height)
            c.showPage()

        c.save()

    def convert_to_pdf(self):
        if not self.image_folder or not self.output_folder:
            return

        self.merge_images_to_pdf()
        messagebox.showinfo("Conversion Complete", "Images have been converted to PDF.")

def main():
    root = tk.Tk()
    app = ImageToPdfConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()