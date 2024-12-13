# -*- coding: utf-8 -*-
"""arcエンティティの座標生成をするモジュール
Created on Thu May 23 15:47:55 2024

@author: AB21074
"""
from generator.param_generator import ParamGenerator
import numpy as np
import math as m

class ArcGenerator(ParamGenerator):
    """直線エンティティを生成するクラス."""

    def __init__(self, drawing_size: tuple[int] = (400, 400)):
        """イニシャライザ."""
        super().__init__(drawing_size)

    def gen_ent(self, size: int = 1):
        """任意サイズの弧のパラメータを生成する."""
        
        line_type = np.zeros([size, 1])
        pad = np.zeros([size,7])
        
        #中心座標を生成
        centers = self.gen_cord(size)
        
        
        #角度をランダムで作成
        start_angle =  self.rng.random([size,1]) *360
        end_angle =  start_angle + self.rng.random([size,1]) * 360
        
        
        #半径の配列を作成
        radius = np.zeros([size, 1])
        
        #元の開始角を求めるための数
        count = np.zeros([size,1])
        
        
        i = 0
        skip = 1
        for i in range(size):
            radius[i] = self.rng.random() * self.sizeX
            
            angle = start_angle[i]
            while angle <= end_angle[i]:
                point_x = centers[i,0] + radius[i] * m.cos(m.radians(angle))
                point_y = centers[i,1] - radius[i] * m.sin(m.radians(angle))
                
                if point_x < 0 or self.sizeX <point_x or point_y < 0 or self.sizeY < point_y:
                    radius[i] *= 0.8
                
                else:
                    angle += skip
                    count[i] += skip
                
        arcs = np.hstack([line_type,pad,centers,radius,start_angle-count,end_angle])    
        return arcs    
        
        
        
        
        '''
            #円弧の座標を１度ずつ変えて求める
            for angle in range(start_angle[i], end_angle[i] + 1, 5):
                
                point_x = centers[i,0] + m.cos(angle) * radius[i]
                point_y = centers[i,1] + m.sin(angle) * radius[i]
                
                #座標がサイズ内になければ半径を縮める
                if not 0 <= point_x <= self.sizeX and 0 <= point_y <= self.sizeY:
                    radius[i] -= 5
                
                else:
                    return radius[i]
            '''    
        
        pad = np.zeros([size, 7])
        
        return np.hstack([line_type,pad,centers,radius,start_angle,end_angle])
        
        
        