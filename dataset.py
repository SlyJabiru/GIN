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
        cot_root = join(radar_root, 'COT')
        cll_root = join(radar_root, 'CLL')
        w, h = 768, 768

        raw_data = np.loadtxt(
            label_file,
            delimiter=',',
            dtype={
                "names": ("date", "energy"),
                "formats": ("i8", "f4")
            })

        self.x = np.empty((0, w, h, 22))
        self.y = np.empty((0, 1))

        for idx in range(raw_data.shape[0]):
            try:
                row = raw_data[idx]
                cot_img = read_image(cot_root, row[0]) / 255.0
                cll_img = read_image(cll_root, row[0]) / 255.0

                month = np.full((w, h, 1), floor(row[0] % 1e8 / 1e6) / 12.0)
                day = np.full((w, h, 1), floor(row[0] % 1e6 / 1e4) / 31.0)
                hour = np.full((w, h, 1), floor(row[0] % 1e4 / 1e2) / 24.0)
                minutes = np.full((w, h, 1), row[0] % 1e2 / 60.0)

                x_data = np.concatenate(
                    (
                        cot_img,
                        cll_img,
                        month,
                        day,
                        hour,
                        minutes
                    ), axis=2)
                self.x = np.concatenate((self.x, x_data.reshape((1, w, h, 22))), axis=0)
                self.y = np.append(self.y, row[1])
            except FileNotFoundError as err:
                print(err)
        self.x = np.transpose(self.x.astype('float32'), (0, 3, 1, 2))
        self.y = self.y.astype('float32')
        self.cnt = self.x.shape[0]

    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]

    def __len__(self):
        return self.cnt


if __name__ == "__main__":
    dataset = RTSDataset('data/test.csv', 'data/radar')
    print(dataset[0])
