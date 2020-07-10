import argparse
from os.path import join, isfile

import torch
from torch import optim, nn

from dataset import *
from model import *
from metric import *
from trainer import Trainer
from utils import load_checkpoint


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='GIN Trainer')

    # training parameters
    parser.add_argument('--batch-size',
                        type=int, default=256)
    parser.add_argument('--epochs',
                        type=int, default=50)
    parser.add_argument('--lr',
                        type=float, default=0.001)
    parser.add_argument('--model',
                        type=str, default='RTS', choices=['RTS', 'RTA'])
    parser.add_argument('--device-ids',
                        type=int, nargs='+', default=None)

    # directory parameters
    parser.add_argument('--data-root',
                        type=str, default='./data')
    parser.add_argument('--save-dir',
                        type=str, default='./checkpoints')
    parser.add_argument('--load',
                        type=str, default=None)

    # model parameters
    parser.add_argument('--backbone',
                        type=str, default='resnet18', choices=['resnet18', 'resnet50', 'resnet101', 'resnet152'])
    parser.add_argument('--nlayers',
                        type=int, default=1)
    parser.add_argument('--nhids',
                        type=int, default=128)
    parser.add_argument('--dropout',
                        type=float, default=0.5)
    args = parser.parse_args()

    torch.manual_seed(1)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"{device} selected for training")

    train_data = eval(f"{args.model}Dataset")(join(args.data_root, 'train.csv'))
    valid_data = eval(f"{args.model}Dataset")(join(args.data_root, 'test.csv'))

    model = eval(f"{args.model}Net")(args)
    if args.device_ids and len(args.device_ids) > 1:
        model = nn.DataParallel(model, device_ids=[i for i in range(len(args.device_ids))])
    model.to(device)

    optimizer = optim.Adam(model.parameters(), lr=args.lr)

    if args.load:
        load_checkpoint(args.load, model, optimizer, args)

    criterion = nn.SmoothL1Loss() if args.model == "RTS" else nn.Softmax()
    metric = eval(f"{args.model.lower()}_metric")

    trainer = Trainer(model, optimizer, criterion, metric, train_data, valid_data, device, args)
    trainer.train()
