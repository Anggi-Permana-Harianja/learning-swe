import numpy as np
import pandas as pd


# function decorator to ensure numpy input
# and found off output to 1 decimal places
def ensure_numpy(function):
    def decorated_function(data):
        array = np.asarray(data)
        output = function(array)
        return np.around(output, 1)

    return decorated_function


# function below is the example of decorators
# we can send numpy_sum as parameters to ensure_numpy
# equals to ensure_numpy(numpy_sum(array)) and ensure_numpy(numpy_mean(array))
@ensure_numpy
def numpy_sum(array):
    return array.sum()


@ensure_numpy
def numpy_mean(array):
    return np.mean(array)


x = np.random.randn(10, 3)
y = pd.DataFrame(x, columns=["A", "B", "C"])

# calling decorated functions
# note: we call the decorated numpy_sum and numpy_mean instead the ensure_numpy
print("numpy_sum(x):", numpy_sum(x))
print("numpy_sum(y):", numpy_sum(y))
print("numpy_mean(x):", numpy_mean(x))
print("numpy_mean(y):", numpy_mean(y))
