# -*- coding: utf-8 -*-
# tkinter 兼容垫片子模块（由 APK 软件打包器 生成）：手机上不支持文件选择对话框
def _no_dialog(*a, **k):
    print("\n【文件选择】手机上暂不支持选择文件/文件夹，已返回空值")
    return ""


def _no_dialogs(*a, **k):
    print("\n【文件选择】手机上暂不支持选择文件/文件夹，已返回空列表")
    return []


askopenfilename = _no_dialog
asksaveasfilename = _no_dialog
askdirectory = _no_dialog
askopenfile = _no_dialog
asksaveasfile = _no_dialog
askopenfilenames = _no_dialogs
askopenfiles = _no_dialogs
