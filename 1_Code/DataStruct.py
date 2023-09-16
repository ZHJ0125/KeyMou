class MoveStruct():
    def __init__(self):
        self.x = 0
        self.y = 0
class ClickStruct():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.button = ""        # Button.left | Button.right | Button.middle
        self.pressed = ""       # True | False
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

