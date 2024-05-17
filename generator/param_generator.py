# -*- coding: utf-8 -*-
"""学習に利用するパラメータを生成するモジュール.

Created on Tue May 14 16:12:45 2024.
@author: Yuta Kuronuma
"""

import numpy as np


class ParamGenerator:
    """任意の座標を生成するクラス."""

    def __init__(self, drawing_size: tuple[int] = (400, 280)):
        """イニシャライザ."""
        self.drawing_size = drawing_size
        self.sizeX = drawing_size[0]
        self.sizeY = drawing_size[1]
        self.rng = np.random.default_rng()

    def gen_ent(self, size: int = 1):
        """0のみのパラメータを生成する."""
        return np.zeros([size, 13])

    def gen_cord(self, size: int = 1):
        """任意サイズのxy座標行列を作成する."""
        paramx = self.sizeX * self.rng.random((size, 1))
        paramy = self.sizeY * self.rng.random((size, 1))

        cords = np.hstack([paramx, paramy])
        return cords
