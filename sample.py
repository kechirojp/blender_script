import bpy
import numpy as np
import os


##############################################################################################################
###  前処理  #################################################################################################
##############################################################################################################
"""
環境変数の取得
Mac/LinuxではHOME
WindowsではHOMEPATHやUSERPROFILEに格納
"""

home_directory = (
                  os.environ.get('HOME') or
                  os.environ.get('HOMEPATH') or
                  os.environ.get('USERPROFILE')
                )

##############################################################################################################




##############################################################################################################
###  前処理  #################################################################################################
##############################################################################################################
"""
作業用フォルダの作成
理由：スクリプトエラー時にファイルが破損する可能性があるため
例 : マテリアルとメッシュの関連付けができなくなる

方針：
フォトグラメトリファイルは巨大なため
一つファイルを処理終了するごとにファイルを削除する
"""
import shutil

# 作業用フォルダのパス
temp_folder_path = f"{home_directory}/Desktop/Blender_files/meshes/temp_folder"

# フォルダが存在するかどうかを確認
if not os.path.exists(temp_folder_path):
  # フォルダを作成する
  os.makedirs(temp_folder_path)
  
##############################################################################################################




##############################################################################################################
###  前処理  #################################################################################################
##############################################################################################################
"""
Blenderファイルリスリストを取得
1: 被写体ファイルのファイルのフルパスをリストを取得する関数を定義
2: 被写体ファイルのファイル名（拡張子無し）を取得する関数を定義
"""
# 関数 get_blender_files_full_pathを定義
def get_blender_files_full_path(path):
  """
  指定したパスにある.blender拡張子を持つファイルのフルパスのリストを返す。

  Args:
    path: 対象フォルダのフルパス

  Returns:
    .blender拡張子を持つファイルのフルパスのリスト
  """
  # ファイル・ディレクトリの一覧を取得
  files = os.listdir(path)
  
  blender_files = []
  for file in files:
    # もし拡張子が.blendなら
    if file.endswith(".blend"):
      # フルパスを取得してリストに追加 ディレクトリ名とファイル名を結合
      blender_files.append(os.path.abspath(os.path.join(path, file)))
      
  return blender_files





# ファイル名（拡張子無し）のみ取得する関数の定義
def get_file_name_without_extension(full_path):
  """
  指定したフルパスから、blenderファイルの拡張子のないファイル名だけを取り出す。

  Args:
    full_path: 対象のフルパス

  Returns:
    ファイル名
  """

  file_name = os.path.basename(full_path)
  file_name = os.path.splitext(file_name)[0] #[0]がファイル名、[1]が拡張子
  return file_name

##############################################################################################################




##############################################################################################################
###  前処理  #################################################################################################
##############################################################################################################
"""
年月日時分を取得
ファイル名に使用
※今後 フォルダ名にも使用するかも
"""
import datetime

# 現在時刻
now = datetime.datetime.now()

# 年
year = now.year

# 月
month = now.month

# 日
day = now.day

# 時間
hour = now.hour

# 分
minute = now.minute

##############################################################################################################




##############################################################################################################
###  前処理  #################################################################################################
##############################################################################################################
"""
rendering設定
"""
# 解像度
resolution_x = 1920
resolution_y = 1080

# 画像の画質 => 画質 max:100 min:0
image_resolution_percentage = 100

# 動画の画質 => 画質 max:100 min:0
movie_resolution_percentage = 10

# フレームレート
fps = 30

# アニメーションの開始フレームと終了フレーム
start_frame = 0
end_frame = 30

##############################################################################################################




##############################################################################################################
###  本番処理  ###############################################################################################
##############################################################################################################
"""
以下の処理

1: meshesディレクトリの被写体ファイル(.blenderファイル)のフルパスリストを取得

2: 被写体ファイルのファイル名（拡張子無し）を取得

3: 4~8の処理を繰り返す

4: フルパスリストの被写体ファイルをtemp_folderにコピー

5: temp_folderにコピーされている
   .blenderファイルの被写体（mesh）をスタジオセットのシーンに配置
   
6: 被写体（mesh）にターンテーブルキーフレームアニメーションの追加

7: 静止画レンダリング・動画レンダリング

8: temp_folderにコピーされている被写体ファイルを削除

"""

# 被写体オブジェクトが入ったディレクトリのすべての.blenderファイルのフルパスリストを取得
blender_files_list = get_blender_files_full_path(f"{home_directory}/Desktop/Blender_files/meshes")

