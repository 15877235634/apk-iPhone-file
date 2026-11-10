# -*- coding: utf-8 -*-
# tkinter 兼容垫片（由 APK 软件打包器 自动生成，只存在于打包项目里，不影响原 .py 文件）
# 手机上没有真正的 tkinter：本包把 tkinter 调用降级，让脚本核心逻辑继续运行。
# SHIM_MODE = "print" ：弹窗内容变成文字输出（最稳妥，无需操作）
# SHIM_MODE = "kivy"  ：弹窗变成真正的手机弹窗（可点按钮、可输入）
SHIM_MODE = "print"

import os


def _cjk_font():
    for _c in ("NotoSansCJK-Regular.ttf", "NotoSansSC-Regular.ttf",
               "msyh.ttf", "simhei.ttf"):
        if os.path.exists(_c):
            return _c
    return None


class _Stub(object):
    """通用空操作对象：窗口/控件等 tkinter 对象全部变成无操作"""
    _NONE_RETURN = frozenset((
        "pack", "pack_forget", "grid", "grid_remove", "place", "config",
        "configure", "mainloop", "update", "update_idletasks", "destroy", "quit",
        "title", "geometry", "protocol", "withdraw", "iconify", "deiconify",
        "resizable", "minsize", "maxsize", "focus_set", "focus_force", "bind",
        "unbind", "insert", "delete", "see", "mark_set", "tag_bind", "yview",
        "xview", "yview_moveto", "xview_moveto", "set", "selection_set",
        "selection_clear", "column", "row", "columnconfigure", "rowconfigure",
        "state", "lift", "lower", "tkraise", "clipboard_clear",
        "clipboard_append", "bell", "attributes", "overrideredirect",
        "transient", "grab_set", "grab_release", "create_text", "create_line",
        "create_rectangle", "create_oval", "create_image", "add_command",
        "add_separator", "add_cascade", "entryconfig", "invoke", "setvar"))

    def __init__(self, *a, **k):
        pass

    def __getattr__(self, name):
        if name.startswith("_"):
            raise AttributeError(name)
        if name in ("get", "getvalue", "getvar", "actual", "cget"):
            return lambda *a, **k: ""
        if name in ("curselection", "size", "find", "find_withtag", "index",
                    "count"):
            return lambda *a, **k: 0
        if name in ("measure", "winfo_width", "winfo_height", "winfo_reqwidth",
                    "winfo_reqheight", "winfo_x", "winfo_y", "winfo_screenwidth",
                    "winfo_screenheight"):
            return lambda *a, **k: 0
        if name == "mainloop":
            def _mainloop(*a, **k):
                print("\n（tkinter 兼容模式：图形窗口和按钮在手机上无法显示/点击，"
                      "已跳过 mainloop。如果程序没有任何输出，说明主要逻辑写在"
                      "按钮回调里——兼容模式无法触发按钮，需要改写成命令式流程，"
                      "可以把脚本发给 AI 帮忙改一版。）")
                return None
            return _mainloop
        if name == "after":
            # 手机上没有事件循环：立即执行回调，保证定时任务里的逻辑照常运行
            def _after(ms, fn=None, *a, **k):
                if fn is not None:
                    try:
                        fn(*a)
                    except Exception:
                        pass
                return None
            return _after
        if name in self._NONE_RETURN:
            return lambda *a, **k: None
        def _stub_method(*a, **k):
            return _Stub()
        return _stub_method

    def __setattr__(self, *a, **k):
        pass

    def __setitem__(self, *a, **k):
        pass

    def __getitem__(self, k):
        return ""

    def __iter__(self):
        return iter(())

    def __bool__(self):
        return True

    def __str__(self):
        return "<tkinter控件(手机上已禁用)>"


class _BaseVar(object):
    def __init__(self, master=None, value=None, name=None):
        self._v = value

    def get(self):
        return self._v

    def set(self, v):
        self._v = v

    def trace(self, *a, **k):
        return None

    def trace_add(self, *a, **k):
        return None


class StringVar(_BaseVar):
    def __init__(self, master=None, value="", name=None):
        _BaseVar.__init__(self, master, "" if value is None else value, name)


class IntVar(_BaseVar):
    def __init__(self, master=None, value=0, name=None):
        _BaseVar.__init__(self, master, 0 if value is None else value, name)


