import numpy as np
from os.path import join
from PIL import Image
import torch
from datetime import datetime, timedelta


def save_checkpoint(tag, model, optimizer, multi_gpu, save_dir):
    print('Snapshot Checkpoint...')
    if multi_gpu:
        model_state_dict = model.module.state_dict()
    else:
        model_state_dict = model.state_dict()

    torch.save({
        'model': model_state_dict,
        'optimizer': optimizer.state_dict()
    }, join(save_dir, str(tag) + '.pth'))


def load_checkpoint(file, model, optimizer, multi_gpu):
    state_dict = torch.load(file, map_location='cpu')
    if multi_gpu:
        model.module.load_state_dict(state_dict['model'])
    else:
        model.load_state_dict(state_dict['model'])
    optimizer.load_state_dict(state_dict['optimizer'])


def read_image(root_dir, key):
    w, h = 768, 768
    ret = np.empty((w, h, 0))
    date_format = "%Y%m%d%H%M"
    base_date = datetime.strptime(str(key), date_format)

    for i in range(3):
        img_name = base_date - timedelta(hours=0, minutes=10 * i)
        img_name = img_name.strftime(date_format)

        img = Image.open(f"{root_dir}/{img_name}.png").convert("RGB")
        img = np.array(img)

        ret = np.concatenate((ret, img), axis=2)

    return ret
