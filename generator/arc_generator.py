# -*- coding: utf-8 -*-
"""arcエンティティの座標生成をするモジュール
Created on Thu May 23 15:47:55 2024

@author: AB21074
"""
from generator.param_generator import ParamGenerator
import numpy as np


class ArcGenerator(ParamGenerator):
    """直線エンティティを生成するクラス."""

    def __init__(self, drawing_size: tuple[int] = (400, 280)):
        """イニシャライザ."""
        super().__init__(drawing_size)

    def gen_ent(self, size: int = 1):
        """任意サイズの円の中心と半径を生成する."""
        
        #中心座標を生成
        centers = self.gen_cord(size)
        
        left = centers[0] #左端から中心の距離
        right = self.sizeX-centers[0] #右端から中心の距離
        down = centers[1] #下端から中心の距離
        up = centers[1] #上端から中心の距離
        
        pad = np.zeros([size, 8])
        
        #最大半径を設定
        max_radius = max(left, right, down, up)
        #ランダムで半径生成
        radius = self.rng.random() * max_radius
        
        
        
        if max_radius = left 
        
        
        