from argparse import ArgumentParser

def get_args():
    parser = ArgumentParser()
    parser.add_argument("--width", type = int, default=30)
    parser.add_argument("--height", type = int, default=30)
    parser.add_argument("--block_size", type = int, default=20)
    parser.add_argument("--snake_length", type = int, default=4)
    parser.add_argument("--snake_speed", type = int, default=10)

    return parser.parse_args()