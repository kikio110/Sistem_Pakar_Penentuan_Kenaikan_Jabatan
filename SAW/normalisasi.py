import numpy as np

def normalisasi(data):
    norm_data = np.array(data, dtype=float)
    for i in range(norm_data.shape[1]):  
        norm_data[:, i] /= np.max(norm_data[:, i])  
    return norm_data
