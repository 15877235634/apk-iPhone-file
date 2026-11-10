[app]
title = xiangqi
package.name = xiangqi
package.domain = com.apkpackager
source.dir = .
source.include_exts = py,png,jpg,jpeg,gif,kv,atlas,ttf,txt,json,csv,db,mp3,wav
version = 1.0
requirements = kivy,python3,subprocess,ctypes
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
