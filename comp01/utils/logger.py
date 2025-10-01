import logging
import os
import sys

from utils.args import args


class Logger:
    def __init__(self):
        if not os.path.exists(args.result_path):
            os.makedirs(args.result_path)

        # with open(args.result_path + 'log.log', 'w') as file:
        #     pass

        formatter = logging.Formatter(
            "%(asctime)s | [%(levelname)s]  %(message)s",
            datefmt = '%Y-%m-%d %H:%M:%S'
        )

        file_handler = logging.FileHandler(args.result_path + 'log.log')
        file_handler.setFormatter(formatter)

        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(formatter)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(self.stream_handler)

    def print(self, message):
        self.logger.info(message)

    def log(self, message):
        self.logger.removeHandler(self.stream_handler)
        self.logger.info(message)
        self.logger.addHandler(self.stream_handler)


logger = Logger()


if __name__ == '__main__':
    logger.print("test123")
    logger.print("test456")