from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from torch.utils.data import Dataset, DataLoader

from args import args
# from utils.args import args


class ModelDataset(Dataset):
    def __init__(self, data, labels):
        super().__init__()
        self.data = self.preprocess(data)
        self.labels = labels
        
    def preprocess(self):
        ...

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index], self.labels[index]


def load_train_data():
    rawData = pd.read_csv(args.train_path)
    
    trainIndices = np.random.choice(len(rawData), int(len(rawData) * args.ratio), replace = False)
    trainRawData = rawData.iloc[trainIndices]
    valRawData = np.setdiff1d(rawData.index, trainIndices)

    trainData, trainLabels = trainRawData[:, -1], trainRawData[:, 1]
    valData, valLabels = valRawData[:, -1], valRawData[:, 1]
    return trainData, trainLabels, valData, valLabels


if __name__ == '__main__':
    data, labels, _, _ = load_train_data()
    dataset = ModelDataset(data, labels)