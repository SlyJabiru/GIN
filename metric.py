import numpy as np


def rta_metric(y_pred, y):
    pass


def rts_metric(y_pred, y):
    y_pred, y = np.array(y_pred), np.array(y)
    ret = np.sum(np.abs(y_pred - y) * y) / np.sum(y)
    return ret
