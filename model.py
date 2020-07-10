from torch import nn
from torch.nn import functional as f
from torchvision.models import resnet18, resnet50, resnet101, resnet152


def _stack_linear_layers(nhids, nlayers, dropout):
    return [
        nn.Sequential(
            nn.Linear(nhids, nhids),
            nn.LayerNorm(nhids),
            nn.LeakyReLU(),
            nn.Dropout(dropout)
        ) for _ in range(nlayers)]


class RTANet(nn.Module):
    def __init__(self, args):
        super().__init__()

    def forward(self, x):
        pass


class RTSNet(nn.Module):
    def __init__(self, args):
        super().__init__()

        self.backbone = eval(args.backbone)
        self.backbone.fc = nn.Linear(self.backbone.fc.in_features, args.nhids)

        layers = _stack_linear_layers(args.nhids, args.nlayers, args.dropout)
        self.fc = nn.Sequential(*layers)
        self.decoder = nn.Linear(args.nhids, 1)

    def forward(self, x):
        x = self.backbone(x)
        x = self.fc(x)
        x = f.leaky_relu(self.decoder(x))

        return x
