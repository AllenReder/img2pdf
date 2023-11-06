from img2pdf import img2pdf
import argparse
import tkinter as tk
from tkinter import filedialog

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--files', type=str, nargs='+', help='图片地址列表')
parser.add_argument('-n', '--name', type=str, help='输出文件名称')
args = parser.parse_args()


if __name__ == "__main__":
    output_name = "output.pdf" # 默认输出文件名
    if args.name:
        output_name = args.name # 使用用户自定义文件名
        # 是否需要补全后缀名
        if not output_name.endswith(".pdf"):
            output_name += ".pdf"
    
    if args.files: # 通过命令行选择图片
        imgs_path = args.files
        img2pdf(imgs_path, output_name)
    else: # 通过系统调用选择图片
        root = tk.Tk()
        root.withdraw()
        imgs_path = filedialog.askopenfilenames(title="选择图片文件", 
            filetypes=(("图片文件", "*.png *.jpg *.jpeg *.gif *.bmp"), ("所有文件", "*.*")))
        img2pdf(imgs_path, output_name)