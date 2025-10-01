import matplotlib.pyplot as plt

from utils.args import args

class Plotter:
    def __init__(self):
        self.train_losses = []
        self.val_losses = []

    def plot(self):
        epochs = range(args.epochs)
        print(self.train_losses)
        print(epochs)

        plt.plot(epochs, self.train_losses, label = 'train loss')
        plt.plot(epochs, self.val_losses, label = 'validation loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        plt.savefig(args.result_path + 'loss_curve.png')
        plt.show()

    def plot_train_loss(self):
        ...

    def plot_val_loss(self):
        ...