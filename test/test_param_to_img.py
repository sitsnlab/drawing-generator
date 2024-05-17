# -*- coding: utf-8 -*-
"""画像作成のテスト.

Created on Fri May 17 01:07:37 2024.
@author: Yuta Kuronuma
"""

from img_writer.param_to_img import Param2Img
from PIL import ImageFont

if __name__ == '__main__':

    # 保存先
    path = '.'
    name = 'testimg.png'

    # 画像サイズ指定 デフォルト:(400, 280)
    size = (100, 70)

    # 描画用オブジェクト作成
    p2p = Param2Img(img_size=size)
    p2p.show_img()

    # 直線
    p2p.draw.line(xy=(0, 0, size[0], size[1]),
                  fill=(255, 0, 0), width=8)
    # 長方形
    p2p.draw.rectangle(xy=(size[0]/3, size[1]/3, size[0], size[1]),
                       fill=(0, 255, 0))
    # 楕円
    p2p.draw.arc(xy=(30, 30, 45, 40),
                 start=0, end=180, fill=(0, 0, 255), width=1)
    p2p.draw.arc(xy=(30, 30, 40, 40),
                 start=0, end=170, fill=(255, 0, 0), width=1)
    p2p.show_img()  # 画像表示
    p2p.reset_img()  # 画像リセット

    # テキスト描画
    font = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', size=10)
    font = None
    p2p.draw.multiline_text(xy=(0, 0),
                            text='Pillow sample', fill=(0, 0, 0), font=font)
    p2p.show_img()  # 画像表示
