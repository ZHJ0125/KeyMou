# 鼠标和键盘移动记录：
# Move(x=752, y=231)
# Click(x=752, y=231, button=Button.left, pressed=True)
# Click(x=752, y=231, button=Button.left, pressed=False)
# Scroll(x=752, y=231, dx=0, dy=1)
# Scroll(x=752, y=231, dx=0, dy=-1)
# Click(x=752, y=231, button=Button.middle, pressed=True)
# Click(x=752, y=231, button=Button.middle, pressed=False)
# Click(x=753, y=231, button=Button.right, pressed=True)
# Click(x=753, y=231, button=Button.right, pressed=False)
# Press(key='q')
# Release(key='q')
# Press(key='w')
# Release(key='w')
# Press(key='1')
# Release(key='1')
# Press(key=Key.esc)
# Bye

PRINT_LOG_PATH = "../2_Log/print_log_20230915_200110.txt"

class MoveStruct():
    def __init__(self):
        self.x = 0
        self.y = 0
class ClickStruct():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.button = ""
        self.pressed = ""
class ScrollStruct():
    def __init__(self) -> None:
        self.x  = 0
        self.y  = 0
        self.dx = 0
        self.dy = 0
class PressStruct():
    def __init__(self) -> None:
        self.key = ""
class ReleaseStruct():
    def __init__(self) -> None:
        self.key = ""

# ----------------------------------------------------------
def main():

    fileHandler = open(PRINT_LOG_PATH, "r")

    while True:
        text_line = fileHandler.readline()
        if not text_line:
            break
        # print(text_line.strip())
        EventType, Operate = decode_type(text_line.strip())
        print("EventType=" + EventType + " Operate=" + Operate)
        if(EventType != "BadString"):
            decode_operate(EventType, Operate)

    fileHandler.close()
# ----------------------------------------------------------


# 处理操作符字符串，获取有效信息
def decode_operate(EventTypeStr, OperateStr):
    # 将字符串中无效字符去除
    removeStr  = "=,"
    replaceStr = "  "
    table=str.maketrans(removeStr, replaceStr)
    Operate = OperateStr.translate(table).split()
    print(Operate)

    if(EventTypeStr == "Move"):
        MoveOperate = MoveStruct()
        MoveOperate.x = Operate[1]  # x 坐标
        MoveOperate.y = Operate[3]  # y 坐标
        print(MoveOperate.x, MoveOperate.y)

    elif(EventTypeStr == "Click"):
        ClickOperate = ClickStruct()
        ClickOperate.x = Operate[1]
        ClickOperate.y = Operate[3]
        ClickOperate.button = Operate[5]
        ClickOperate.pressed = Operate[7]
        print(ClickOperate.x, ClickOperate.y, ClickOperate.button, ClickOperate.pressed)
    
    elif(EventTypeStr == "Scroll"):
        ScrollOperate = ScrollStruct()
        ScrollOperate.x = Operate[1]
        ScrollOperate.y = Operate[3]
        ScrollOperate.dx = Operate[5]
        ScrollOperate.dy = Operate[7]
        print(ScrollOperate.x, ScrollOperate.y, ScrollOperate.dx, ScrollOperate.dy)

    elif(EventTypeStr == "Press"):
        PressOperate = PressStruct()
        PressOperate.key = Operate[1]
        print(PressOperate.key)

    elif(EventTypeStr == "Release"):
        ReleaseOperate = ReleaseStruct()
        ReleaseOperate.key = Operate[1]
        print(ReleaseOperate.key)
    


# 处理字符串，返回值：
#   1. 事件类型："Move", "Click", "Scroll", "Press", "Release", "BadString"
#   2. 操作内容
def decode_type(encoder_text):

    EventFlag = False
    EventsType = ("Move", "Click", "Scroll", "Press", "Release")

    for Event in EventsType:
        if(Event in encoder_text):
            print(encoder_text + "符合事件类型: " + Event)
            EventFlag = True
            break
    if(EventFlag):
        str = encoder_text.lstrip(Event).lstrip('(').rstrip(')')
        # print("EventType=" + Event + " Operate=" + str)
        return(Event, str)
    else:
        return("BadString","NULL")
      

if __name__ == "__main__":
    # decode_type("Click(x=752, y=231, button=Button.left, pressed=True)")
    # decode_operate("Click", "x=752, y=231, button=Button.left, pressed=True")
    main()
