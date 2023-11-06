# Img2PDF


## 中文简介

你可以使用这个工具将若干图片文件直接生成一个pdf文件, 方便传输/展示等用途. 

## English Introduction

You can use this tool to generate a PDF file directly from several image files, which is convenient for transfer/display purposes.

---

## How to use?

### Easy to do:
```bash
python main.py
```
This will use such as `File Explorer (Windows)` or `Finder (MacOS)` to choose images.

## Use Args :
`-f, --files`: Several images path, must be image like `*.png`,`*.jpg`,`*.jpeg`,`*.gif`,`*.bmp`

`-n, --name`: The name of output file. No matter you use `sample` or `sample.pdf`, it will be `sample.pdf`.

### Use Package
```python
from img2pdf import img2pdf

img2pdf(imgs_path, output_name="output.pdf")
```

---

# TO DO

## Now

- ~~更新以命令行参数的方式选择图片~~
- ~~更新基于系统提供的接口方式通过文件管理器/Finder选择图片~~

## Maybe

- 可选的pdf页面大小格式
- 打包exe运行文件(Windows)