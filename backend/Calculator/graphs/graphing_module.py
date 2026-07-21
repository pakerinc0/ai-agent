import matplotlib.pyplot as plt
from graph_data import data

def plot_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('График функции')
    plt.grid(True)

def main():
    x = [row['x'] for row in data]
    y = [row['y'] for row in data]

    plot_graph(x, y)
    plt.show()

if __name__ == "__main__":
    main()
