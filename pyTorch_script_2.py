# -*- coding: utf-8 -*-
import numpy as np

'''
At its core PyTorch provides two main features:

- An n-dimensional Tensor, similar to numpy but can run on GPUs
- Automatic differentiation for building and training NNs

'''

# We will use a fully-connected ReLU network as our running example. The network will have a single hidden layer, and will be trained with 
# gradient descent to fit random data by minimizing the Euclidean distance between the network output and the true output.

# Before introducing PyTorch, we will first implement the network using numpy.

''' 
Numpy provides an n-dimensional array object, and many functions for manipulating these arrays. Numpy is a generic framework for scientific 
computing; it does not know anything about computation graphs, or deep learning, or gradients. However we can easily use numpy to fit a 
two-layer network to random data by manually implementing the forward and backward passes through the network using numpy operations:
'''

# N is batch size; D_in is input dimension
# H is hidden dimension; D_out is output dimensiond 
N, D_in, H, D_out = 64, 1000, 100, 10

# Create random input and output data
x = np.random.randn(N, D_in)
y = np.random.randn(N, D_out)

# Randomly initialize weights
w1 = np.random.randn(D_in, H)
w2 = np.random.randn(H, D_out)

learning_rate = 1e-6
for t in range(500):
    # Forward pass: compute predicted y
    h = x.dot(w1)  # Dot product of two arrays
    h_relu = np.maximum(h, 0)
    y_pred = h_relu.dot(w2)
    
    # Compute and print loss
    loss = np.square(y_pred - y).sum()
    print(t, loss)
    # print(type(loss), loss.shape)
    
    # Backprop to compute gradients of w1 and w2 with respect to loss
    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.T.dot(grad_y_pred) # compute grad_w2
    grad_h_relu = grad_y_pred.dot(w2.T)
    grad_h = grad_h_relu.copy()
    grad_h[h<0] = 0
    grad_w1 = x.T.dot(grad_h)  # compute grad_w1

    # Update weights
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2
    
    print("w1 is {} \n\n and w2 is {}".format(w1, w2))
    exit()
    
    