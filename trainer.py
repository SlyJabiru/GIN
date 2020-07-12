import torch
from torch.utils.data import DataLoader

from utils import save_checkpoint


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
        self.multi_gpu = args.device_ids and len(args.device_ids) > 1

    def train(self):
        best_metric = 1e9

        train_loader = DataLoader(
            dataset=self.train_data,
            shuffle=True,
            num_workers=1,
            batch_size=self.args.batch_size
        )
        valid_loader = DataLoader(
            dataset=self.valid_data,
            shuffle=False,
            num_workers=1,
            batch_size=self.args.batch_size
        )

        for epoch in range(1, self.args.epochs + 1):
            print(f"<Epoch {epoch:2d}>")

            self.model.train()
            train_loss, train_metric = self._train_epoch(train_loader, True)

            self.model.eval()
            valid_loss, valid_metric = self._train_epoch(valid_loader, False)

            print(f"Train / Loss: {train_loss} / Metric: {train_metric}")
            print(f"Valid / Loss: {valid_loss} / Metric: {valid_metric}")

            if best_metric > valid_metric:
                best_metric = valid_metric
                save_checkpoint(
                    "best_model",
                    self.model,
                    self.optimizer,
                    self.multi_gpu,
                    self.args.save_dir
                )
            save_checkpoint(
                f"checkpoint_{epoch}",
                self.model,
                self.optimizer,
                self.multi_gpu,
                self.args.save_dir
            )

    def _train_epoch(self, loader, is_train):
        total_loss = 0.0
        preds = []
        reals = []

        for batch, (x, y) in enumerate(loader):
            if is_train:
                self.optimizer.zero_grad()
            x, y = x.to(self.device), y.to(self.device)
            y_pred = self.model(x)

            y, y_pred = y.view(-1), y_pred.view(-1)
            preds = preds + y_pred.tolist()
            reals = reals + y.tolist()

            loss = self.criterion(y_pred, y)
            if is_train:
                loss.backward()
            del x, y

            total_loss = batch / (batch + 1) * total_loss + loss.item() / (batch + 1)

        return total_loss, self.metric(preds, reals)
