""" Add Matplotlib figure to board. """
from matplotlib import pyplot as plt
from torch.utils.tensorboard import SummaryWriter


if __name__ == '__main__':
    # initialize
    board = SummaryWriter('runs/000')

    # make a figure to add
    plt.ion()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 10])
    ax.grid()
    fig.tight_layout()

    # add figure to board
    board.add_figure('Clamped quadratic', fig)

    # teardown
    board.close()
