from cnocr import CnOcr
from PIL import ImageGrab
from Header import ocr_valid_range
from json import loads, dumps
from os import remove, path
import time

OCR_IMAGE_SAVE_PATH = '../3_Docs/examples/temp.jpg'

def main():
    # start_time = time.time()
    if(OCR_Specific_Region("CDTU_Toolkit_Login_Status") == "未登录"):
        print("\033[34m[Info]\033[0m: 登录状态: 未登录")
    if(OCR_Specific_Region("CDTU_Toolkit_NetConnect_Status") == "关"):
        print("\033[34m[Info]\033[0m: 网络状态: 关")
    # end_time = time.time()
    # print('\n ==== OCR cost time: {} ===='.format(end_time-start_time))


def OCR_Specific_Region(ocr_range_str):
    # 检查参数是否为有效区域
    ocr_check_result = ocr_valid_range.get(ocr_range_str, "NOT_FOUND")
    if(ocr_check_result == "NOT_FOUND"):
        print("\033[93m[Warning]\033[0m: 无效的字符识别区域")
    else:
        # 截取指定区域图像并存储
        screenshot = ImageGrab.grab(bbox = ocr_check_result)
        screenshot.save(OCR_IMAGE_SAVE_PATH)

        # 识别截取图片的文字内容
        ocr = CnOcr()  # 所有参数都使用默认值
        out = ocr.ocr_for_single_line(OCR_IMAGE_SAVE_PATH)  # 单行文字模型
        # print(type(out))    # <class 'dict'>

        # 格式化识别结果并输出识别内容
        ocr_result = loads(dumps(out))
        # print("\033[35m[Debug]\033[0m: 识别结果: " + ocr_result["text"])

        # # 删除临时截图文件
        # if(path.isfile(OCR_IMAGE_SAVE_PATH)):
        #     remove(OCR_IMAGE_SAVE_PATH) # 删除临时文件
        #     print("\033[34m[Info]\033[0m: File \"" + OCR_IMAGE_SAVE_PATH + "\" Removed.")

        return ocr_result["text"]

if __name__ == "__main__":
    main()