import torch
from tqdm import tqdm

from utils.args import args
from utils.logger import logger
from utils.plotter import Plotter
from utils.dataset import ModelDataset, load_train_data


def train():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    logger.print(f'Using device: {device}')

    train_dataset, train_labels, val_dataset, val_labels = load_train_data()
    train_loader = torch.utils.data.DataLoader(
        train_dataset, 
        batch_size = args.batch_size, 
        shuffle = True,
        num_workers = 8,
        pin_memory = True
    )
    val_loader = torch.utils.data.DataLoader(
        val_dataset, 
        batch_size = args.batch_size, 
        shuffle = False,
        num_workers = 8,
        pin_memory = True
    )

    model = ...
    optimizer = torch.optim.Adam(model.parameters(), lr = args.lr)
    criterion = torch.nn.BCEWithLogitsLoss()
    plotter = Plotter()

    for epoch in range(args.epochs):
        model.train()
        for idx, (data, label) in enumerate(tqdm(train_loader, desc = f'[Epoch {epoch + 1}] Training: ')):
            optimizer.zero_grad()

            data, label = data.to(device), label.to(device)
            output = model(data)
            loss = criterion(output, label)
            loss.backward()
            optimizer.step()

            plotter.train_losses.append(loss.item())

        model.eval()
        with torch.no_grad():
            for idx, (data, label) in enumerate(tqdm(val_loader, desc = f'[Epoch {epoch + 1}] Validation: ')):
                data, label = data.to(device), label.to(device)
                output = model(data)
                loss = criterion(output, label)
                plotter.val_losses.append(loss.item())

    plotter.plot()


if __name__ == '__main__':
    train()