class DoubleVar(_BaseVar):
    def __init__(self, master=None, value=0.0, name=None):
        _BaseVar.__init__(self, master, 0.0 if value is None else value, name)


class BooleanVar(_BaseVar):
    def __init__(self, master=None, value=False, name=None):
        _BaseVar.__init__(self, master, False if value is None else value, name)


class Tk(_Stub): pass
class Toplevel(_Stub): pass
class Frame(_Stub): pass
class Label(_Stub): pass
class Button(_Stub): pass
class Entry(_Stub): pass
class Text(_Stub): pass
class Canvas(_Stub): pass
class Listbox(_Stub): pass
class Scrollbar(_Stub): pass
class Menu(_Stub): pass
class Menubutton(_Stub): pass
class Checkbutton(_Stub): pass
class Radiobutton(_Stub): pass
class Scale(_Stub): pass
class Spinbox(_Stub): pass
class LabelFrame(_Stub): pass
class Message(_Stub): pass
class PanedWindow(_Stub): pass
class OptionMenu(_Stub): pass
class PhotoImage(_Stub): pass
class BitmapImage(_Stub): pass
class Tcl(_Stub): pass


# ---- 常量 ----
TRUE, FALSE = 1, 0
YES, NO, OK, CANCEL = "yes", "no", "ok", "cancel"
TOP, BOTTOM, LEFT, RIGHT = "top", "bottom", "left", "right"
BOTH, NONE, X, Y = "both", "none", "x", "y"
N, S, E, W = "n", "s", "e", "w"
NS, EW, NSEW = "ns", "ew", "nsew"
NW, NE, SW, SE = "nw", "ne", "sw", "se"
HORIZONTAL, VERTICAL = "horizontal", "vertical"
END, NORMAL, DISABLED, ACTIVE = "end", "normal", "disabled", "active"
CENTER, BASELINE = "center", "baseline"
SEL_FIRST, SEL_LAST = "sel.first", "sel.last"
CURRENT, ANCHOR = "current", "anchor"
WORD, CHAR = "word", "char"
SUNKEN, RAISED, FLAT = "sunken", "raised", "flat"
GROOVE, RIDGE = "groove", "ridge"
SINGLE, BROWSE, MULTIPLE, EXTENDED = "single", "browse", "multiple", "extended"
TkVersion = 8.6


# ---- 对话框实现 ----
def _print_dialog(kind, title, message, with_input=False, input_default=""):
    tag = {"showinfo": "提示", "showwarning": "警告", "showerror": "错误"}.get(
        kind, "弹窗")
    print("\n【%s·%s】%s" % (tag, title, message))
    if with_input:
        print("（兼容模式无法手动输入，自动填入默认值：%s）" % (input_default or "<空>"))
        return input_default or ""
    if kind.startswith("ask"):
        print("（兼容模式自动选择了默认答案：是/确定）")
        return True
    return True


