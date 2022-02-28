import torch
import torch.nn as nn
import torchvision.datasets as dset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

'''
Q4
학습 Loop 구현
'''

'''
for문이 한번 돌때마다 batch_size만큼의 데이터를 꺼내서 학습시키는 것
즉, for문이 한번 돌면 1 epoch만큼 학습시킨 것
'''
for epoch in range(training_epochs):
    for i, (imgs, labels) in enumerate(train_loader):
        imgs, labels = imgs.to(device), labels.to(device)
        imgs = imgs.view(-1, 28*28)

        outputs = linear(imgs)
        loss = criterion(outputs, labels)

        optimizer.zero_grad() #gradient 값 초기화
        loss.backward() # gradient 값 갱신
        optimizer.step() # parameters 값 갱신

        _, argmax = torch.max(outputs, 1)
        accuracy = (labels == argmax).float().mean()

        if(i+1) % 100 == 0:
            print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}, Accuracy: {:.2f}%'.format(
                epoch+1, training_epochs, i+1, len(train_loader), loss.item(), accuracy.item()*100))
