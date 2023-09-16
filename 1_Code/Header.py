import DataStruct

MoveOperate = DataStruct.MoveStruct()
ClickOperate = DataStruct.ClickStruct()
ScrollOperate = DataStruct.ScrollStruct()
PressOperate = DataStruct.PressStruct()
ReleaseOperate = DataStruct.ReleaseStruct()

keyboard_map = {
    # -------- Ctrl + 字母 --------
    "\\x01" : 'a',      # Ctrl + a
    "\\x02" : 'b',      # Ctrl + b
    "\\x03" : 'c',      # Ctrl + c
    "\\x04" : 'd',      # Ctrl + d
    "\\x05" : 'e',      # Ctrl + e
    "\\x06" : 'f',      # Ctrl + f
    "\\x07" : 'g',      # Ctrl + g
    "\\x08" : 'h',      # Ctrl + h
    "\\t"   : 'i',      # Ctrl + i
    "\\n"   : 'j',      # Ctrl + j
    "\\x0b" : 'k',      # Ctrl + k
    "\\x0c" : 'l',      # Ctrl + l
    "\\r"   : 'm',      # Ctrl + m
    "\\x0e" : 'n',      # Ctrl + n
    "\\x0f" : 'o',      # Ctrl + o
    "\\x10" : 'p',      # Ctrl + p
    "\\x11" : 'q',      # Ctrl + q
    "\\x12" : 'r',      # Ctrl + r
    "\\x13" : 's',      # Ctrl + s
    "\\x14" : 't',      # Ctrl + t
    "\\x15" : 'u',      # Ctrl + u
    "\\x16" : 'v',      # Ctrl + v
    "\\x17" : 'w',      # Ctrl + w
    "\\x18" : 'x',      # Ctrl + x
    "\\x19" : 'y',      # Ctrl + y
    "\\x1a" : 'z',      # Ctrl + z
    # ------ Ctrl + 特殊字符 -------
    "<186>" : ';',      # Ctrl + ;
    "<187>" : '=',      # Ctrl + =
    "<189>" : '-',      # Ctrl + -
    "<192>" : '`',      # Ctrl + `
    "<222>" : '\'',     # Ctrl + \
    "<48>"  : '0',      # Ctrl + 0
    "<49>"  : '1',      # Ctrl + 1
    "<50>"  : '2',      # Ctrl + 2
    "<51>"  : '3',      # Ctrl + 3
    "<52>"  : '4',      # Ctrl + 4
    "<53>"  : '5',      # Ctrl + 5
    "<54>"  : '6',      # Ctrl + 6
    "<55>"  : '7',      # Ctrl + 7
    "<56>"  : '8',      # Ctrl + 8
    "<57>"  : '9',      # Ctrl + 9
    # ------ Shift + 特殊字符 -------
    "~"     : '`',      # shift + `
    "!"     : '1',      # shift + 1
    "@"     : '2',      # shift + 2
    "#"     : '3',      # shift + 3
    "$"     : '4',      # shift + 4
    "%"     : '5',      # shift + 5
    "^"     : '6',      # shift + 6
    "*"     : '7',      # shift + 7
    "("     : '8',      # shift + 8
    ")"     : '9',      # shift + 9
    "_"     : '-',      # shift + -
    "+"     : '=',      # shift + =
    ":"     : ';',      # shift + ;
    "\""    : '\'',     # shift + '
    "<"     : ',',      # shift + ,
    "{"     : '[',      # shift + [
    "}"     : ']',      # shift + ]
    "|"     : '\\',     # shift + \
    "?"     : '/',      # shift + /
}
