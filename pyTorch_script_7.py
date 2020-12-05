'''
PyTorch:optim
Up to this point we have updated the weights of our models by manually mutating the Tensors holding learnable parameters (with torch.no_grad() or .data) 
to avoid tracking history in autograd). This is not a huge burden for simple optimization algorithms like stochastic gradient descent, but in practice 
'''

# -*- coding: utf-8 -*-
import torch

# N is batch size; D_in is input dimension;
# H is hidden layers; D_out is output dimension. 
N, D_in, H, D_out = 64, 1000, 100, 10

# Create random Tensors to hold inputs and outputs
x = torch.randn(N, D_in)
y = torch.randn(N, D_out)

# Use the nn package to define our model and loss function.
model = torch.nn.Sequential (torch.nn.Linear(D_in, H), torch.nn.ReLU(), torch.nn.Linear(H, D_out), )
loss_fn = torch.nn.MSELoss(reduction='sum')

# Use the optim package to define an Optimizer that will update the weights of the model for us. Here we will use Adam; The optim package contains many other
# optimization algorithms. The 1st argument to the Adam constructor tells the optimizer which Tensors it should update.
learning_rate = 1e-4
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
for t in range(500):
    # Forward pass: compute predicted y by passing x to the model.
    y_pred = model(x)
    
    # Compute and print loss
    loss = loss_fn(y_pred, y)
    if t%100 == 99:
        print(t, loss.item())
        
    # Before the backward pass, use the optimizer object to zero all of the gradients for the variables it will update (which are the learnable 
    # weights of the model). This is because by default, gradients are accumulated in buffers (i.e., not overwritten) whenever .backward() is called. 
    # Checkout docs of torch.autograd.backward for more details. 
    optimizer.zero_grad()
    
    # Backward pass: compute gradient of the loss with respect to model parameters
    loss.backward()
    
    # Calling the step function on an Optimizer makes an update to its parameters.
    optimizer.step()