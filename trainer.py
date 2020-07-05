import torch


class Trainer:
    def __init__(self, model, optimizer, criterion, metric, train_data, valid_data, device, args):
        self.model = model
        self.optimizer = optimizer
        self.criterion = criterion
        self.metric = metric
        self.train_data = train_data
        self.valid_data = valid_data
        self.device = device
        self.args = args

    def train(self):
        pass
