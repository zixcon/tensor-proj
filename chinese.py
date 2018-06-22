import codecs
import string
### 中文处理
from zhon import hanzi

start_cn, end_cn = (0x4E00, 0x9FA5)
# start_comma, end_comma = (0xEA84BF, 0xEAA980)
start_comma, end_comma = (0xA13F, 0xAA40)
start_en, end_en = (0xFF21, 0xFF5A)
with codecs.open("comma.txt", "w", "utf-8") as f:
    f.write(string.punctuation)
    f.write(string.digits)
    f.write(hanzi.punctuation)
    # for codepoint in range(int(start_comma), int(end_comma) + 1):
    #     f.write(chr(codepoint))
with codecs.open("chinese.txt", "w", "utf-8") as f:
    for codepoint in range(int(start_en), int(end_en) + 1):
        f.write(chr(codepoint))
    for codepoint in range(int(start_cn), int(end_cn) + 1):
        f.write(chr(codepoint))


