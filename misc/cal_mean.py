import argparse
import os

import numpy as np
from PIL import Image


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trainDataPath',
                        type=str,
                        default='/media/E/own_open_source/ProcessedData/Data.2019.11/NWPU/1129_min_576x768_mod16/img',
                        help='absolute path to your data path')
    return parser


if __name__ == '__main__':
    args = make_parser().parse_args()

    imgs_list = []

    for i_img, img_name in enumerate(os.listdir(args.trainDataPath)):
        if i_img % 100 == 0:
            print(i_img)
        img = Image.open(os.path.join(args.trainDataPath, img_name))
        if img.mode == 'L':
            img = img.convert('RGB')

        img = np.array(img.resize((1024, 768), Image.BILINEAR))

        imgs_list.append(img)

    imgs = np.array(imgs_list).astype(np.float32) / 255.
    red = imgs[:, :, :, 0]
    green = imgs[:, :, :, 1]
    blue = imgs[:, :, :, 2]

    print("means: [{}, {}, {}]".format(np.mean(red), np.mean(green), np.mean(blue)))
    print("stdevs: [{}, {}, {}]".format(np.std(red), np.std(green), np.std(blue)))
