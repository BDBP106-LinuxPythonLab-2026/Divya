import numpy as np


def one_hot_encode_dna(sequence):
    mapping = {
        'A': [1, 0, 0, 0],
        'G': [0, 1, 0, 0],
        'C': [0, 0, 1, 0],
        'T': [0, 0, 0, 1]
    }

    encoded_matrix = [mapping[base] for base in sequence.upper()]

    return np.array(encoded_matrix)


dna_sequence = "GATTACA"
encoded_dna = one_hot_encode_dna(dna_sequence)

print("Original Sequence: ", dna_sequence)
print("One-Hot Encoded NumPy Array Matrix:\n")
print(encoded_dna)

