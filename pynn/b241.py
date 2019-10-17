# 2.4.1 框架代码
# 2.4.2 初始化网络

# neural network class definition

class neuralNetwork:
    
    # initialise the neural network
    def __init__(self,
    inputnodes, hiddennodes, outputnodes,
    learningrate):
    
        # set number of nodes in each input, hidden, output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        
        # learning rate
        self.lr = learningrate
        pass
        
    # train the neural network
    def train():
        pass
        
    # query the neural network
    def query():
        pass

# number of input, hidden, output nodes
input_nodes = 3
hidden_nodes = 3
output_nodes = 3

# learning rate is 0.5
learning_rate = 0.5

# create instance of neural network
# or, "set n to an instance of class neuralNetwork, call it with params input_nodes, hidden_nodes, output_nodes, and learing_rate" in zedd's words.
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)