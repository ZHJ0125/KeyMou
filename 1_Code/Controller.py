import pynput
import time

def test():

    ctr = pynput.mouse.Controller()

    time.sleep(2)
    # ----------- 单击双击 ----------------
    # Click(x=1140, y=668, button=Button.left, pressed=True)
    # Click(x=1140, y=668, button=Button.left, pressed=True)
    # Click(x=1140, y=668, button=Button.left, pressed=True)
    # Click(x=1140, y=668, button=Button.right, pressed=True)
    ctr.click(pynput.mouse.Button.left)     #左键单击
    time.sleep(0.2)
    ctr.click(pynput.mouse.Button.left, 2)  #左键双击
    time.sleep(0.2)
    ctr.click(pynput.mouse.Button.right)    #右键单击
    time.sleep(0.2)

    # ------------- 拖动 ------------------
    # Click(x=1140, y=668, button=Button.left, pressed=True)
    # Click(x=1190, y=718, button=Button.left, pressed=False)
    # Scroll(x=1190, y=718, dx=0, dy=50)
    ctr.press(pynput.mouse.Button.left)     #按下左键
    time.sleep(0.2)
    ctr.move(50, 0)                         #右移50单位
    time.sleep(0.2)
    ctr.move(0, 50)                         #下移50单位
    time.sleep(0.2)
    ctr.release(pynput.mouse.Button.left)   #释放左键
    time.sleep(0.2)

    # ------------- 滚轮 -------------------
    # Scroll(x=1190, y=718, dx=0, dy=50)
    # Scroll(x=1190, y=718, dx=0, dy=-50)
    ctr.scroll(0, 50)                       #向上滚动50单位
    time.sleep(0.2)
    ctr.scroll(0, -50)                      #向下滚动50单位
    time.sleep(0.2)

def mouse_test():
    
    ctr = pynput.mouse.Controller()
    time.sleep(5)

    # ------------------- 双击测试 ---------------------------
    # Click(x=501, y=14, button=Button.left, pressed=True)
    # Click(x=501, y=14, button=Button.left, pressed=False)
    ctr.position = (501, 14)  # 移动到标题栏
    time.sleep(1)
    ctr.click(pynput.mouse.Button.left, 2)  # 双击
    time.sleep(0.5)

    # ------------------- 拖动测试 ---------------------------
    # Move(x=501, y=14)
    # Click(x=501, y=14, button=Button.left, pressed=True)
    # Move(x=501, y=14)
    # ......
    # Move(x=728, y=448)
    # Click(x=729, y=449, button=Button.left, pressed=False)
    # Click(x=729, y=449, button=Button.left, pressed=True)
    # Move(x=730, y=448)
    # ......
    # Move(x=957, y=250)
    # Click(x=957, y=250, button=Button.left, pressed=False)
    ctr.position = (501, 14)  # 移动到标题栏
    time.sleep(0.5)
    ctr.press(pynput.mouse.Button.left)     # 按下
    time.sleep(0.5)
    ctr.position = (728, 448)               # 拖动
    time.sleep(0.5)
    ctr.release(pynput.mouse.Button.left)   # 松开
    time.sleep(1)
    ctr.press(pynput.mouse.Button.left)
    time.sleep(0.5)
    ctr.position = (957, 250)
    time.sleep(0.5)
    ctr.release(pynput.mouse.Button.left)
    time.sleep(2)

def keyboard_test():

    ctr = pynput.keyboard.Controller()
    time.sleep(5)

    # Press and release space
    ctr.press(pynput.keyboard.Key.space)
    ctr.release(pynput.keyboard.Key.space)

    # Type a lower case A; this will work even if no key on the
    # physical keyboard is labelled 'A'
    ctr.press('a')
    ctr.release('a')

    # Type two upper case As
    ctr.press('A')
    ctr.release('A')
    with ctr.pressed(pynput.keyboard.Key.shift):
        ctr.press('a')
        ctr.release('a')

    # --------------- 按下100次HelloWorld ----------------
    # Type 'HelloWorld' using the shortcut type method
    ctr.type('HelloWorld\n')

    with ctr.pressed(pynput.keyboard.Key.ctrl_l):
        ctr.press('a')
        ctr.release('a')
    with ctr.pressed(pynput.keyboard.Key.ctrl_l):
        ctr.press('c')
        ctr.release('c')
    for i in range(100):
        # ctr.type('Send'+str(i+1)+"/100：")
        ctr.type("Send %3s/100: " % str(i+1))
        with ctr.pressed(pynput.keyboard.Key.ctrl_l):
            ctr.press('v')
            ctr.release('v')
        time.sleep(0.05)
    
    ctr.press(pynput.keyboard.Key.enter)
    ctr.release(pynput.keyboard.Key.enter)

def main():
    pass
    # mouse_test()        # 双击+拖动
    # keyboard_test()     # 输出字符

if __name__ == "__main__":
    main()
