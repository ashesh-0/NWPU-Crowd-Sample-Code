import torch
import torch.nn as nn
import torch.nn.functional as F
from config import cfg
from misc.layer import FC, Conv2d
from misc.utils import *
from torchvision import models


class VGG(nn.Module):
    def __init__(self):
        super(VGG, self).__init__()
        vgg = models.vgg16(pretrained=True)

        features = list(vgg.features.children())
        self.features4 = nn.Sequential(*features[0:23])

        self.de_pred = nn.Sequential(Conv2d(512, 128, 1, same_padding=True, NL='relu'),
                                     Conv2d(128, 1, 1, same_padding=True, NL='relu'))

    def forward(self, x):
        x = self.features4(x)
        x = self.de_pred(x)

        x = F.interpolate(x, scale_factor=8, mode='bilinear')

        return x
