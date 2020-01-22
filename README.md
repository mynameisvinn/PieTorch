# pietorch
a python implementation of pytorch. in a nutshell, it is autograd plus graphs.

## examples
```python
from Tensor import Tensor
from Op import Pow

X = Tensor(val=10, name="X")
Z = Pow(X, 2)
Z.val  # 100
Z.backward()  # compute gradients
X.grad  # gradient is 2x = 20
```
a more realistic example.
```python
from nn import Tensor, Add, Multiply, Pow, Relu, Module, Loss, Optimizer

class Net(Module):
    def __init__(self):
        super(Net, self).__init__() 
        self.Y = Tensor(val=5, name="Y")
        self.Z = Tensor(val=-4, name="Z")
        
    def forward(self, x):
        q = Add(x, self.Y)
        y = Relu(q)
        f = Multiply(y, self.Z)
        return f

model = Net()
output = model(-2)
output.val  # prints -12.0
```