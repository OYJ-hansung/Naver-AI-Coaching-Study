import torch
import torch.nn as nn
import torchvision.datasets as dset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader


'''
Q3
loss 함수와 optimizer 구현
'''

criterion = torch.nn.CrossEntropyLoss().to(device)
# torch.nn.CrossEntropyLoss를 이용하여 손실값을 구함
optimizer = torch.optim.SGD(linear.parameters(), lr=0.1)
