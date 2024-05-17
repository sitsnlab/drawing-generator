# -*- coding: utf-8 -*-
"""画像サイズ設定と図形の描画を行う.

Created on Tue Apr  9 12:49:17 2024.
@author: Yuta Kuronuma
"""

from PIL import Image, ImageDraw
from pathlib import Path as plib
from tqdm import tqdm
import numpy as np


class Param2Img:
    """座標を指定したサイズの画像に描画するベースクラス."""

    canvas: Image.Image | None = None

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
        self.drawing_size = drawing_size
        self.img_size = img_size
        self.background = background
        self.reset_img()
        self.dim_rate = (img_size[0]/drawing_size[0],
                         img_size[1]/drawing_size[1])

    def reset_img(self):
        """画像の初期化."""
        self.canvas = Image.new(mode='RGB', size=self.img_size,
                                color=self.background)
        self.draw = ImageDraw.Draw(self.canvas)

    def convert_cood(self, xy: tuple[float]) -> tuple[float]:
        """図面上の座標を画像の位置へ変換する.

        Parameters
        ----------
        xy : tuple[float]
            変換対象となる座標.

        Returns
        -------
        tuple[float]
            変換後の座標.

        """
        xy[1] = self.drawing_size[1] - xy[1]
        return xy[0] * self.dim_rate[0], xy[1] * self.dim_rate[1]

    def save_img(self, directory, name):
        """画像を書き出す.

        Parameters
        ----------
        directory : TYPE
            保存先のディレクトリ.
        name : TYPE
            ファイル名.

        Returns
        -------
        None.

        """
        path = plib(directory)
        path = path / name
        self.canvas.save(fp=path, quality=95)

    def show_img(self):
        """画像を表示する."""
        self.canvas.show()

    def draw_imgs(self, params: np.ndarray, directory: str = r".\a"):
        r"""入力されたパラメータに合わせて図形画像を作成する.

        Parameters
        ----------
        params : np.ndarray
            エンティティのリスト.　(n*13)
        directory : str, optional
            保存先. The default is r".\a".

        Returns
        -------
        None.

        """
        for i, param in tqdm(enumerate(params)):
            name = 'p{:0=5}.jpg'.format(i)
            self.draw_ent(param)
            self.save_img(directory, name)
            self.reset_img()

    def draw_ent(self, param: np.ndarray,
                 target: ImageDraw.ImageDraw | None = None,
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
        pass
