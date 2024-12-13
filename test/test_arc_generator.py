# -*- coding: utf-8 -*-
"""arc_generator.ArcGeneratorのテスト.
Circle2Imgのテストも兼ねる.
Created on Wed Nov 27 08:52:08 2024

@author: AB21074
"""


from pathlib import Path as plib

from img_writer.arc_to_img import Arc2Img
from csv_io import CsvIO
from generator.arc_generator import ArcGenerator

if __name__ == '__main__':
    data_name = 'test_arc_data'  # データセット名指定

    # path,directry作成
    directry = plib(r'D:\pic_dataset') / data_name
    directry.mkdir(parents=True, exist_ok=True)
    csvpath = directry / (data_name + '.csv')

    ent_num = 100  # データ数
    size = (100, 100)  # 画像サイズ
    # 図面サイズ：(400, 280)

    # パラメータ作成
    ag = ArcGenerator()
    arcs = ag.gen_ent(ent_num)


    CsvIO.write_csv(arcs, csvpath)  # CSV保存
    params = CsvIO.read_csv(csvpath)  # 読み込み

    print(params.shape)

    # 画像作成
    a2i = Arc2Img(img_size=size)
    a2i.draw_imgs(params, directry)