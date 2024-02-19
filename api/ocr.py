# 导入所需库
from paddleocr import PaddleOCR



def test():
    # 初始化PaddleOCR
    ocr = PaddleOCR(use_angle_cls=True, lang="ch", page_num=0)

    # 读取PDF文件
    pdf_file = r"D:\111.pdf"

    # 使用PaddleOCR识别PDF中的文本
    result = ocr.ocr(pdf_file, cls=True)

    # 输出识别结果
    for line in result:
        print(line[-1][0])

if __name__ == '__main__':
    test()

