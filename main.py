from img2pdf import img2pdf

image_files = ["imgs/img1.png", "imgs/img2.png", "imgs/img3.png", "imgs/img4.png", "imgs/img5.png"]

if __name__ == "__main__":
    img2pdf(image_files, "output.pdf")