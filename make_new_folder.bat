@echo off

rem デスクトップに「Blender_files」フォルダが存在しない場合は作成する
if not exist "%USERPROFILE%\Desktop\Blender_files" (
  mkdir "%USERPROFILE%\Desktop\Blender_files"
)

rem 「Blender_files」フォルダを親フォルダとして、その中に「meshes」「images」「studio」「studio_and_meshes」のフォルダを作成する
rem meshesフォルダが存在しない場合は作成する
if not exist "%USERPROFILE%\Desktop\Blender_files\meshes" (
  mkdir "%USERPROFILE%\Desktop\Blender_files\meshes"
)
rem imagesフォルダが存在しない場合は作成する
if not exist "%USERPROFILE%\Desktop\Blender_files\images" (
  mkdir "%USERPROFILE%\Desktop\Blender_files\images"
)
rem studioフォルダが存在しない場合は作成する
if not exist "%USERPROFILE%\Desktop\Blender_files\studio" (
  mkdir "%USERPROFILE%\Desktop\Blender_files\studio"
)
rem studio_and_meshesフォルダが存在しない場合は作成する
if not exist "%USERPROFILE%\Desktop\Blender_files\studio_and_meshes" (
  mkdir "%USERPROFILE%\Desktop\Blender_files\studio_and_meshes"
)

rem 処理が完了したことを表示する
echo 処理が完了しました。
