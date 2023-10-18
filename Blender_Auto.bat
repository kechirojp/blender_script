@echo off

rem Blenderを起動し、studio.blendファイルを読み込みます。
rem Blenderでpythonスクリプトを実行する
rem Blenderのバージョンは3.6です。
blender "%USERPROFILE%\Desktop\Blender_files\studio\studio.blend" --background --python "C:\Program Files\Blender Foundation\Blender 3.6\3.6\scripts\sample.py"


