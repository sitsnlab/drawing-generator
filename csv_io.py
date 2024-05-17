# -*- coding: utf-8 -*-
"""保存したCSVファイルを読み込むモジュール.

Created on Wed May 15 11:26:51 2024.
@author: Yuta Kuronuma
"""

import numpy as np


class CsvIO:
    """CSVに保存したパラメータを読み込み、arrayにするクラス."""

    @classmethod
    def read_csv(cls, filepath: str = 'param_test.csv'):
        """CSVを読み込む."""
        param = np.loadtxt(filepath, delimiter=',')
        return param

    @classmethod
    def write_csv(cls, param: np.ndarray, filepath: str = 'param_test.csv'):
        """CSVを書き出す."""
        np.savetxt(filepath, param, delimiter=',')
