# 指定ディレクトリ内のファイルを連番ファイル名に変更するコード
#-----------------------------------------------------------
# 第１引数：ディレクトリの絶対パス
# 第２引数：対象ファイルの拡張子(.除く)
# 第３引数：接頭語 
# 「第３引数で指定した接頭語+通し番号.拡張子」というファイル名に変換する
# 

import sys
import cv2
import glob
import shutil
import os

def renban_de_rename(dir_path, ext, initial):
    pick = dir_path + ext

    # ファイルリストの読み込み
    file_names = glob.glob(pick)
    file_names.sort()

    # 'ディレクトリ内のファイル数だけループ
    num = 0
    for file_path in file_names:
        if len(initial) > 0:
            new_name = initial
            new_name += '{:0=6}'.format(num)
        else:
            new_name = '{:0=6}'.format(num)
        
        new_name += '.'
        new_name += args[2]
        new_path = dir_path + new_name    
        os.rename(file_path, new_path)

        msg = 'Renamed: ' + os.path.basename(file_path)
        msg += '-> ' + os.path.basename(new_path)
        print(msg)
        
        num += 1

if __name__ == '__main__':
    # コマンドラインから引数を取得する
    args = sys.argv

    dir_path = args[1]
    dir_path += "/"
    ext = "*." + args[2]
    initial = args[3]

    renban_de_rename(dir_path, ext, initial)
