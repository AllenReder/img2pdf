from img2pdf import img2pdf
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('imgs_path', type=str, nargs='*', help='文件地址列表')
args = parser.parse_args()

imgs_path = args.imgs_path

if __name__ == "__main__":
    if not imgs_path:
        print("未提供图片路径")
        exit(0)
    img2pdf(imgs_path, "output.pdf")