def _kivy_popup(kind, title, message, with_input=False, input_default=""):
    """在手机界面上弹出真正的对话框；kivy 不可用时退回文字输出"""
    try:
        import queue as _q
        import threading as _threading
        from kivy.clock import Clock
    except Exception:
        return _print_dialog(kind, title, message, with_input, input_default)
    _result = {}
    _done = _threading.Event()

    def _close(_popup, value):
        _result["v"] = value
        try:
            _popup.dismiss()
        except Exception:
            _done.set()

    def _open(_dt):
        popup = None
        try:
            from kivy.uix.popup import Popup
            from kivy.uix.boxlayout import BoxLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            from kivy.uix.textinput import TextInput
            fname = _cjk_font() or "Roboto"
            content = BoxLayout(orientation="vertical", padding=12, spacing=10)
            lbl = Label(text=str(message), halign="left", valign="middle",
                        color=(0.06, 0.22, 0.09, 1), font_name=fname,
                        font_size="15sp")
            lbl.bind(width=lambda i, w: setattr(i, "text_size", (w, None)))
            content.add_widget(lbl)
            ti = None
            if with_input:
                ti = TextInput(text="" if input_default is None else str(input_default),
                               multiline=False, size_hint_y=None, height=42,
                               font_size="14sp", font_name=fname,
                               background_color=(1, 1, 1, 1),
                               foreground_color=(0.1, 0.3, 0.15, 1), focus=True)
                content.add_widget(ti)
            btn_row = BoxLayout(size_hint_y=None, height=46, spacing=8)
            green = (0.26, 0.63, 0.28, 1)
            gray = (0.55, 0.55, 0.55, 1)
            red = (0.72, 0.25, 0.2, 1)
            if with_input:
                b_ok = Button(text="确定", size_hint=(1, 1), bold=True,
                              background_normal="", background_color=green,
                              color=(1, 1, 1, 1), font_name=fname)
                b_ok.bind(on_press=lambda *_: _close(popup, ti.text if ti else ""))
                b_cancel = Button(text="取消", size_hint=(1, 1),
                                  background_normal="", background_color=gray,
                                  color=(1, 1, 1, 1), font_name=fname)
                b_cancel.bind(on_press=lambda *_: _close(popup, None))
                btn_row.add_widget(b_ok)
                btn_row.add_widget(b_cancel)
            elif kind in ("askyesno", "askyesnocancel"):
                b_yes = Button(text="是", size_hint=(1, 1), bold=True,
                               background_normal="", background_color=green,
                               color=(1, 1, 1, 1), font_name=fname)
                b_yes.bind(on_press=lambda *_: _close(popup, True))
                b_no = Button(text="否", size_hint=(1, 1),
                              background_normal="", background_color=red,
                              color=(1, 1, 1, 1), font_name=fname)
                b_no.bind(on_press=lambda *_: _close(popup, False))
                btn_row.add_widget(b_yes)
                btn_row.add_widget(b_no)
                if kind == "askyesnocancel":
                    b_c = Button(text="取消", size_hint=(1, 1),
                                 background_normal="", background_color=gray,
                                 color=(1, 1, 1, 1), font_name=fname)
                    b_c.bind(on_press=lambda *_: _close(popup, None))
                    btn_row.add_widget(b_c)
            else:
                b_ok = Button(text="确定", size_hint=(1, 1), bold=True,
                              background_normal="", background_color=green,
                              color=(1, 1, 1, 1), font_name=fname)
                b_ok.bind(on_press=lambda *_: _close(popup, True))
                btn_row.add_widget(b_ok)
            content.add_widget(btn_row)
            popup = Popup(title=str(title), content=content,
                          size_hint=(0.85, 0.45), auto_dismiss=False)
            popup.bind(on_dismiss=lambda *_: _done.set())
            popup.open()
        except Exception:
            _result["v"] = _print_dialog(kind, title, message, with_input,
                                         input_default)
            _done.set()

    Clock.schedule_once(_open, 0)
    _done.wait()
    return _result.get("v")


def _show_dialog(kind, title, message, with_input=False, input_default=""):
    if SHIM_MODE == "kivy":
        return _kivy_popup(kind, title, message, with_input, input_default)
    return _print_dialog(kind, title, message, with_input, input_default)


def showinfo(title="提示", message="", **k):
    return _show_dialog("showinfo", title, message)


def showwarning(title="警告", message="", **k):
    return _show_dialog("showwarning", title, message)


def showerror(title="错误", message="", **k):
    return _show_dialog("showerror", title, message)


def askyesno(title="询问", message="", **k):
    return _show_dialog("askyesno", title, message)


def askokcancel(title="确认", message="", **k):
    return _show_dialog("askokcancel", title, message)


def askretrycancel(title="重试", message="", **k):
    return _show_dialog("askretrycancel", title, message)


def askyesnocancel(title="询问", message="", **k):
    return _show_dialog("askyesnocancel", title, message)


# 子模块：预先导入，保证 tkinter.messagebox 这类用法直接可用
from tkinter import messagebox as messagebox  # noqa: E402
try:
    from tkinter import filedialog as filedialog  # noqa: E402,F401
    from tkinter import simpledialog as simpledialog  # noqa: E402,F401
    from tkinter import ttk as ttk  # noqa: E402,F401
    from tkinter import font as font  # noqa: E402,F401
    from tkinter import scrolledtext as scrolledtext  # noqa: E402,F401
    from tkinter import colorchooser as colorchooser  # noqa: E402,F401
    from tkinter import commondialog as commondialog  # noqa: E402,F401
    from tkinter import dialog as dialog  # noqa: E402,F401
except Exception:
    pass


def __getattr__(name):
    """兜底：脚本用到垫片没覆盖的 tkinter 子模块/名字时，
    返回空操作对象而不是报错（from tkinter import 任意名字 都不会崩）"""
    if name.startswith("_"):
        raise AttributeError(name)
    return _Stub()
