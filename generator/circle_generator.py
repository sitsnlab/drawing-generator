from generator.param_generator import ParamGenerator
import numpy as np

class CircleGenerater(ParamGenerator):
    """"円エンティティを生成するクラス."""
    
    def __init__(self, drawing_size: tuple[int] = (400, 280)):
        """イニシャライザ."""
        super().__init__(drawing_size)
    
    def gen_ent(self, size: int = 1):
        """任意サイズの円の中心と半径を生成する."""
        centers = self.gen_cord(size)
        radii = np.zeros(size)
        pad = np.zeros([size, 5])

        for i, (x, y) in enumerate(centers):
            max_radius_x = min(x, self.sizeX - x)
            max_radius_y = min(y, self.sizeY - y)
            max_radius = min(max_radius_x, max_radius_y)
            radii[i] = self.rng.random() * max_radius
        
        radii = radii.reshape(size,1)    
        circles = np.hstack([pad,centers,radii,pad])
        return circles
        
     
