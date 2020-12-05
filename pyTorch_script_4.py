# -*- coding: utf-8 -*-
'''
In the examples 1,2,3 we had to manually implement both the forward and backward passes of our neural network. 
Manually implementing the backward pass is not a big deal for a small two-layer network, but can quickly get very hairy for large complex networks.

Thankfully we can use automatic differentiation to automate the computation of backward passes in neural networks. The autograd package in PyTorch 
provides exactly this functionality. When using autograd, the forward pass of your network will define a computational graph; nodes i the graph will be
Tensors, and edges will be functions that produce output Tensors from input Tensors. Backpropagating through this graph then allows you to easily compute gradients  

Each Tensor represents a node in a computational graph. If x is a Tensor that has x.requires_grad=True then x.grad is another Tensor holding the gradient of x with
respect to some scalar value. Here we use PyTorch and autograd to implement our two-layer

Here we use PyTorch Tensors and autograd to implement our two-layer network; now we no longer need to manually implement the backward pass through the network:  
'''

import torch

dtype = torch.float
device = torch.device("cpu")
# device = torch.device("cuda:0") # uncomment this to run on gpu

# N is batch size; D_in is input dimension;
# H is hidden dimension; D_out is output dimension.
N, D_in, H, D_out = 64, 1000, 100, 10

# Create random Tensors to hold inputs and outputs.
# Setting requires_grad = False indicates that we do not need to compute gradients with respect to these Tensors during the backward pass.
x = torch.randn(N, D_in, device=device, dtype=dtype)
y = torch.randn(N, D_out, device=device, dtype=dtype)

# Create random Tensors for weights.
# setting requires_grad = True indicates that we want to compute gradients with respect to these Tensors during the backward pass.
w1 = torch.randn(D_in, H, device=device, dtype=dtype, requires_grad=True)
w2 = torch.randn(H, D_out, device=device, dtype=dtype, requires_grad=True)

learning_rate=1e-6
for t in range(500):
    # Forward pass: compute predicted y using operations on Tensors; these are exactly the same operations we used to compute the forward pass using
    # Tensors, but we do not need to keep references to intermediate values since we are not implementing the backward pass by hand.
    y_pred = x.mm(w1).clamp(min=0).mm(w2)
    
    # Compute and print loss using operations on Tensors. Now loss is a Tensor of shape (1,) loss.item() gets the scalar value held in the loss.
    loss = (y_pred - y).pow(2).sum()
    if t%100 == 99:
        print(t, loss.item())
        
    # Use autograd to compute the backward pass. This call will compute the gradient of loss with respect to all Tensors with requires_grad=True.  
    # After this call w1.grad and w2.grad will be Tensors holding the gradient of the loss with respect to w1 and w2 respectively.
    loss.backward()
    
    # Manually update weights using gradient descent. Wrap in torch.no_grad() because weights have requires_grad=True, but we don't need to track this
    # in autograd. 
    
    # An alternative way is to operate on weight.data and weight.grad.data. Recall that tensor.data gives a tensor that shares the storage with tensor, but doesn't 
    # track history. You can also use torch.optim.SGD to achieve this.
    with torch.no_grad():
        w1 -= learning_rate*w1.grad
        w2 -= learning_rate*w2.grad
        
        # Manually zero the gradients after updating weights
        w1.grad.zero_()
        w2.grad.zero_()

    
   
