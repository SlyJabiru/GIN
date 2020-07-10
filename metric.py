import torch


def rta_metric(y_pred, y):
    pass


def rts_metric(y_pred, y):
    ret = torch.sum(torch.abs(y_pred - y) * y) / torch.sum(y)
    return ret.item()
