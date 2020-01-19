import unittest
from nn import Tensor, Add, Multiply, Module, Relu, Pow

class Test_PieTorch(unittest.TestCase):

    def setUp(self):
        self.X = Tensor(val=-2, name="X")
        self.Y = Tensor(val=5, name="Y")
        self.Q = Add(self.X, self.Y)
        self.Z = Tensor(val=-4, name="Z")
        self.F = Multiply(self.Q, self.Z)

        

    def test_forward_pass(self):
        """
        to be revised since F.val is not dynamically computed at runtime
        """
        self.assertEqual(self.F.val, -12.0)

    def test_accumulated_grad(self):
        self.F.backward()  # call backward on root
        self.assertEqual(self.X.accumulated_grad, -4.0)
        self.assertEqual(self.Y.accumulated_grad, -4.0)
        self.assertEqual(self.Z.accumulated_grad, 3.0)

    def test_module(self):
        class Net(Module):
            def __init__(self):
                super(Net, self).__init__() 
                
            def forward(self, x):
                x = Pow(x, 2)
                return Relu(x)

        model = Net()
        self.assertEqual(model(3).val, 9.0)

if __name__ == "__main__":
    unittest.main()