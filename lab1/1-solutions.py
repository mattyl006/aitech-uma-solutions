import numpy as np

x = np.array([[1.0, 2.0, 3.0],
           [1.0, 3.0, 6.0]])
X = np.matrix(x)
y = np.array([[5],
            [6]])

print (
    np.matmul (
        np.matmul (
            np.linalg.inv (
                np.matmul(x.T, x)
            ),
            x.T
        ),
        y
    )
)

print (
    ((X.T * X)**-1)*X.T*y
)
