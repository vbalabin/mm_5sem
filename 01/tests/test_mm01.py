# content of test_sysexit.py
import pytest
from read_and_calc import calculate_nonlinear
from read_and_calc import calculate_diff_1
from read_and_calc import calculate_diff_2


def test_calculate_nonlinear():
    func1 = lambda x: 1.*x**4 - 4.*x**3 + 3.* x**2 - 2.* x - 2.
    func2 = lambda x: 1.*x**4 - 5.*x**3 - 4.*x**2 - 3.*x + 12.
    coeffs1 = [1., -4., 3., -2., -2.]
    coeffs2 = [1., -5., -4., -3., 12.]

    assert pytest.approx(func1(0), .001) == calculate_nonlinear(coeffs1, 0)
    assert pytest.approx(func1(5), .001) == calculate_nonlinear(coeffs1, 5)
    assert pytest.approx(func1(2.2), .001) == calculate_nonlinear(coeffs1, 2.2)

    assert pytest.approx(func2(4), .001) == calculate_nonlinear(coeffs2, 4)
    assert pytest.approx(func2(3), .001) == calculate_nonlinear(coeffs2, 3)
    assert pytest.approx(func2(-3.1), .001) == calculate_nonlinear(coeffs2, -3.1)

def test_calculate_diff_1():
    # func1 = lambda x: 1.*x**4 - 4.*x**3 + 3.* x**2 - 2.* x - 2.
    func1 = lambda x: 4.*x**3 - 12.*x**2 + 6.* x - 2.
    #func2 = lambda x: 1.*x**4 - 5.*x**3 - 4.*x**2 - 3.*x + 12.
    func2 = lambda x: 4.*x**3 - 15.*x**2 - 8.*x - 3.
    coeffs1 = [1., -4., 3., -2., -2.]
    coeffs2 = [1., -5., -4., -3., 12.]

    assert pytest.approx(func1(0), .001) == calculate_diff_1(coeffs1, 0)
    assert pytest.approx(func1(5), .001) == calculate_diff_1(coeffs1, 5)
    assert pytest.approx(func1(2.2), .001) == calculate_diff_1(coeffs1, 2.2)

    assert pytest.approx(func2(4), .001) == calculate_diff_1(coeffs2, 4)
    assert pytest.approx(func2(3), .001) == calculate_diff_1(coeffs2, 3)
    assert pytest.approx(func2(-3.1), .001) == calculate_diff_1(coeffs2, -3.1)

def test_calculate_diff_2():
    # func1 = lambda x: 1.*x**4 - 4.*x**3 + 3.* x**2 - 2.* x - 2.
    # func1 = lambda x: 4.*x**3 - 12.*x**2 + 6.*x - 2.
    func1 = lambda x: 12.*x**2 - 24.*x + 6.
    # func2 = lambda x: 1.*x**4 - 5.*x**3 - 4.*x**2 - 3.*x + 12.
    # func2 = lambda x: 4.*x**3 - 15.*x**2 - 8.*x - 3.
    func2 = lambda x: 12.*x**2 - 30.*x - 8.
    coeffs1 = [1., -4., 3., -2., -2.]
    coeffs2 = [1., -5., -4., -3., 12.]

    assert pytest.approx(func1(0), .001) == calculate_diff_2(coeffs1, 0)
    assert pytest.approx(func1(5), .001) == calculate_diff_2(coeffs1, 5)
    assert pytest.approx(func1(2.2), .001) == calculate_diff_2(coeffs1, 2.2)

    assert pytest.approx(func2(4), .001) == calculate_diff_2(coeffs2, 4)
    assert pytest.approx(func2(3), .001) == calculate_diff_2(coeffs2, 3)
    assert pytest.approx(func2(-3.1), .001) == calculate_diff_2(coeffs2, -3.1)