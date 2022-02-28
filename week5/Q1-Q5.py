import torch
import torch.nn as nn
import torchvision.datasets as dset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

'''
Q1
학습 데이터 준비
MNIST 데이터셋을 직접 Load
데이터셋을 로드하고 DataLoader 구현
'''

training_epochs = 15  # training 반복 횟수
batch_size = 100 # 몇 개의 샘플로 가중치를 갱신할 것인지 설정

root = './data' # 데이터의 경로
mnist_train = dset.MNIST(root=root, train=True,
                         transform=transforms.ToTensor(), download=True)
mnist_test = dset.MNIST(root=root, train=False,
                        transform=transforms.ToTensor(), download=True)
            
# train : 테스트용 데이터를 가져올지 학습용 데이터를 가져올지 표시
# transforms.ToTensor()를 넣어서 일반 이미지를 pytorch tensor로 변환
# download : True로 설정하면 MNIST 데이터가 없으면 다운을 받는다.

train_loader = DataLoader(mnist_train, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(mnist_test, batch_size=batch_size, shuffle=False)

'''
Q2
데이터 학습할 모델 구현
모델 안의 가중치 초기화시키기
입력 데이터 형태(1차원)에 맞는 linear 모델 구성
'''

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
linear = torch.nn.Linear(784, 10, bias=True).to(device)
# 입력값은 28*28=784개이고, 출력값은 0~9까지 총 10개
# bias=True : 가중치 외에도 편향값도 사용

torch.nn.init.normal_(linear.weight)

'''
Q3
loss 함수와 optimizer 구현
'''

criterion = torch.nn.CrossEntropyLoss().to(device)
# torch.nn.CrossEntropyLoss를 이용하여 손실값을 구함

optimizer = torch.optim.SGD(linear.parameters(), lr=0.1)

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

'''
Q5
테스트 데이터를 이용해 테스트 진행
'''

linear.eval()
with torch.no_grad():
    correct = 0
    total = 0
    for i, (imgs, labels) in enumerate(test_loader):
        imgs, labels = imgs.to(device), labels.to(device)
        imgs = imgs.view(-1, 28*28)
        outputs = linear(imgs)
        _, argmax = torch.max(outputs, 1)
        total += imgs.size(0)
        correct += (labels == argmax).sum().item()

    print('Test accuracy for {} images: {:.2f}%'.format(total, correct/total*100))
