import seaborn as sns
import matplotlib.pyplot as plt


def plot_scatter(data, x: list, y: str, hue=None, row=1, col=1, size=(20, 5)):
    fig, ax = plt.subplots(row, col, figsize=size)

    if row == 1 and col == 1:
        ax = [ax]

    for i in range(row):
        for j in range(col):
            index = i * col + j
            sns.scatterplot(data=data, x=x[index], y=y, hue=hue, ax=ax[i][j] if (row > 1 and col > 1) else ax[max(i, j)])

    plt.show()


def scatter(data, x: list, y: str, nrow=1, ncol=1, figsize=(20, 5)):
    fig, axs = plt.subplots(nrow, ncol, figsize=figsize)

    if nrow == 1 and ncol == 1:
        axs = [axs]
    else:
        axs = axs.flatten()

    #for i, feature in enumerate(x):
    for i, ax in enumerate(axs):
        data.plot.scatter(x=x[i], y=y, ax=ax)

    plt.show()


def histogram(data, columns: list, nrow=1, ncol=1, figsize=(15, 10), bins=50):
    # fig, axs = plt.subplots(nrow, ncol, figsize=figsize)

    # if nrow == 1 and ncol == 1:
    #     axs = [axs]
    # else:
    #     axs = axs.flatten()

    # for i, ax in enumerate(axs):
    #     ax.hist(data[columns[i]], bins=bins, edgecolor="black")
    #     ax.set_title(f"{columns[i]}")
    
    data.hist(bins=bins, figsize=figsize, edgecolor='black', grid=False)

    plt.tight_layout()
    plt.show()


def correlation_heatmap(data, size=(5, 3), annot_kws={"size": 10}, fmt=".2f", cmap="cool"):
    correlation = data.corr()

    plt.figure(figsize=size)
    sns.heatmap(correlation, annot=True, annot_kws=annot_kws, fmt=fmt, cbar=True, cmap=cmap)
    plt.show()
