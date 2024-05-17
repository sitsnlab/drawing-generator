# -*- coding: utf-8 -*-
"""LINEエンティティの座標生成をするモジュール.

Created on Wed May 15 18:56:40 2024.
@author: Yuta Kuronuma
"""

from generator.param_generator import ParamGenerator
import numpy as np


class LineGenerator(ParamGenerator):
    """直線エンティティを生成するクラス."""

    def __init__(self, drawing_size: tuple[int] = (400, 280)):
        """イニシャライザ."""
        super().__init__(drawing_size)

    def gen_ent(self, size: int = 1):
        """線の生成を行う."""
        line_type = np.zeros([size, 1])
        start = self.gen_cord(size)
        end = self.gen_cord(size)
        pad = np.zeros([size, 8])

        return np.hstack([line_type, start, end, pad])
