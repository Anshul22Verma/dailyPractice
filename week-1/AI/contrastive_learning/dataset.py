import cv2
import numpy as np
import pandas as pd
import random
import torch
from torch.utils.data import Dataset
from torchvision import transforms


class GaussianNoiseTransform:
    def __init__(self, mean=0.0, std=1.0):
        """
        Args:
            mean (float): Mean of the Gaussian noise.
            std (float): Standard deviation of the Gaussian noise.
        """
        self.mean = mean
        self.std = std

    def __call__(self, tensor):
        """
        Args:
            tensor (Tensor): Input image tensor (C, H, W) normalized to [0, 1].

        Returns:
            Tensor: Image tensor with added Gaussian noise.
        """
        noise = torch.randn(tensor.size()) * self.std + self.mean
        noisy_tensor = tensor + noise
        return torch.clamp(noisy_tensor, 0.0, 1.0)  # Ensure pixel values stay in [0, 1]


class ContrastiveDataset(Dataset):
    def __init__(self, phase: str, img_path_df: pd.DataFrame, MEAN: float, STD: float):
        """
            phase: train / validation
            img_path_df: a dataframe with image path in a column named `image`
            MEAN: Mean of training images for normalizing images
            STD: Standard-deviation of training images for normalizing images
        """
        self.phase = phase
        self.img_path_df = img_path_df
        self.MEAN = MEAN  # np.mean(trimages/255.0,axis=(0,2,3),keepdims=True)
        self.STD = STD  # np.std(trimages/255.0,axis=(0,2,3),keepdims=True)
        self.transforms = transforms.Compose([
            transforms.RandomHorizontalFlip(0.5),
            transforms.RandomResizedCrop(32, (0.8, 1.0)),
            # color augmentation
            transforms.Compose([
                transforms.RandomApply([transforms.ColorJitter(0.8, 0.8, 0.8, 0.2)], p = 0.8),
                transforms.RandomGrayscale(p=0.2),
                # SOBEL FILTERING - NOT adding right now
                # GAUSSIAN NOISE
                transforms.RandomApply([GaussianNoiseTransform(mean=0.0, std=1.0)], p=0.5),
                # GAUSSIAN BLURRING
                transforms.RandomApply([transforms.GaussianBlur(kernel_size=5, sigma=(0.1, 2.0))], p=0.5),
            ]),
        ])

    def __len__(self):
        return len(self.img_path_df)

    def __getitem__(self,idx):
        
        img_path = self.img_path_df.iloc[idx]["image"]
        x = cv2.imread(img_path)
        
        #print(x.shape)
        x = x.astype(np.float32)/255.0

        x1 = self.augment(torch.from_numpy(x))
        x2 = self.augment(torch.from_numpy(x))
        
        x1 = self.preprocess(x1)
        x2 = self.preprocess(x2)
        return x1, x2

    #shuffles the dataset at the end of each epoch
    def on_epoch_end(self):
        self.imgarr = self.imgarr[random.sample(population = list(range(self.__len__())),k = self.__len__())]

    def preprocess(self, frame):
        frame = (frame-self.MEAN)/self.STD
        return frame
    
    #applies randomly selected augmentations to each clip (same for each frame in the clip)
    def augment(self, frame, transformations = None):
        if self.phase == 'train':
            frame = self.transforms(frame)
            return frame
        else:
            return frame
