import torch
import torch.nn as nn
import torchvision.datasets as dset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

'''
Q2
데이터 학습할 모델 구현
모델 안의 가중치 초기화시키기
입력 데이터 형태(1차원)에 맞는 linear 모델 구성
'''

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
linear = torch.nn.Linear(784, 10, bias=True).to(device)

torch.nn.init.normal_(linear.weight)

print(torch.cuda.is_available())
