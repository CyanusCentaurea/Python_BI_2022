import numpy


def array_building():
    """
    Creates three arrays:
    [0. 0. 0.]

    [[1 2 3]
    [4 5 6]
    [7 8 9]]

    [1.  1.5 2.  2.5 3.  3.5]
    using different functions and methods of NumPy.
    """
    zeros_way1 = numpy.array([0., 0., 0.])
    zeros_way2 = numpy.zeros(3)
    zeros_way3 = numpy.linspace(0, 0, num=3)
    zeros_way4 = numpy.full(3, 0.)
    zeros_way5 = numpy.full(3, 0, numpy.float64)
    zeros_way6 = numpy.array([0, 0, 0]).astype(float)
    zeros_way7 = zeros_way1.copy()
    small_matrix_way1 = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    small_matrix_way2 = numpy.arange(1, 10).reshape(3, 3)
    small_matrix_way3 = small_matrix_way1.copy()
    small_matrix_way4 = numpy.full((3, 3), numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    by_steps_way1 = numpy.array([1., 1.5, 2., 2.5, 3., 3.5])
    by_steps_way2 = numpy.arange(1, 4, 0.5)
    by_steps_way3 = by_steps_way1.copy()


def matrix_multiplication(matrix1, matrix2):
    """
    Returns the result of multiplying two matrices. Not adapted for the input of matrices that cannot be multiplied.
    """
    return numpy.dot(matrix1, matrix2)


def multiplication_check(matrices):
    """
    Accepts a list of matrices.
    Returns True if they can be multiplied by each other in the order in which they are given,
    False if they cannot be multiplied.
    """
    return all(matrix1.shape[1] == matrix2.shape[0] for matrix1, matrix2 in zip(matrices[:-1], matrices[1:]))


def multiply_matrices(matrices):
    """
    Accepts a list of matrices.
    Returns the result of multiplication if they can be multiplied by each other in the order in which they are given,
    None if they cannot be multiplied.
    """
    res = None
    for matrix1, matrix2 in zip(matrices[:-1], matrices[1:]):
        try:
            res = numpy.dot(matrix1, matrix2)
        except ValueError:
            return res
    return res


def compute_multidimensional_distance(point1, point2):
    """
    Accepts 2 1d-arrays with any number of values (but equal) and returns the distance between them.
    """
    # return numpy.sqrt(numpy.sum(numpy.square(point1 - point2)))
    return numpy.linalg.norm(point1 - point2)


def compute_2d_distance(point1, point2):
    """
    Accepts two 1d arrays with any number of values (but equal) and returns the distance between them.
    """
    return compute_multidimensional_distance(point1, point2)


def compute_pair_distances(arr):
    """
    Accepts one 2d array, where each row is an observation, and each column is a feature.
    Returns a matrix of pairwise distances.
    """
    outer_product = numpy.add.outer(numpy.sum(arr ** 2, axis=1), numpy.sum(arr ** 2, axis=1))
    mult_matrix = matrix_multiplication(arr, numpy.transpose(arr))
    return numpy.sqrt(outer_product - 2 * mult_matrix)

