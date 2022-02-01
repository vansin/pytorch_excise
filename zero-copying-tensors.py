import numpy as np
import torch
import torch.nn.functional as F

np_array = np.array([[1.,1.],[1., 1.]])
torch_array = torch.from_numpy(np_array)
torch_array.add_(1.0)

print(np_array)

np_array = np_array + 1
np_array += 1

print(torch_array)

a = torch.tensor([1,2,3,4,5])
b = a.numpy()

print(b)