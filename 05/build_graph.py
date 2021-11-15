import numpy as np


def build_graph_lab6(x_1, y_1, x_2, y_2, path):
    import matplotlib.pyplot as plt
    from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)  

    fig, ax = plt.subplots()

    # set the x-spine (see below for more info on `set_position`)
    ax.spines['left'].set_position('zero')

    # turn off the right spine/ticks
    ax.spines['right'].set_color('none')
    ax.yaxis.tick_left()

    # set the y-spine
    ax.spines['bottom'].set_position('zero')

    # turn off the top spine/ticks
    ax.spines['top'].set_color('none')
    ax.xaxis.tick_bottom()

    # ax.set_aspect('equal')
    ax.set_box_aspect(1)

    p1, = ax.plot(x_1, y_1, "k.")
    p1, = ax.plot(x_2, y_2, "r-")

    ax.set_xlim(0, 2.2)
    ax.set_ylim(-5, 3)
    ax.xaxis.set_major_locator(MultipleLocator(0.2))
    ax.yaxis.set_major_locator(MultipleLocator(0.5))


    ax.grid(which='major', alpha=0.2)    

    fig.savefig(path, dpi=200)
    print(f'graph has been saved to {path}')      
