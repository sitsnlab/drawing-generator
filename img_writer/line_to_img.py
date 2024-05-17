# -*- coding: utf-8 -*-
"""Lineエンティティの画像を作成するモジュール.

Created on Fri May 17 01:26:52 2024.
@author: Yuta Kuronuma
"""

import numpy as np
from PIL import ImageDraw

from img_writer.param_to_img import Param2Img


class Line2Img(Param2Img):
    """指定したサイズの画像へ直線を描画するクラス."""

    def __init__(self, drawing_size: tuple[int] = (400, 280),
                 img_size: tuple[int] = (400, 280),
                 background: tuple[int] = (255, 255, 255)):
        """イニシャライザ.

        Parameters
        ----------
        drawing_size : tuple[int], optional
            図面サイズ. The default is (400, 280).
        img_size : tuple[int], optional
            出力する画像サイズ. The default is (400, 280).
        background : tuple[int], optional
            背景色. The default is (255, 255, 255).

        Returns
        -------
        None.

        """
        super().__init__(drawing_size, img_size, background)

    def draw_ent(self, param: np.ndarray, target: ImageDraw = None,
                 color=(0, 0, 0), lineweight=0):
        """画像に図形を描画する.

        Parameters
        ----------
        param : np.ndarray
            図形情報.
        draw : ImageDraw | None, optional
            図形情報を書き込む対象. The default is None.
        color : TYPE, optional
            線の色. The default is (0, 0, 0)黒.
        lineweight : TYPE, optional
            線太さ. The default is 1.

        Returns
        -------
        None.

        """
        draw = self.draw if target is None else target
        start = param[1:3]
        end = param[3:5]

        xy = self.convert_cood(start), self.convert_cood(end)
        draw.line(xy, fill=color, width=lineweight)
