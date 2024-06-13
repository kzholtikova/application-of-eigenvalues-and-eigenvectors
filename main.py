import numpy as np


def find_eigenvalues_and_vectors(matrix):
    return np.linalg.eig(matrix)  # returns a named tuple: eigenvalues(…, M) array; eigenvectors(…, M, M) array


def validate_eigenvalues_and_vectors(matrix, eigenvalues, eigenvectors):  # eigenvectors[:,i] corresponds to eigenvalues[i]
    res = True
    for i, evalue in enumerate(eigenvalues.eigenvalues):
        evector = eigenvectors[:, i]
        if np.dot(matrix, evector) != evalue * evector:
            print(f"{evalue} and corresponding {evector} failed the validation.")
            res = False

    return res
