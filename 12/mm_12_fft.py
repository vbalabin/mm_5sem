import os
from manage_data import print_to_txt, strip_ext
import numpy as np

## Дано:
a = -np.pi
b = np.pi
n = 512
def f_(x):
    return np.arctan(1 / (1 + 10*x))

OUTPUT_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.txt'
OUTPUT_GRAPH_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.png'
TO_FILE = True


def tmas(count, length):
    mas = tuple(dict() for _ in range(count))
    for d in mas:
        for i in range(1, length):
            d[i] = 0
    return mas


def fast_furier(xr, xi, yr, yi, n, ind):
    k = n
    log2 = 0
    while True:
        k = k // 2
        log2 = log2 + 1
        if k < 2: break

    mm = 1
    for m in range(1, log2 + 1): 
      m2 = mm * 2
      k1 = int(np.trunc(np.power(2, (log2 - m)) - 1))
      l1 = mm - 1

      for k in range(1, k1 + 1 + 1):
        for l in range(1, l1 + 1 + 1): 
          j = m2 * (k - 1) + l
          i = mm * (k - 1) + l
          w = np.pi * (l - 1) / mm
          si = ind * np.sin(w)
          co = np.cos(w)
          ni = np.trunc(np.power(2, (log2 - 1)) + i)
          jm = np.trunc(j + np.power(2, (m - 1)))
          xa = xr[ni] * co + xi[ni] * si
          xb = xi[ni] * co - xr[ni] * si
          yr[j] = xr[i] + xa
          yi[j] = xi[i] + xb
          yr[jm] = xr[i] - xa
          yi[jm] = xi[i] - xb

      for it in range(1, n): 
        xr[it] = yr[it]
        xi[it] = yi[it]

      mm = m2

    if ind < 0:
      return

    for i in range(1, n):
      xr[i] = xr[i] / n
      xi[i] = xi[i] / n


def inv_fast_furier(a, b, ar, ai, xr, xi, n, eps, ip):
    h = (b - a) / (n - 1)

    fast_furier(ar, ai, xr, xi, n, ip)
    for i in range(1, n):

        k = i - 1
        w = k * 2 * np.pi / (b - a)
        c = np.cos(w * a)
        s = np.sin(w * a)
        w = w * h * (b - a)
        if w < eps:
            w4 = h - 2 * np.pi * np.pi * k * k * np.power(h, 3) / np.power((b - a), 2)
            w5 = 2 * np.pi * k * h * h / (b - a)
            a1 = w4 * ar[i] + ip * w5 * ai[i]
            b1 = w4 * ai[i] - ip * w5 * ar[i]
        else:
            if k == 0: 
                w1 = 0
                w3 = 0
            else:
                w1 = np.sin(2 * np.pi * k / n) * (b - a) / (2 * np.pi * k)
                w2 = 2 * np.power(np.sin(np.pi * k / n), 2)
                w3 = w2 * (b - a) / (2 * np.pi * k)

            w2 = 2 * np.power(np.sin(np.pi * k / n), 2)
            a1 = w1 * ar[i] + ip * w3 * ai[i]
            b1 = w1 * ai[i] - ip * w3 * ar[i]

        ar[i] = a1 * c + b1 * s * ip
        ai[i] = b1 * c - a1 * s * ip

        if ip > 0:
            ar[i] = ar[i] * n * n
            ai[i] = ai[i] * n * n
        ar[i] = ar[i] / n
        ai[i] = ai[i] / n


@print_to_txt(TO_FILE, OUTPUT_PATH)
def main():
    eps = 0.1e-6
    global n
    n = n + 1
    h = (b - a) / (n - 1)
    omg = 0

    xr, xi, ar, ai = tmas(4, n)

    for i in range(1, n):
        x = (i - 1) * h
        ar[i] = f_(x)
        ai[i] = 0

    inv_fast_furier(a, b, ar, ai, xr, xi, n, eps, 1)
    print(f"{'N':^3s} | {'omega':^5s} | {' Re':^14s} | {' Im':^14s}")
    for i in range(1, n):
        omg = (i - 1) * 2 * np.pi / (b - a)
        if i < 12 or n - i < 12:
            print(f"{i:3d} | {omg:-5.1f} | {ar[i]:-14.5e} | {ai[i]:-14.5e}")
        if i == 12:
            print('-' * 45)


    print()
    print("Общий результат вычислений интеграла f(x)e^(iwx):")
    print(f"Re = {sum(ar.values()):.7f}")
    print(f"Im = {sum(ai.values()):.7f}j")


if __name__ == '__main__':
    main()
