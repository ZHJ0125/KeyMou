# 本文件负责执行解析完毕的键鼠操作命令

import Decoder
import Header
import pynput
import time

DELAY_SECOND = 0.012    # 每步骤操作延时
PRINT_LOG_PATH = "../2_Log/KeyMou_log_20230917_012126.txt"   # 双击、单击、拖动、移动、字母数字按键

# ----------------------------------------------------------
def main():

    # 打开 Listener 录制的日志文件
    fileHandler = open(PRINT_LOG_PATH, "r")

    while True:
        text_line = fileHandler.readline()  # 逐行解析
        if not text_line:
            break
        # print(text_line.strip())
        # decode_type 函数解析出操作类型和操作指令
        EventType, Operate = Decoder.decode_type(text_line.strip())
        print("EventType=" + EventType + " Operate=" + Operate)
        # 不符合规定操作类型的操作会被指定为 BadString 类型
        if(EventType != "BadString"):
            # decode_type 函数解析操作指令并赋值给对应的 DataStruct 对象
            Decoder.decode_operate(EventType, Operate)
            if(EventType == "Move" or "Click" or "Scroll"):
                exec_mouse(EventType)
            # 处理键盘相关指令
            if(EventType == "Press" or "Release"):
                exec_keyboard(EventType)

    fileHandler.close()
# ----------------------------------------------------------

# exec_mouse 函数处理鼠标相关指令
def exec_mouse(EventType):
    ctr = pynput.mouse.Controller()
    # 移动鼠标操作
    if(EventType == "Move"):
        ctr.position = (Header.MoveOperate.x, Header.MoveOperate.y)
        time.sleep(DELAY_SECOND)
    # 点击鼠标操作
    elif(EventType == "Click"):
        ctr.position = (Header.ClickOperate.x, Header.ClickOperate.y)   # 先移动到点击位置
        time.sleep(DELAY_SECOND)
        if(Header.ClickOperate.pressed == "True"):      # 判断为"按下"操作
            if(Header.ClickOperate.button == "Button.left"):        # 左键按下
                ctr.press(pynput.mouse.Button.left)
            elif(Header.ClickOperate.button == "Button.right"):     # 右键按下
                ctr.press(pynput.mouse.Button.right)
            elif(Header.ClickOperate.button == "Button.middle"):    # 滚轮按下
                ctr.press(pynput.mouse.Button.middle)
        elif(Header.ClickOperate.pressed == "False"):   # 判断为"松开"操作
            if(Header.ClickOperate.button == "Button.left"):        # 左键松开
                ctr.release(pynput.mouse.Button.left)
            elif(Header.ClickOperate.button == "Button.right"):     # 右键松开
                ctr.release(pynput.mouse.Button.right)
            elif(Header.ClickOperate.button == "Button.middle"):    # 滚轮松开
                ctr.release(pynput.mouse.Button.middle)
    # 鼠标滚动操作
    elif(EventType == "Scroll"):
        ctr.position = (Header.ScrollOperate.x, Header.ScrollOperate.y)   # 先移动到滚轮位置
        time.sleep(DELAY_SECOND*2)
        # print("dx = " + Header.ScrollOperate.dx + ", dy = " + Header.ScrollOperate.dy)
        ctr.scroll(Header.ScrollOperate.dx, int(Header.ScrollOperate.dy)) # 直接滚动
        time.sleep(DELAY_SECOND*2)

# exec_keyboard 函数处理键盘相关指令
def exec_keyboard(EventType):
    ctr = pynput.keyboard.Controller()

    if(EventType == "Press"):   # 按键被按下
        print("按键按下：" + Header.PressOperate.key)
        try:                    # 找字典里有没有匹配的键值对
            SearchMapResult = Header.keyboard_map.get(Header.PressOperate.key, "NOT_FOUND")
            if(SearchMapResult == "NOT_FOUND"):         # 字典里没有匹配字符
                ctr.press(Header.PressOperate.key)      # 按照普通字母和数字处理
            else:                                       # 否则按照字典映射处理
                print("===== 字典中找到的对应值为：" + SearchMapResult)
                ctr.press(SearchMapResult)
        except:     # 抛出异常就尝试按照特殊字符处理
            if(Header.PressOperate.key == "Key.enter"):
                ctr.press(pynput.keyboard.Key.enter)
            elif(Header.PressOperate.key == "Key.ctrl_l"):
                ctr.press(pynput.keyboard.Key.ctrl_l)
            elif(Header.PressOperate.key == "Key.backspace"):
                ctr.press(pynput.keyboard.Key.backspace)
            elif(Header.PressOperate.key == "Key.space"):
                ctr.press(pynput.keyboard.Key.space)
            elif(Header.PressOperate.key == "Key.shift"):
                ctr.press(pynput.keyboard.Key.shift)
            elif(Header.PressOperate.key == "Key.esc"):
                ctr.press(pynput.keyboard.Key.esc)
            else:
                print("\033[93m[Warning]\033[0m: 遇到无法处理的字符：" + Header.PressOperate.key)
        time.sleep(0.1)

    elif(EventType == "Release"):   # 按键松开，相同处理方式
        print("按键松开：" + Header.ReleaseOperate.key)
        try:
            SearchMapResult = Header.keyboard_map.get(Header.ReleaseOperate.key, "NOT_FOUND")
            if(SearchMapResult == "NOT_FOUND"):             # 字典里没有匹配字符
                ctr.release(Header.ReleaseOperate.key)      # 按照普通字母和数字处理
            else:                                           # 否则按照字典映射处理
                print("======= 字典中找到的对应值为：" + SearchMapResult)
                ctr.release(SearchMapResult)
        except:     # 抛出异常尝试按照特殊字符处理
            if(Header.ReleaseOperate.key == "Key.enter"):
                ctr.release(pynput.keyboard.Key.enter)
            elif(Header.ReleaseOperate.key == "Key.ctrl_l"):
                ctr.release(pynput.keyboard.Key.ctrl_l)
            elif(Header.ReleaseOperate.key == "Key.backspace"):
                ctr.release(pynput.keyboard.Key.backspace)
            elif(Header.ReleaseOperate.key == "Key.space"):
                ctr.release(pynput.keyboard.Key.space)
            elif(Header.ReleaseOperate.key == "Key.shift"):
                ctr.release(pynput.keyboard.Key.shift)
            elif(Header.ReleaseOperate.key == "Key.esc"):
                ctr.release(pynput.keyboard.Key.esc)
            else:
                print("\033[93m[Warning]\033[0m: 遇到无法处理的字符：" + Header.ReleaseOperate.key)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
