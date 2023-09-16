# KeyMou

### 功能列表

- [x] 鼠标和键盘操作监听
- [x] 鼠标 左右中键单击 / 左键双击 / 拖拽 的回放
- [x] 鼠标滚轮上下滚动回放
- [x] 键盘操作回放
    - [x] 支持字母和数字输入
    - [x] 支持部分 Ctrl 和 Shift [组合键输入](1_Code/Header.py)
    - [x] 支持部分特殊字符输入
- [ ] 文字识别
- [ ] 任务进度提示

### 使用方法

1. 使用环境： Windows + Python3
```powershell
PS C:\Users\ZHJ\Desktop\KeyMou> python -V
Python 3.11.5
```

2. 安装依赖
```
PS C:\Users\ZHJ\Desktop\KeyMou> pip install pynput==1.7.6
Requirement already satisfied: pynput==1.7.6 in d:\python3\install\lib\site-packages (1.7.6)
Requirement already satisfied: six in d:\python3\install\lib\site-packages (from pynput==1.7.6) (1.16.0)
```

3. 运行监听程序，录制需要执行的动作
```
PS C:\Users\ZHJ\Desktop\KeyMou\1_Code> python .\Listener.py
开始运行，日志文件将保存到: ../2_Log/print_log_20230916_182145.txt   # 这里是录制的监听日志路径
按下 ESC 键并晃动鼠标停止监听...
程序结束
```

4. 修改 Executer.py 文件中第 7 行的监听日志路径
```
--→ PRINT_LOG_PATH = "../2_Log/print_log_20230916_181238.txt"
```

5. 运行执行程序，回放监听器录制的操作
```
PS C:\Users\ZHJ\Desktop\KeyMou\1_Code> python .\Executer.py
```

### 工程结构

**Listener.py `--监听/生成操作日志--→` Decoder.py `--解析日志内容--→` Executer.py `--执行日志操作--→` 回放操作日志**

```
KeyMou
├─ 1_Code
│  ├─ Controller.py --→ 仅测试用
│  ├─ DataStruct.py --→ 键盘鼠标操作结构体
│  ├─ Decoder.py    --→ 译码器用于解析操作命令
│  ├─ Executer.py   --→ 执行器用于执行操作命令
│  ├─ Header.py     --→ 存放一些公共文件
│  └─ Listener.py   --→ 监听器用于获取键鼠操作
└─ 2_Log            --→ 存放操作日志文件
```

### 目前已知 Bug

* 无法处理的按键包括 `,`、`=`、`'`，问题定位 `decode_operate()`
