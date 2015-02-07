""" Given the set of points generated by f(x) = e^(2 * x) + 3 * x with some
noise, use Levenberg-Marquardt algorithm to find the model to fit
all the points.
"""

import numpy as np
import scipy.optimize as scipy_opt

def exp_func(x_data, a, b):
    """ Computes the function e^(a * x) + b * x
    Args:
        x_data : A Numpy array of input data
        a : Real-valued argument of the function
        b : Real-valued argument of the function

    Returns:
        A Numpy array of values of the function e^(a * x) + b * x evaluated
        at each x in xData
    """
    return np.exp(a * x_data) + b * x_data

def main():
    """ Main function to set up data points and calls Scipy curve fitting
    routine (whose underlying algorithm is Levenberg-Marquardt)
    """
    x_data = np.array([
        2.2, 2.0, 1.9, 1.8, 1.28, 1.33, 1.12, 1.1, 0.8, 0.5, 1.7, 1.5, -14.8,
        -14.0, -12.0, -1.5, 1.0, 0.0, -1.0, -2.0, -5.0, -3.0, -4.0, -10.0,
        -15.0, -6.0, -4.50
    ])
    y_data = np.array([
        88.0, 60.6, 50.4, 42.0, 16.7758, 18.286, 12.75, 12.33, 7.35, 4.22,
        35.0, 14.62, -44.4, -42.0, -35.9, -4.4502, 10.4, 0.99, -2.87, -5.98,
        -15.0, -8.9, -11.9996, -30.0, -43.0, -17.99999, -13.499877
    ])
    guess_abs = [[0.0, 4.0], [5.5, -10.5], [-0.1, 100.0], [8.9, 5.0]]

    for guess_ab in guess_abs:
        ab, covariance = scipy_opt.curve_fit(exp_func, x_data, y_data, guess_ab)
        print 'Intial guess: %s' % str(guess_ab)
        print 'LM results: %s' % str(ab)

if __name__ == "__main__":
    main()
