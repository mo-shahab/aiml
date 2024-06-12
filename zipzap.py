import numpy as np

# Data Preparation
x = np.array([[2, 9], [1, 5], [3, 6]], dtype=float)
y = np.array([[92], [86], [89]], dtype=float) / 100

# Neural Network Architecture
input_layer_neurons = 2
hidden_layer_neurons = 3
output_layer_neurons = 1

# Initialize Weights and Biases
wh = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
bh = np.random.uniform(size=(1, hidden_layer_neurons))
wout = np.random.uniform(size=(hidden_layer_neurons, output_layer_neurons))
bout = np.random.uniform(size=(1, output_layer_neurons))

# Training Parameters
epochs = 5
learning_rate = 0.1

# Training Loop
for epoch in range(epochs):
    # Forward Pass
    h_input = np.dot(x, wh) + bh
    h_layer_activation = 1 / (1 + np.exp(-h_input))
    output_input = np.dot(h_layer_activation, wout) + bout
    output = 1 / (1 + np.exp(-output_input))

    # Backward Pass
    EO = y - output
    d_output = EO * output * (1 - output)
    EH = d_output.dot(wout.T)
    d_hidden_layer = EH * h_layer_activation * (1 - h_layer_activation)

    # Update Weights and Biases
    wout += h_layer_activation.T.dot(d_output) * learning_rate
    wh += x.T.dot(d_hidden_layer) * learning_rate

    # Display Results
    print(f"--Epoch {epoch + 1}--")
    print("Input:\n", x)
    print("Actual Output:\n", y)
    print("Predicted Output:\n", output)

# Display Final Results
print("Input:\n", x)
print("Actual Output:\n", y)
print("Predicted Output:\n", output)