for file_path in blender_files_list:  
    
    # ファイル名（拡張子無し）を取得 => 保存時のファイル名に使用
    file_name = get_file_name_without_extension(file_path)
    
    
    """
    元データ破損を防ぐために
    作業用フォルダに.blenderファイルをコピー
    """
    # 作業用フォルダのパス
    # temp_folder_path = f"{home_directory}/Desktop/Blender_files/meshes/temp_folder"
    shutil.copy(file_path, temp_folder_path)
    
    # 作業用フォルダにコピーされた.blenderファイルのフルパス  
    file_path = os.path.join(temp_folder_path, os.path.basename(file_path))
    
    
    
    
    """
    オブジェクトの追加
    ・blendファイルからオブジェクトを追加する => append
    ※ .blend以外 => import
    """
    # file_path：フルパスでBlendファイルを指定する
    file_path

    # inner_path：タイプ、ここではオブジェクトobjectを指定した。マテリアルの場合はmaterial等になる。
    inner_path = 'Object'

    # object_name：オブジェクトの名称  
    object_name = 'mesh'

    # ファイルを開き、オブジェクトを指定　追加
    bpy.ops.wm.append(
                        filepath=os.path.join(file_path, inner_path, object_name),
                        directory=os.path.join(file_path, inner_path),
                        filename=object_name
                      )



    
    """
    忘れがちだけど重要な処理
    ・オブジェクトの選択
    """
    # オブジェクトの取得
    obj = bpy.data.objects["mesh"]

    # オブジェクトの選択
    obj.select_set(True)
    



    """
    静止画レンダリング
    """
    """
    忘れがちだけど重要な処理
    ・レンダリングサイズを指定 => 動画撮影時の設定が残っているので必ず指定しておく
    """
    # レンダリングサイズを指定
    bpy.context.scene.render.resolution_x = resolution_x
    bpy.context.scene.render.resolution_y = resolution_y

    # 画質を落とす max:100 min:0
    bpy.context.scene.render.resolution_percentage = image_resolution_percentage
    
    # 現在のビューでレンダリング
    bpy.ops.render.render(use_viewport=True)

    #　レンダリング結果を保存 => ファイル名は上で取得したファイル名
    bpy.data.images['Render Result'].save_render( filepath = f"{home_directory}/Desktop/Blender_files/images/{file_name}_{year}_{month}{day}_{hour}{minute}.png")




    """
    忘れがちだけど重要な処理
    ・オブジェクトの選択
    """
    # オブジェクトの取得
    obj = bpy.data.objects["mesh"]

    # オブジェクトの選択
    obj.select_set(True)
    
    
    
    
    """
    アニメーションをつける
    ※オイラー角で指定
    ※うまくいかない場合は、ファイルを開いて回転モードをオイラー角に変更する
    """
    # レンダリングする対象のオブジェクトを選択
    mesh = bpy.data.objects['mesh']

    # フレームの開始位置を指定
    mesh.keyframe_insert(data_path="rotation_euler", frame=start_frame)
    
    # z軸方向に360°回転させる
    # オイラー角で指定!!!!
    mesh.rotation_euler.z += np.radians(-360)
    
    # フレームの終了位置を指定
    mesh.keyframe_insert(data_path="rotation_euler", frame=end_frame)




    """
    動画レンダリング
    """
    # レンダリングサイズを指定
    bpy.context.scene.render.resolution_x = resolution_x
    bpy.context.scene.render.resolution_y = resolution_y

    # 画質を落とす max:100 min:0
    bpy.context.scene.render.resolution_percentage = movie_resolution_percentage

    # ファイル形式を指定
    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'

    # レンダリングするフレームの開始位置と終了位置を指定
    bpy.context.scene.frame_start = start_frame
    bpy.context.scene.frame_end = end_frame

    # フレームレートを指定
    bpy.context.scene.render.fps = fps

    # レンダリングムービーの保存先 => ファイル名は上で取得したファイル名
    bpy.data.scenes["Scene"].render.filepath = f"{home_directory}/Desktop/Blender_files/movies/{file_name}_{year}_{month}{day}_{hour}{minute}.mp4"
    bpy.ops.render.render(animation=True)




    """
    忘れがちだけど 重要な処理
    ・オブジェクトの選択
    """
    # オブジェクトの取得
    obj = bpy.data.objects["mesh"]

    # オブジェクトの選択
    obj.select_set(True)
    
    # オブジェクトの削除
    bpy.ops.object.delete()
    
    
    
    
    """
    作業フォルダ内の一時ファイルを削除
    フォトグラメトリファイルは巨大なため都度削除
    """
    os.remove(file_path)
    
##############################################################################################################

# .blendファイルリスト分の処理が終わったら終了
