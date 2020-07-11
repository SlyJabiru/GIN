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

        self.backbone = eval(args.backbone)()
        self.backbone.conv1 = nn.Conv2d(22, 64, kernel_size=7, stride=2, padding=3, bias=False)
        self.backbone.fc = nn.Linear(self.backbone.fc.in_features, 1)

    def forward(self, x):
        x = f.leaky_relu(self.backbone(x))

        return x
