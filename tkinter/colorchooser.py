# -*- coding: utf-8 -*-
# tkinter 兼容垫片子模块（由 APK 软件打包器 生成）：手机上不支持取色器
def askcolor(color=None, **k):
    print("\n【取色器】手机上暂不支持选取颜色，已返回默认颜色：白色")
    return ((255, 255, 255), "#ffffff")


class Chooser(object):
    def __init__(self, *a, **k):
        pass

    def show(self, *a, **k):
        return askcolor()
