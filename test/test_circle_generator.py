

"""circle_generator.CircleGeneratorのテスト.
Circle2Imgのテストも兼ねる.
Created on Wed May 22 12:16:58 2024


@author: AB21074
"""

from pathlib import Path as plib

from img_writer.circle_to_img import Circle2Img
from csv_io import CsvIO
from generator.circle_generator import CircleGenerater

if __name__ == '__main__':
    data_name = 'test_circle_data'  # データセット名指定

    # path,directry作成
    directry = plib(r'D:\pic_dataset') / data_name
    directry.mkdir(parents=True, exist_ok=True)
    csvpath = directry / (data_name + '.csv')

    ent_num = 100  # データ数
    size = (100, 70)  # 画像サイズ
    # 図面サイズ：(400, 280)

    # パラメータ作成
    cg = CircleGenerater()
    circles = cg.gen_ent(ent_num)


    CsvIO.write_csv(circles, csvpath)  # CSV保存
    params = CsvIO.read_csv(csvpath)  # 読み込み

    print(params.shape)

    # 画像作成
    c2i = Circle2Img(img_size=size)
    c2i.draw_imgs(params, directry)

    # 画像作成
    c2i = Circle2Img(img_size=size)
    c2i.draw_imgs(params, directry)
