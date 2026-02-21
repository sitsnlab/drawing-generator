# -*- coding: utf-8 -*-
"""line_generator.LineGeneratorのテスト.
Line2Imgのテストも兼ねる.

Created on Wed May 15 20:17:56 2024.
@author: Yuta Kuronuma
"""

from pathlib import Path as plib
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from img_writer.line_to_img import Line2Img
from csv_io import CsvIO
from generator.line_generator import LineGenerator

if __name__ == '__main__':
    data_name = 'line_224x224_test'  # データセット名指定

    # path,directry作成
    directry = plib(r'') / data_name
    directry.mkdir(parents=True, exist_ok=True)
    csvpath = directry / (data_name + '.csv')

    ent_num = 1000  # データ数
    size = (224, 224)  # 画像サイズ
    drawing_size = (400, 400) # 図面サイズ：(400, 280)

    # パラメータ作成
    lg = LineGenerator(drawing_size=drawing_size)
    lines = lg.gen_ent(ent_num)

    CsvIO.write_csv(lines, csvpath)  # CSV保存
    params = CsvIO.read_csv(csvpath)  # 読み込み

    print(params.shape)

    # 画像作成
    l2i = Line2Img(img_size=size, drawing_size=drawing_size)
    l2i.draw_imgs(params, directry)
