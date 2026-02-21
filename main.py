# -*- coding: utf-8 -*-
"""
generator CLI 

Example:
    python main.py \
        --type line \
        --img_size 224 224 \
        --drawing_size 400 280 \
        --out_dir ./EntityImages \
        --name my_experiment
"""

import argparse
from pathlib import Path
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from csv_io import CsvIO


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--type",
        type=str,
        required=True,
        choices=["line", "arc", "circle"],
        help="Entity type"
    )

    parser.add_argument("--num", type=int, default=1000)

    parser.add_argument(
        "--img_size",
        type=int,
        nargs=2,
        metavar=("WIDTH", "HEIGHT"),
        default=(224, 224),
        help="Image size (width height)"
    )

    parser.add_argument(
        "--drawing_size",
        type=int,
        nargs=2,
        metavar=("WIDTH", "HEIGHT"),
        default=(400, 400),
        help="Drawing size (width height)"
    )

    parser.add_argument(
        "--out_dir",
        type=str,
        default="EntityImages",
        help="Output base directory"
    )

    parser.add_argument(
        "--name",
        type=str,
        default=None,
        help="Output dataset name"
    )

    args = parser.parse_args()

    ent_type = args.type
    ent_num = args.num
    img_size = tuple(args.img_size)
    drawing_size = tuple(args.drawing_size)

    # entityごとに切り替え
    if ent_type == "line":
        from generator.line_generator import LineGenerator
        from img_writer.line_to_img import Line2Img
        Generator = LineGenerator
        ImgWriter = Line2Img

    elif ent_type == "arc":
        from generator.arc_generator import ArcGenerator
        from img_writer.arc_to_img import Arc2Img
        Generator = ArcGenerator
        ImgWriter = Arc2Img

    elif ent_type == "circle":
        from generator.circle_generator import CircleGenerater
        from img_writer.circle_to_img import Circle2Img
        Generator = CircleGenerater
        ImgWriter = Circle2Img

    else:
        raise ValueError("Unknown type")

    # ★ 名前決定ロジック
    if args.name is not None:
        data_name = args.name
    else:
        data_name = f"{ent_type}_{img_size[0]}x{img_size[1]}"

    base_dir = Path(args.out_dir)
    directry = base_dir / data_name
    directry.mkdir(parents=True, exist_ok=True)

    csvpath = directry / f"{data_name}.csv"

    # パラメータ生成
    generator = Generator(drawing_size=drawing_size)
    entities = generator.gen_ent(ent_num)

    # CSV保存
    CsvIO.write_csv(entities, csvpath)
    params = CsvIO.read_csv(csvpath)

    print("Generated shape:", params.shape)
    print("Output directory:", directry.resolve())

    # 画像生成
    img_writer = ImgWriter(img_size=img_size, drawing_size=drawing_size)
    img_writer.draw_imgs(params, directry)

    print("Done.")


if __name__ == "__main__":
    main()