import matplotlib.pyplot as plt

def plot_graph(y_values1, y_values2):
    x_values = range(len(y_values1))  # Assume x values are indices of y values

    plt.plot(x_values, y_values1, label='Y Values 1')
    plt.plot(x_values, y_values2, label='Y Values 2')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Graph Title')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
y_values1 = [10.2253, 9.3312, 7.2847, 7.0951, 7.0726, 6.9745, 6.7792, 6.8274, 7.1154, 8.3522, 7.0162, 7.4534, 8.9241, 7.0105, 6.7694]
y_values2 = [2.3451, 4.5349, 6.2130, 7.9561, 10.9196, 9.8997, 8.6058, 7.1343, 8.9157, 5.8251, 10.9674, 9.4068, 8.3033, 8.9920, 8.5269]
plot_graph(y_values1, y_values2)

