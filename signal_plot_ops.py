import matplotlib.pyplot as plt


def load_signal_from_txt(path):
    values = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line: 
                values.append(float(line))
    return values


def signal_min(values):
    return min(values)


def signal_max(values):
    return max(values)


def signal_avg(values):
    return sum(values) / len(values)


def plot_signal(values):
    plt.figure()
    plt.plot(values)
    plt.title("Signal Plot")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    path = "ekg_signal.txt"

    signal = load_signal_from_txt(path)

    print("Min:", signal_min(signal))
    print("Max:", signal_max(signal))
    print("Avg:", signal_avg(signal))

    plot_signal(signal)
