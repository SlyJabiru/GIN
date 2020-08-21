import cv2
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import argparse

from os import listdir, mkdir
from os.path import isfile, join, isdir, exists
from datetime import datetime, timedelta


def crop_func(folder):
    print(folder)

    save_root = join(folder, 'cropped')
    if not exists(save_root):
        print(f'mkdir {save_root}')
        mkdir(save_root)

    files = [join(folder, f) for f in listdir(folder) if isfile(join(folder, f))]

    for f in files:
        img = Image.open(f).convert('RGB')
        area = (64, 64, 832, 832)
        cropped = img.crop(area)
        numpy_image = np.array(cropped)

        for w in range(numpy_image.shape[0]):
            for h in range(numpy_image.shape[1]):
                color = numpy_image[w, h]
                b, g, r = color[0], color[1], color[2]
                if not ((b == 0 and g == 0 and r == 0) or (b == 0 and g == 0 and r == 255) or (
                            b == 0 and g == 255 and r == 0) or (b == 255 and g == 0 and r == 0) or (b == 255 and g == 255 and r == 255)):
                    numpy_image[w, h][0] = 0
                    numpy_image[w, h][1] = 0
                    numpy_image[w, h][2] = 0

        dt_str = f[-5:-17:-1][::-1]
        dt = datetime.strptime(dt_str, "%Y%m%d%H%M")
        kst = dt + timedelta(hours=9)

        save_path = join(save_root, kst.strftime("%Y%m%d%H%M")) + '.png'

        derived_img = Image.fromarray(numpy_image.astype('uint8'), 'RGB')
        derived_img.save(save_path)
        print(save_path)

    print('End of job')


if __name__ == '__main__':
    print('Main invoked!')
    parser = argparse.ArgumentParser(description='python Implementation')
    parser.add_argument('path', type=str, default=None, help='path')

    args = parser.parse_args()
    print(args)

    print('Path:', args.path)
    # print('start_dt:', args.start_dt)
    # print('end_dt:', args.end_dt)

    crop_func(args.path)
    # with open(save_path, "wb") as fd:
    #     fd.write(numpy_image)

# img = cv2.imread('/Users/leeseungjoon/Downloads/work/01/gk2a_ami_le2_dcoew-cot_ko020lc_202007011304.png')
# img = Image.open('/Users/leeseungjoon/Downloads/work_2/01/gk2a_ami_le2_cla-cll_ko020lc_202005312130.png').convert('RGB')
# img = Image.open('/Users/leeseungjoon/Downloads/work/01/gk2a_ami_le2_dcoew-cot_ko020lc_202007011304.png').convert('RGB')
#  size: (900, 922)
# img.show()
#
# area = (64, 64, 832, 832)
# # area = (900 - 350, 922 - 35, 888, 902)  # fixed.
# cropped = img.crop(area)
# cropped.show()
#
# open_cv_image = np.array(cropped)
# open_cv_image = open_cv_image[:, :].copy()
# # d = {}
#
# for w in range(open_cv_image.shape[0]):
#     for h in range(open_cv_image.shape[1]):
#         color = open_cv_image[w, h]
#         b, g, r = color[0], color[1], color[2]
#         if not ((b == 0 and g == 0 and r == 0) or (b == 0 and g == 0 and r == 255) or (
#                     b == 0 and g == 255 and r == 0) or (b == 255 and g == 0 and r == 0)):
#             open_cv_image[w, h][0] = 0
#             open_cv_image[w, h][1] = 0
#             open_cv_image[w, h][2] = 0
#
#
# image = Image.fromarray(open_cv_image.astype('uint8'), 'RGB')
# image.show()

#         d[(b, g, r)] = 1
#
# print(d.keys())
# print(len(d))
#
# color = ('b', 'g', 'r')
# for i,col in enumerate(color):
#     histr = cv2.calcHist([open_cv_image], [i], None, [256], [0, 256])
#     plt.subplot(3, 1, i + 1)
#     plt.plot(histr, color=col)
#     plt.xlim([0, 256])
# plt.show()
