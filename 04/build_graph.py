import numpy as np
from data_input import f_1, f_2, left_x_limiter, right_x_limiter

"""
"""


def create_graph_nonlinear_system(left_xlim, right_xlim, func1, func2):
    """
    строит график заданных функции на заданном отрезке
    """

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

    ax.set_aspect('equal')

    step = (right_xlim - left_xlim) / 1000
    x_list1 = np.arange(left_xlim, right_xlim, step)
    y_list1 = np.fromiter((func1(x) for x in x_list1), dtype=np.float64)
    y_list2 = np.fromiter((func2(x) for x in x_list1), dtype=np.float64)
    

    p1, = ax.plot(x_list1, y_list1, "b-")
    p1, = ax.plot(x_list1, y_list2, "k-")

    ax.set_xlim(left_xlim, right_xlim)
    ax.set_ylim(left_xlim, right_xlim)
    

    ax.grid(which='major', alpha=0.3)    

    plt.show()
    path = 'txt/graph.png'
    fig.savefig(path, dpi=96)
    print(f'graph has been saved to {path}')


if __name__ == '__main__':

    # строим график
    create_graph_nonlinear_system(left_x_limiter, right_x_limiter, f_1, f_2)
