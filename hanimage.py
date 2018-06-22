import os
import string
### 中文处理
from zhon import hanzi
from PIL import Image, ImageDraw, ImageFont, ImageFilter

start_cn, end_cn = (0x4E00, 0x9FA5)
start_en, end_en = (0xFF21, 0xFF5A)

chinese_dir = 'chinese'
if not os.path.exists(chinese_dir):
    os.mkdir(chinese_dir)


def hanzi_image(code, width=128, height=128):
    # 创建Image对象
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象
    font = ImageFont.truetype('arialuni.ttf', 36)
    # font = ImageFont.truetype(size=32)
    # 创建Draw对象
    draw = ImageDraw.Draw(image)
    # 随机颜色填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=(255, 255, 255))
    # 验证码写到图片上
    draw.text(xy=(40, 40), text=code, font=font, fill=0)
    # 模糊滤镜
    # image = image.filter(ImageFilter.BLUR)
    return code, image


i = 0
digits = string.digits
pun = string.punctuation
hanzi_pun = hanzi.punctuation
for i in range(len(digits)):
    if digits[i] is not None:
        if digits[i] != '':
            code, image = hanzi_image(digits[i])
            print(code)
            image.save(chinese_dir + '/' + code + '.jpeg')
for i in range(len(pun)):
    if pun[i] is not None:
        if pun[i] != '':
            code, image = hanzi_image(pun[i])
            print(code)
            if code == '.':
                code = '点号'
            if code == '/':
                code = '反斜划线'
            image.save(chinese_dir + '/' + code + '.jpeg')
for i in range(len(hanzi_pun)):
    if hanzi_pun[i] is not None:
        if hanzi_pun[i] != '':
            code, image = hanzi_image(hanzi_pun[i])
            print(code)
            image.save(chinese_dir + '/' + code + '.jpeg')
for codepoint in range(int(start_en), int(end_en) + 1):
    code, image = hanzi_image(chr(codepoint))
    print(code)
    image.save(chinese_dir + '/' + code + '.jpeg')
for codepoint in range(int(start_cn), int(end_cn) + 1):
    code, image = hanzi_image(chr(codepoint))
    print(code)
    image.save(chinese_dir + '/' + code + '.jpeg')
    # i = i + 1
    # if i == 5:
    #     break
