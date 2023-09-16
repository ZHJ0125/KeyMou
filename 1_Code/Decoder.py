# 本文件负责解析由 Listener.py 录制的监听日志文件

import Header

PRINT_LOG_PATH = "../2_Log/print_log_20230915_200110.txt"

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
            if(EventType == "Move"):
                # pass
                print(Header.MoveOperate.x, Header.MoveOperate.y)
            elif(EventType == "Click"):
                # pass
                print(Header.ClickOperate.x, Header.ClickOperate.y, Header.ClickOperate.button, Header.ClickOperate.pressed)
            elif(EventType == "Scroll"):
                # pass
                print(Header.ScrollOperate.x, Header.ScrollOperate.y, Header.ScrollOperate.dx, Header.ScrollOperate.dy)
            elif(EventType == "Press"):
                # pass
                print(Header.PressOperate.key)
            elif(EventType == "Release"):
                # pass
                print(Header.ReleaseOperate.key)

    fileHandler.close()
# ----------------------------------------------------------


# 处理操作符字符串，获取有效信息
def decode_operate(EventTypeStr, OperateStr):
    # 将字符串中无效字符去除
    removeStr  = "=,'"
    replaceStr = "   "
    table=str.maketrans(removeStr, replaceStr)
    Operate = OperateStr.translate(table).split()
    print(Operate)

    if(EventTypeStr == "Move"):
        Header.MoveOperate.x = Operate[1]  # x 坐标
        Header.MoveOperate.y = Operate[3]  # y 坐标
        # print(Header.MoveOperate.x, Header.MoveOperate.y)

    elif(EventTypeStr == "Click"):
        Header.ClickOperate.x = Operate[1]
        Header.ClickOperate.y = Operate[3]
        Header.ClickOperate.button = Operate[5]
        Header.ClickOperate.pressed = Operate[7]
        # print(Header.ClickOperate.x, Header.ClickOperate.y, Header.ClickOperate.button, Header.ClickOperate.pressed)

    elif(EventTypeStr == "Scroll"):
        Header.ScrollOperate.x = Operate[1]
        Header.ScrollOperate.y = Operate[3]
        Header.ScrollOperate.dx = Operate[5]
        Header.ScrollOperate.dy = Operate[7]
        # print(Header.ScrollOperate.x, Header.ScrollOperate.y, Header.ScrollOperate.dx, Header.ScrollOperate.dy)

    elif(EventTypeStr == "Press"):
        Header.PressOperate.key = Operate[1]
        # print(Header.PressOperate.key)

    elif(EventTypeStr == "Release"):
        Header.ReleaseOperate.key = Operate[1]
        # print(Header.ReleaseOperate.key)
# ----------------------------------------------------------
    

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
# ----------------------------------------------------------

if __name__ == "__main__":
    # decode_type("Click(x=752, y=231, button=Button.left, pressed=True)")
    # decode_operate("Click", "x=752, y=231, button=Button.left, pressed=True")
    main()
