def show_lab1():
    code = """
# Program 1: Basic Neuron Model with Different Activation Functions

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('default')  

# Basic Neuron

class Neuron:
    def __init__(self, input_size):
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand()

    def forward(self, x):
        return 1 / (1 + np.exp(-(np.dot(x, self.weights) + self.bias)))

input_size = 5
num_samples = 100
inputs = np.random.rand(num_samples, input_size)

neuron = Neuron(input_size)
outputs = neuron.forward(inputs)
print("Neuron outputs:\\n", outputs)

def sigmoid(x): return 1 / (1 + np.exp(-x))
def tanh(x): return np.tanh(x)
def relu(x): return np.maximum(0, x)
def softmax(x): return np.exp(x) / np.sum(np.exp(x))

# Plot 
def plot_activation(x, y, title):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y)
    plt.title(title)
    plt.grid(True)
    plt.show()

# Plots

x = np.linspace(-10, 10, 200)

plot_activation(x, sigmoid(x), "Sigmoid Activation Function")
plot_activation(x, tanh(x), "Hyperbolic Tangent Activation Function")
plot_activation(x, relu(x), "ReLU Activation Function")

t = np.linspace(-5, 5, 20)
plot_activation(t, softmax(t), "Softmax Activation Function")
"""
    print(code)
# This file contains all lab programs with show_labX() printers.


def show_lab2():
    code = """
# LAB 2 CODE HERE
"""
    print(code)


def show_lab3():
    code = """
# LAB 3 CODE HERE
"""
    print(code)


def show_lab4():
    code = """
# LAB 4 CODE HERE
"""
    print(code)


def show_lab5():
    code = """
# LAB 5 CODE HERE
"""
    print(code)


def show_lab6():
    code = """
# LAB 6 CODE HERE
"""
    print(code)


def show_lab7():
    code = """
# LAB 7 CODE HERE
"""
    print(code)


def show_lab8():
    code = """
# LAB 8 CODE HERE
"""
    print(code)


def show_lab9():
    code = """
# LAB 9 CODE HERE
"""
    print(code)


def show_lab10():
    code = """
# LAB 10 CODE HERE
"""
    print(code)
