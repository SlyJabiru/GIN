from multiprocessing import Process
from PIL import Image
import numpy as np
from os import listdir, mkdir, getpid
from os.path import isfile, join, isdir, exists
from datetime import datetime, timedelta


def crop(folder):
    proc = getpid()
    save_root = join(folder, 'cropped')
    if not exists(save_root):
        print(f'mkdir {save_root} by process id: {proc}')
        mkdir(save_root)
    files = [join(folder, f) for f in listdir(folder) if isfile(join(folder, f))]
    for f in files:
        img = Image.open(f).convert('RGB')
        area = (64, 64, 832, 832)
        cropped = img.crop(area)
        numpy_image = np.array(cropped)
        # for w in range(numpy_image.shape[0]):
        #     for h in range(numpy_image.shape[1]):
        #         color = numpy_image[w, h]
        #         b, g, r = color[0], color[1], color[2]
        #         if not ((b == 0 and g == 0 and r == 0) or (b == 0 and g == 0 and r == 255) or (
        #                     b == 0 and g == 255 and r == 0) or (b == 255 and g == 0 and r == 0) or (b == 255 and g == 255 and r == 255)):
        #             numpy_image[w, h][0] = 0
        #             numpy_image[w, h][1] = 0
        #             numpy_image[w, h][2] = 0
        dt_str = f[-5:-17:-1][::-1]
        dt = datetime.strptime(dt_str, "%Y%m%d%H%M")
        kst = dt + timedelta(hours=9)
        save_path = join(save_root, kst.strftime("%Y%m%d%H%M")) + '.png'
        derived_img = Image.fromarray(numpy_image.astype('uint8'), 'RGB')
        derived_img.save(save_path)
        print(f'Saved {save_path} by process id: {proc}')
    print(f'End of job. folder: {folder}, process id: {proc}')


arg_dict = {
    '4111': ['/home/gcp_study_sjlee/for-image-crop-bucket/4111/01/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4111/02/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4111/03/'],
    '4112': ['/home/gcp_study_sjlee/for-image-crop-bucket/4112/01/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4112/02/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4112/03/'],
    '4113': ['/home/gcp_study_sjlee/for-image-crop-bucket/4113/01/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4113/02/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4113/03/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4113/04/'],
    '4114': ['/home/gcp_study_sjlee/for-image-crop-bucket/4114/01/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4114/02/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4114/03/'],
    '4115': ['/home/gcp_study_sjlee/for-image-crop-bucket/4115/01/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4115/02/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4115/03/'],
    '4126': ['/home/gcp_study_sjlee/for-image-crop-bucket/4126/01/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4126/02/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4126/03/'],
    '4127': ['/home/gcp_study_sjlee/for-image-crop-bucket/4127/01/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4127/02/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4127/03/'],
    '4128': ['/home/gcp_study_sjlee/for-image-crop-bucket/4128/01/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4128/02/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4128/03/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4128/04/']
}
if __name__ == '__main__':
    for k in arg_dict:
        path_list = arg_dict[k]
        procs = []
        for path in path_list:
            proc = Process(target=crop, args=(path,))
            procs.append(proc)
            proc.start()
        for proc in procs:
            proc.join()
