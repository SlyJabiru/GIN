from os.path import join
import numpy as np
from torch.utils.data import Dataset

from utils import read_image


class RTADataset(Dataset):
    def __init__(self, label_file, radar_root):
        pass

    def __getitem__(self, idx):
        pass

    def __len__(self):
        pass


class RTSDataset(Dataset):
    def __init__(self, label_file, radar_root):
        cot_root = join(radar_root, 'COT')
        cll_root = join(radar_root, 'CLL')
        w, h = 768, 768

        raw_data = np.loadtxt(label_file, delimiter=',', dtype=np.float32)
        self.x = np.empty((0, w, h, 10))
        self.y = raw_data[:, 1]
        self.cnt = self.y.shape[0]

        for idx in range(raw_data.shape[0]):
            row = raw_data[idx]
            radar_name = f"{row[0]}.png"
            cot_img = read_image(join(cot_root, radar_name)) / 255.0
            cll_img = read_image(join(cll_root, radar_name)) / 255.0

            month = np.full((w, h, 1), int(row[0][4:6]) / 12.0)
            day = np.full((w, h, 1), int(row[0][6:8]) / 31.0)
            hour = np.full((w, h, 1), int(row[0][8:10]) / 24.0)
            minutes = np.full((w, h, 1), int(row[0][10:12]) / 60.0)

            x_data = np.concatenate(
                (
                    cot_img,
                    cll_img,
                    month,
                    day,
                    hour,
                    minutes
                ), axis=2)
            self.x = np.append(self.x, x_data.reshape((1, w, h, 10)))

    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]

    def __len__(self):
        return self.cnt

