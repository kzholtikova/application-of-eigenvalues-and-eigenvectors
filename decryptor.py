import numpy as np

'''
A = T * D * T^-1
encrypted = A * original = T * D * T^-1 * original
decrypted = A^-1 * encrypted = T^-1 * D^-1 * T * encrypted
where D - diagonalized matrix, A - standard basis transformation matrix, T - change of basis matrix of eigenvectors
'''


def encrypt_message(message, key_matrix):
    message_vector = np.array([ord(char) for char in message])
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))
    encrypted_vector = np.dot(diagonalized_key_matrix, message_vector)
    return encrypted_vector


message = "Meaningful Message."
print("Original message: ", message)
key_matrix = np.random.randint(0, 256, (len(message), len(message)))
encrypted_message = encrypt_message(message, key_matrix)
print("Encrypted message: ", encrypted_message)
