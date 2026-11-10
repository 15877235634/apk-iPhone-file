# -*- coding: utf-8 -*-
# tkinter 兼容垫片子模块（由 APK 软件打包器 生成）
from tkinter import _show_dialog


def askstring(title="输入", prompt="", initialvalue="", **k):
    return _show_dialog("askstring", title, prompt, with_input=True,
                        input_default=initialvalue)


def askinteger(title="输入", prompt="", initialvalue=None, **k):
    v = _show_dialog("askstring", title, prompt, with_input=True,
                     input_default="" if initialvalue is None else str(initialvalue))
    if v is None or v == "":
        return None
    try:
        return int(v)
    except ValueError:
        return None


def askfloat(title="输入", prompt="", initialvalue=None, **k):
    v = _show_dialog("askstring", title, prompt, with_input=True,
                     input_default="" if initialvalue is None else str(initialvalue))
    if v is None or v == "":
        return None
    try:
        return float(v)
    except ValueError:
        return None
