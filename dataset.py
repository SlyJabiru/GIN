from os.path import join
from math import floor
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
        raw_data = np.loadtxt(
            label_file,
            delimiter=',',
            dtype={
                "names": ("date", "energy"),
                "formats": ("i8", "f4")
            })

        self.radar_root = radar_root
        self.w, self.h = 768, 768

        self.rows = raw_data
        self.cnt = self.rows.shape[0]

    def __getitem__(self, idx):
        cot_root = join(self.radar_root, "COT")
        cll_root = join(self.radar_root, "CLL")
        row = self.rows[idx]

        cot_img = read_image(cot_root, row[0])
        cll_img = read_image(cll_root, row[0])

        month = np.full((self.w, self.h, 1), floor(row[0] % 1e8 / 1e6) / 12.0, dtype=np.float32)
        day = np.full((self.w, self.h, 1), floor(row[0] % 1e6 / 1e4) / 31.0, dtype=np.float32)
        hour = np.full((self.w, self.h, 1), floor(row[0] % 1e4 / 1e2) / 24.0, dtype=np.float32)
        minutes = np.full((self.w, self.h, 1), row[0] % 1e2 / 60.0, dtype=np.float32)

        x_data = np.concatenate(
            (
                cot_img,
                cll_img,
                month,
                day,
                hour,
                minutes
            ), axis=2)

        return np.transpose(x_data, (2, 0, 1)), row[1]

    def __len__(self):
        return self.cnt
