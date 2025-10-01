import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--train_path', type = str, default = './data/train.csv')
parser.add_argument('--test_path', type = str, default = './data/test.csv')
parser.add_argument('--random_seed', '-r', type = int, dest = 'random_seed', default = 42)
parser.add_argument('--learning_rate', '-lr', type = float, dest = 'lr', default = 1e-3)
parser.add_argument('--batch_size', '-b', type = int, dest = 'batch', default = 32)
parser.add_argument('--epochs', '--epoch', '-e', type = int, dest = 'epochs', default = 50)
parser.add_argument('--result_path', '-rp', type = str, default = './result/test/')
parser.add_argument(
    '--ratio', type = float, default = 0.8, 
    help = 'The ratio of training set while splitting the raw training dataset'
)

args = parser.parse_args()

if __name__ == '__main__':
    print(args)