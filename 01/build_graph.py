import numpy as np
from read_and_calc import read_equation_coeffs, calculate_nonlinear, INPUT_FILE

"""
В этом модуле
Используя смесь табличного метода + графическиго метода, 
мы постараемся автоматизировать поиск промежутков изоляции корня 
для нелинейного уравнения ax^4 + .. + e = 0
"""

def find_range_for_graph_method(left_xlim, right_xlim, func):
    """
    Цель сократить промежуток на котором стоит рисовать график функции,
    обрезав промежуток слева-справа, на котором |y| значительно больше 0
    """
    step = (right_xlim - left_xlim) / 2000
    close_to_0_value = (right_xlim - left_xlim) / 100

    new_left_xlim = None
    new_right_xlim = None
    for x in np.arange(left_xlim, right_xlim, step):
        y = func(x)
        if abs(y) < close_to_0_value:
            if not new_left_xlim:
                new_left_xlim = x - step
                new_right_xlim = x + step
            else:
                new_right_xlim = x + step

    return new_left_xlim, new_right_xlim

def create_graph(left_xlim, right_xlim, func):
    """
    строит график заданной функции на заданном отрезке
    """

    import matplotlib.pyplot as plt
    from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

    # выбор массива для нанесения на график
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
  

    step = (right_xlim - left_xlim) / 1000
    x_list = np.arange(left_xlim, right_xlim, step)
    y_list = tuple(func(x) for x in x_list)

    p1, = ax.plot(x_list, y_list, "b-")

    ax.grid(which='major', alpha=0.3)    

    plt.show()
    path = 'txt/graph.png'
    fig.savefig(path, dpi=96)
    print(f'graph has been saved to {path}')



if __name__ == '__main__':
    # теперь f_ наша функция
    coeffs = read_equation_coeffs(INPUT_FILE)
    f_ = lambda x: calculate_nonlinear(coeffs, x)

    # уточняем отрезок на котором строим график
    left, right = find_range_for_graph_method(-1000, 1000, f_)
    # строим график
    create_graph(left, right, f_)
