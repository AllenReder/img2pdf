from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# 定义图片文件列表
image_files = ["img1.png", "img2.png", "img3.png", "img4.png", "img5.png"]

# 指定生成的PDF文件名
output_pdf = "output.pdf"

# 打开一个PDF文件，并设置页面大小
c = canvas.Canvas(output_pdf, pagesize=letter)

for image_file in image_files:
    # 添加目录
    image_file = 'imgs/' + image_file

    # 打开每个图片文件
    img = Image.open(image_file)

    # 获取图片的宽度和高度
    width, height = img.size

    # 将图片添加到PDF页面，确保图片与页面大小一致
    c.setPageSize((width, height))
    c.drawImage(image_file, 0, 0, width, height)

    # 添加新页面
    c.showPage()

# 保存生成的PDF文件
c.save()

print(f"PDF文件 '{output_pdf}' 已创建成功。")
