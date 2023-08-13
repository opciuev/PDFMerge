# 我希望使用Python实现一个图片合并为PDF文件的小程序
# 1. 指定一个路径，路径下有很多文件夹，每个文件夹下有很多图片
# 2. 将每个文件夹下的图片合并为一个PDF文件，PDF文件名为文件夹名
# 3. 需要书签，书签就是图片名
# 举个例子
# 1. 指定路径为C:\macshare\DLRAW.NET-Tsugumomo vol 01-30\DLRAW.NET-Tsugumomo v01-02
# 2. C:\macshare\DLRAW.NET-Tsugumomo vol 01-30\DLRAW.NET-Tsugumomo v01-02下有文件夹“DLRAW.NET-[浜田よしかづ] つぐもも 第01巻”，“DLRAW.NET-[浜田よしかづ] つぐもも 第02巻”
# 3. “DLRAW.NET-[浜田よしかづ] つぐもも 第01巻”下有图片“DLRAW.NET-0001.jpg”，“DLRAW.NET-0002.jpg”
# 下面开始写代码
import os
import tkinter as tk
from tkinter import filedialog
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

            c.drawImage(image_path, 0, 0, width=img_width, height=img_height)
            c.showPage()

        c.save()

    def convert_to_pdf(self):
        if not self.image_folder or not self.output_folder:
            return

        self.merge_images_to_pdf()
        tk.messagebox.showinfo("Conversion Complete", "Images have been converted to PDF.")

def main():
    root = tk.Tk()
    app = ImageToPdfConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
