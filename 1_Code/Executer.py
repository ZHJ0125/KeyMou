import Decoder
import Header
import pynput
import time

DELAY_SECOND = 0.015    # 每步骤操作延时
PRINT_LOG_PATH = "../2_Log/print_log_20230916_181238.txt"   # 双击、单击、拖动、移动

# ----------------------------------------------------------
def main():

    fileHandler = open(PRINT_LOG_PATH, "r")

    while True:
        text_line = fileHandler.readline()
        if not text_line:
            break
        # print(text_line.strip())
        EventType, Operate = Decoder.decode_type(text_line.strip())
        # print("EventType=" + EventType + " Operate=" + Operate)
        if(EventType != "BadString"):
            Decoder.decode_operate(EventType, Operate)
            if(EventType == "Move" or "Click" or "Scroll"):
                # print(Header.MoveOperate.x, Header.MoveOperate.y)
                exec_mouse(EventType, Operate)
            # elif(EventType == "Click"):
            #     # print(Header.ClickOperate.x, Header.ClickOperate.y, Header.ClickOperate.button, Header.ClickOperate.pressed)
            #     exec_mouse(EventType, Operate)
            # elif(EventType == "Scroll"):
            #     # print(Header.ScrollOperate.x, Header.ScrollOperate.y, Header.ScrollOperate.dx, Header.ScrollOperate.dy)
            #     exec_mouse(EventType, Operate)
            elif(EventType == "Press"):
                print(Header.PressOperate.key)
            elif(EventType == "Release"):
                print(Header.ReleaseOperate.key)
    fileHandler.close()
# ----------------------------------------------------------

def exec_mouse(EventType, Operate):
    ctr = pynput.mouse.Controller()
    # 移动鼠标操作
    if(EventType == "Move"):
        ctr.position = (Header.MoveOperate.x, Header.MoveOperate.y)
        time.sleep(DELAY_SECOND)
    # 点击鼠标操作
    elif(EventType == "Click"):
        ctr.position = (Header.ClickOperate.x, Header.ClickOperate.y)   # 先移动到点击位置
        time.sleep(DELAY_SECOND)
        if(Header.ClickOperate.pressed == "True"):    # 判断为"按下"操作
            if(Header.ClickOperate.button == "Button.left"):        # 左键按下
                ctr.press(pynput.mouse.Button.left)
            elif(Header.ClickOperate.button == "Button.right"):     # 右键按下
                ctr.press(pynput.mouse.Button.right)
            elif(Header.ClickOperate.button == "Button.middle"):    # 滚轮按下
                ctr.press(pynput.mouse.Button.middle)
        elif(Header.ClickOperate.pressed == "False"):
            if(Header.ClickOperate.button == "Button.left"):        # 左键松开
                ctr.release(pynput.mouse.Button.left)
            elif(Header.ClickOperate.button == "Button.right"):     # 右键松开
                ctr.release(pynput.mouse.Button.right)
            elif(Header.ClickOperate.button == "Button.middle"):    # 滚轮松开
                ctr.release(pynput.mouse.Button.middle)
    elif(EventType == "Scroll"):
        ctr.position = (Header.ScrollOperate.x, Header.ScrollOperate.y)   # 先移动到滚轮位置
        time.sleep(DELAY_SECOND*2)
        print("dx = " + Header.ScrollOperate.dx + ", dy = " + Header.ScrollOperate.dy)
        ctr.scroll(Header.ScrollOperate.dx, int(Header.ScrollOperate.dy)) # 直接滚动
        time.sleep(DELAY_SECOND*2)

if __name__ == "__main__":
    main()
