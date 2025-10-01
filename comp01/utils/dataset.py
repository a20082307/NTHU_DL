import pandas as pd
from torch.utils.data import Dataset, DataLoader

from utils.args import args

def load_train():
    train_df = pd.read_csv(args.train_path)
    