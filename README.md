# Blender自動処理サンプル概要
meshesフォルダ（被写体ファイルを入れるフォルダ）に入ったいるすべてのファイルに
以下の一連処理

 1. スタジオセットに被写体をインポート
 2.  被写体にターンテーブルアニメーションをつける 
 3. 静止画・動画の撮影

## 使い方（ windows）
### git clone を使わない場合を想定 ※非エンジニア用
#### ※デスクトップで作業した場合

 ### 1. make_new_folder.batをダブルクリック 
 デスクトップに以下の構成でフォルダが作成される。

```
    Blender_files
    ├─images
    ├─meshes
    ├─movies
    ├─studio
    └─studio_and_meshes
```

 ### 2. 撮影セットであるstudio.blendをstudioフォルダに配置。
 ### 3. sample.pyをBlender本体がインストールされているフォルダ内にあるscriptsフォルダ内においてください。
     
    例
    ```
    C:/Program Files/Blender Foundation/Blender 3.6/3.6/scripts
    ```
**※Blenderのバージョンは各自の環境に合わせてください。**

    
    
 ### 4. template.blend : 被写体用テンプレートファイル 
 - デフォルトで入っているmeshの位置・大きさに合わせて 被写体を配置 。
  - 被写体の名前は必ず**mesh**に書き換えてください。
  - デフォルトのmeshは削除。 
  - ファイル名は任意のものにしていただいて構いません。
  - 被写体ファイルをmeshesフォルダに配置。
    **※複数ファイル可**

### 5. Blender_Auto.batの**sample.pyのパスは各自の環境に書き換えてください。**
 以下はBlender3.6の場合
```
blender "%USERPROFILE%\Desktop\Blender_files\studio\studio.blend" --background --python "C:\Program Files\Blender Foundation\Blender 3.6\3.6\scripts\sample.py"
```

  ※.batファイルの書き換えの方法
  - ファイル名 Blender_Auto.batの.batを.txtに書き換え
  - Blender_Auto.txtをメモ帳などのテキストエディタで開く
  - Blenderバージョンなどの当該部分を書き換え 
  - 保存
   - Blender_Auto.txtのファイル名をBlender_Auto.batに書き換え

### 6. Blender_Auto.batを起動
meshesフォルダ内の被写体を自動で撮影用ファイルに追加 ===>アニメーション追加 ===> レンダリング（静止画・動画生成）
生成された静止画はimagesフォルダ 　動画はmoviesフォルダに保存されます。






## フォルダ・ファイル構成例
```
Blender_files
├─images（レンダリング画像保存先）
│
├─meshes（被写体ファイルを入れるフォルダ）
│  │例
│  │  Horse_Statue_only.blend(フォトグラメトリファイル)
│  │  safety_cone_only.blend
│  │  Squirrel_statue_only.blend(フォトグラメトリファイル)
│  │
│  └─temp_folder（作業用テンポラリフォルダ）
│
├─movies（レンダリング動画保存先）
│
├─studio
│      studio.blend(撮影用スタジオセット)
└─studio_and_meshes
```

## ファイル
- make_new_folder.bat : 自動処理に必要なフォルダを生成
- Blender_Auto.bat : Blenderをバックグラウンドで立ち上げ　pythonスクリプトを走らせるバッチファイル
 - studio.blend                      : 撮影用のカメラ・ライト・背景の入ったファイル
 - template.blend : 被写体用テンプレートファイル
 デフォルトで入っているmeshの位置・大きさに合わせて 被写体を配置
 被写体の名前は必ず**mesh**に書き換えてください。
- sample.py : 被写体配置　アニメーション追加　静止画・動画レンダリングの自動処理を行うpythonスクリプト
Blender本体がインストールされているフォルダ内にあるscriptsフォルダ内においてください。

