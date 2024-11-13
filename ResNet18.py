import torch
from torch import nn
import torch.functional as f
import torch.nn.functional as F


class ResNetBlock(nn.Module):
    def __init__(self, in_channels, out_channels, kernel=3, first_stride=1, padding=1, dropout=0.1):
        super().__init__()

        self.block = nn.Sequential(
            nn.Conv2d(in_channels=in_channels, out_channels=out_channels, stride=first_stride, padding=padding, kernel_size=kernel),
            nn.BatchNorm2d(num_features=out_channels),
            nn.ReLU(inplace=True),
            nn.Dropout2d(p=dropout),
            nn.Conv2d(in_channels=out_channels, out_channels=out_channels, stride=1, padding=padding, kernel_size=kernel),
            nn.BatchNorm2d(num_features=out_channels), 
            nn.Dropout2d(p=dropout),
        )


        self.skip_connection = nn.Sequential(
            nn.Conv2d(in_channels=in_channels, out_channels=out_channels, stride=first_stride, padding=padding, kernel_size=kernel),
            nn.BatchNorm2d(num_features=out_channels)
        )
        self.relu = nn.ReLU()

    def forward(self, x):
        x1 = self.block(x)
        x2 = self.skip_connection(x)

        x3 = x1 + x2

        x4 = self.relu(x3)
        return x4

class ResNet18(nn.Module):
    def __init__(self, in_channels, out_classes):
        super().__init__()

        self.in_channels = in_channels
        self.out_classes = out_classes

        self.conv1 = nn.Sequential(
            nn.Conv2d(in_channels=self.in_channels, out_channels=64, kernel_size=7, stride=2, padding=3),
            nn.BatchNorm2d(num_features=64),
            nn.ReLU(inplace=True)
        )

        self.conv2_1 =ResNetBlock(in_channels=64, out_channels=64, kernel=3, first_stride=1)
        self.conv2_2 = ResNetBlock(in_channels=64, out_channels=64, kernel=3, padding=1)

        self.conv3_1 = ResNetBlock(in_channels=64, out_channels=128, kernel=3, padding=1, first_stride=2)
        self.conv3_2 = ResNetBlock(in_channels=128, out_channels=128, kernel=3, padding=1, first_stride=1)

        self.conv4_1 = ResNetBlock(in_channels=128, out_channels=256, kernel=3, padding=1, first_stride=2)
        self.conv4_2 = ResNetBlock(in_channels=256, out_channels=256, kernel=3, padding=1, first_stride=1)

        self.conv5_1 = ResNetBlock(in_channels=256, out_channels=512, kernel=3, padding=1, first_stride=2)
        self.conv5_2 = ResNetBlock(in_channels=512, out_channels=512, kernel=3, padding=1, first_stride=1)

        self.relu = nn.ReLU()
        self.max_pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=1)
        self.avg_pool = nn.AvgPool2d(kernel_size=2, stride=2)

        self.fc1 = nn.Linear(in_features=512*8*8, out_features=2048)
        self.fc2 = nn.Linear(in_features=2048, out_features=out_classes)

        def forward(self, x):
        x = self.conv1(x)

        x = self.max_pool(x)

        x = self.conv2_1(x)
        x = self.conv2_2(x)


        x = self.conv3_1(x)
        x = self.conv3_2(x)

        x = self.conv4_1(x)
        x = self.conv4_2(x)

        x = self.conv5_1(x)
        x = self.conv5_2(x)

        x = self.avg_pool(x)

        x = x.view(-1, 512*8*8)

        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)

        x1 = torch.softmax(x, dim=1)
        return x1
        
if __name__ == "__main__":

    x = torch.rand(size=(8,3,512,512))
    print(x.shape)

    model = ResNet18(in_channels=3, out_classes=2)

    output = model(x)

    print("Output: ", output.shape)