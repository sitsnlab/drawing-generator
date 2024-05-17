# -*- coding: utf-8 -*-
"""line_generator.LineGeneratorのテスト.
Line2Imgのテストも兼ねる.

Created on Wed May 15 20:17:56 2024.
@author: Yuta Kuronuma
"""

from pathlib import Path as plib

from img_writer.line_to_img import Line2Img
from csv_io import CsvIO
from generator.line_generator import LineGenerator

if __name__ == '__main__':
    data_name = 'test_line_data'  # データセット名指定

    # path,directry作成
    directry = plib(r'D:\pic_dataset') / data_name
    directry.mkdir(parents=True, exist_ok=True)
    csvpath = directry / (data_name + '.csv')

    ent_num = 100  # データ数
    size = (100, 70)  # 画像サイズ
    # 図面サイズ：(400, 280)

    # パラメータ作成
    lg = LineGenerator()
    lines = lg.gen_ent(ent_num)

    CsvIO.write_csv(lines, csvpath)  # CSV保存
    params = CsvIO.read_csv(csvpath)  # 読み込み

    print(params.shape)

    # 画像作成
    l2i = Line2Img(img_size=size)
    l2i.draw_imgs(params, directry)
