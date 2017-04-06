import matplotlib.pyplot as plt



def visualize(x, y, orientation="horizontal", xlabel="input", ylabel="output", title="Bar Comparison"):
    if orientation is "horizontal":
        rects=plt.bar(range(len(y)), y,align='center')
        plt.xticks(range(len(x)), x, rotation="vertical")
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        return rects,plt
    else:
        rects=plt.barh(range(len(y)), y,align='center')
        plt.yticks(range(len(x)), x)
        plt.title(title)
        plt.xlabel(ylabel)
        plt.ylabel(xlabel)
        return rects,plt