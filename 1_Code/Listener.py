# 本文件负责监听键鼠操作并生成可供回放的日志文件

import pynput
from threading import Thread
import sys, time

PRINT_LOG_PATH = "../2_Log/KeyMou_log_" + time.strftime("%Y%m%d_%H%M%S") + ".txt"
run_threads_flag = True  # 线程允许运行标志

class MyListener():

    # 获取按键状态
    def Keyboard_Get(self):
        global run_threads_flag
        while run_threads_flag:
            with pynput.keyboard.Events() as keyboard_event:
                key_get = keyboard_event.get()
            if isinstance(key_get, pynput.keyboard.Events.Event):
                print(key_get)
                # ESC键结束程序
                if(key_get.key is pynput.keyboard.Key.esc):
                    run_threads_flag = False
                    print("Bye")

    # 获取鼠标移动状态
    def Mouse_Get(self):
        # global run_threads_flag
        while run_threads_flag:
            with pynput.mouse.Events() as mouse_event:
                move_get = mouse_event.get()
            if (isinstance(move_get, pynput.mouse.Events.Event) and run_threads_flag):
                print(move_get)


# main 函数监听鼠标和键盘的操作记录，并生成用于回放的日志文件
def main():

    print("开始运行，日志文件将保存到: \"\033[92m" + PRINT_LOG_PATH + "\033[0m\"")
    print("按下 \033[91mESC\033[0m 键并 \033[91m晃动鼠标\033[0m 停止监听...")
    # 标准输出改成输出到文件
    source_stdout = sys.stdout
    print_log = open(PRINT_LOG_PATH, "w+")
    sys.stdout = print_log
    print("鼠标和键盘移动记录 - " + PRINT_LOG_PATH)

    # -----------------------------------------------
    # 创建两个线程分别监听鼠标和键盘的操作
    Keyboard_Thread = Thread(target=MyListener().Keyboard_Get)  # 键盘线程
    Mouse_Thread = Thread(target=MyListener().Mouse_Get)        # 鼠标线程

    # 启动线程运行
    Keyboard_Thread.start()
    Mouse_Thread.start()

    # 等待线程执行完毕
    Keyboard_Thread.join()
    Mouse_Thread.join()
    # -----------------------------------------------

    # 恢复标准输出流
    sys.stdout = source_stdout
    print_log.close()
    print("监听程序结束")

if __name__ == "__main__":
    main()
