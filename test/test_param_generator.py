# -*- coding: utf-8 -*-
"""param_generator.ParamGeneratorのテスト.

Created on Wed May 15 13:34:59 2024.
@author: Yuta Kuronuma
"""

from csv_io import CsvIO
from generator.param_generator import ParamGenerator

if __name__ == '__main__':
    ent_num = 100  # データ数

    # パラメータ作成
    pg = ParamGenerator()
    zeros = pg.gen_ent(ent_num)

    CsvIO.write_csv(zeros, 'param_test.csv')  # CSV保存
    params = CsvIO.read_csv('param_test.csv')  # 読み込み

    print(params.shape)
