import torch
import torch.nn as nn
import torchvision.datasets as dset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt


training_epochs = 15  # training 반복 횟수 / 에폭
batch_size = 100 # 몇 개의 샘플로 가중치를 갱신할 것인지 설정 / 배차크기

root = './data' 
mnist_train = dset.MNIST(root=root, train=True,
                         transform=transforms.ToTensor(), download=True)
mnist_test = dset.MNIST(root=root, train=False, 
                        transform=transforms.ToTensor(), download=True)

train_loader = DataLoader(mnist_train, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(mnist_test, batch_size=batch_size, shuffle=False)

# Dataloader에 저장된 이미지를 출력해본다.
train_features, train_labels = next(iter(train_loader))
img = train_features[1].squeeze()
label = train_labels[1]
plt.imshow(img, cmap="gray")
plt.show()
print(f"Label: {label}")