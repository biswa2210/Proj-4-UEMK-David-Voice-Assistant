import torch.nn as tnn
# Brain of our Voice Assistant
class Brain(tnn.Module):

    def __init__(self,input_size,hidden_size,num_classes):
        super(Brain,self).__init__()
        self.l1 = tnn.Linear(input_size,hidden_size)
        self.l2 = tnn.Linear(hidden_size,hidden_size)
        self.l3 = tnn.Linear(hidden_size,num_classes)
        self.relu = tnn.ReLU()

    def forward(self,x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        return out