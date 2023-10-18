@echo off

rem デスクトップに「Blender_files」フォルダが存在しない場合は作成する
if not exist "%USERPROFILE%\Desktop\Blender_files" (
  mkdir "%USERPROFILE%\Desktop\Blender_files"
)

rem 「Blender_files」フォルダを親フォルダとして、その中に「meshes」「images」「studio」「studio_and_meshes」のフォルダを作成する
rem 「meshes」フォルダ
mkdir "%USERPROFILE%\Desktop\Blender_files\meshes"
rem 「images」フォルダ
mkdir "%USERPROFILE%\Desktop\Blender_files\images"
rem 「studio」フォルダ
mkdir "%USERPROFILE%\Desktop\Blender_files\studio"
rem 「studio_and_meshes」フォルダ
mkdir "%USERPROFILE%\Desktop\Blender_files\studio_and_meshes"

rem 処理が完了したことを表示する
echo 処理が完了しました。