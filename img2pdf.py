from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def img2pdf(image_path, output_name="output.pdf"):
    """
    Integrate pictures into a pdf file.
    Args:
        image_path: A list of image paths.
        output_name: The name of the output pdf file.
    """

    output_pdf = output_name  # 指定生成的PDF文件名
    c = canvas.Canvas(output_pdf, pagesize=letter)  # 打开一个PDF文件，并设置页面大小

    for image_file in image_path:
        print(f"正在处理图片文件 '{image_file}' ...")
        img = Image.open(image_file)  # 打开每个图片文件
        width, height = img.size  # 获取图片的宽度和高度

        # 将图片添加到PDF页面，确保图片与页面大小一致
        c.setPageSize((width, height))
        c.drawImage(image_file, 0, 0, width, height)

        c.showPage()  # 添加新页面

    # 保存生成的PDF文件
    c.save()

    print(f"PDF文件 '{output_pdf}' 已创建成功。")
