# very simple ascii art generator
# don't expect miracles

import os
from PIL import Image

def get_gray_value(r, g, b):
    # 将RGB值转换为灰度值
    return int(0.299 * r + 0.587 * g + 0.114 * b)

def convert_to_ascii(image):
    # 创建一个字符集，灰度值将被映射到这些字符上
    ascii_chars = "@%#*+=-:. "
    width, height = image.size
    scale = 255 // (len(ascii_chars) - 1)
    ascii_image = ""

    # 遍历图片的每个像素
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            gray_value = get_gray_value(r, g, b)
            index = gray_value // scale
            ascii_image += ascii_chars[index]
        ascii_image += "\n"
    
    return ascii_image


def save_pic_as_ascii(image_path="", save_path="", print_to_console=False):
    # 打开图片并转换为灰度
    if image_path == "":
        image_path = r"game/resources/negi-miku.png" 

    image_name = os.path.basename(image_path)

    image = Image.open(image_path).convert("RGB")

    # 调整图片大小，这里设置为宽度为80字符
    width, height = image.size
    aspect_ratio = height / width
    new_width = 80
    new_height = aspect_ratio * new_width * 0.5  # 0.5是为了调整字符的高度与宽度比例
    resized_image = image.resize((int(new_width), int(new_height)))

    # 转换为ASCII艺术
    ascii_art = convert_to_ascii(resized_image)
    
    # 终端输出ASCII艺术
    if print_to_console:
        print(ascii_art)
    
    # save ascii_art to save_path
    save_name = image_name + "-ascii_art.txt"
    if save_path == "":
        save_path = os.path.join(os.path.dirname(image_path), save_name)
    with open(save_path, "w") as f:
        f.write(ascii_art)
        

