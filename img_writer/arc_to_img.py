# -*- coding: utf-8 -*-
"""弧エンティティの画像を作成するモジュール.
Created on Tue Nov 26 14:25:06 2024

@author: AB21074
"""

import numpy as np
import math
from PIL import ImageDraw

from img_writer.param_to_img import Param2Img

class Arc2Img(Param2Img):
    """指定したサイズの画像へ直線を描画するクラス."""

    def __init__(self, drawing_size: tuple[int] = (400, 400),
                 img_size: tuple[int] = (400, 400),
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
        center = param[8:10]
        radius = param[10]
        
        
        start_corner = [center[0] - radius, center[1] + radius]
        end_corner = [center[0] + radius, center[1] - radius]
        
        
        start_angle = param[11]
        end_angle = param[12]


        xy = self.convert_cood(start_corner), self.convert_cood(end_corner)
        draw.arc(xy, start_angle, end_angle, fill = (0,0,0))