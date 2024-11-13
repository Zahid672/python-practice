import os 

from PIL import Image
import matplotlib.pyplot as plt


import torch
from torchvision import transforms as t
from torch.utils.data import Dataset, dataloader


class ScalpDataset(Dataset):
    def __init__(self, data_dir, task, transform=None, target_transform=None):
        super().__init__()
        self.data_dir = data_dir
        self.task = task

        self.image_names, self.labels = self.__process_data()

        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.image_names)
    
    def __getitem__(self, index):
        image_name = self.image_names[index]
        label = self.labels[index]

        label_map = {0: '_0. Good', 1: '_1. Mild', 2: '_2. Moderate', 3:'_3. Severe'}

        label_directory = f'[Source] {self.task}{label_map[label]}'
        image_path = os.path.join(self.data_dir, label_directory, image_name)
        image = Image.open(image_path)

        if self.transform:
            image = self.transform(image)

        if self.target_transform:
            label = self.target_transform(label)

            return image, label
        

        def __process_data(self):

            ## [Source] Interfollicular erythema_1. Mild
            Good_images = os.listdir(os.path.join(self.data_dir, f'[Source] {self.task}_0. Good'))
            Mild_images = os.listdir(os.path.join(self.data_dir, f'[Source] {self.task}_1. Mild'))
            Moderate_images = os.listdir(os.path.join(self.data_dir, f'[Source] {self.task}_2. Moderate_images'))
            Severe_images = os.listdir(os.path.join(self.data_dir, f'[Source] {self.task}_3. Severe'))
        

        ### filtering only jpg images

        Good_images = [image_name for image_name in Good_images if '.jpg' in image_name]
        Mild_images = [image_name for image_name in Mild_images if '.jpg' in image_name]
        Moderate_images = [image_name for image_name in Moderate_images if '.jpg' in image_name]
        Severe_images = [image_name for image_name in Severe_images if '.jpg' in image_name]

        ## Combining all the data

        combined_images = Good_images + Mild_images + Moderate_images + Severe_images
        labels = [0]*len(Good_images) + [1]*len(Mild_images) + [2]*len(Moderate_images) + [3]*len(Severe_images)

        return combined_images


if __name__ == '__main__':
    main_dir = 'Dataset'
    train_dir = os.path.join(main_dir, "Training")
    test_dir = os.path.join(main_dir, "Validation")

    task = "Interfollicular erythema"


