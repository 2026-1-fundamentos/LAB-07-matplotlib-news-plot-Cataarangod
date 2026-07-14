"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv("files/input/news.csv", index_col=0)

    colors = {
        "Television": "dimgrey",
        "Newspaper": "grey",
        "Internet": "tab:blue",
        "Radio": "lightgrey",
    }

    zorder = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,
        "Radio": 1,
    }

    linewidth = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 4,
        "Radio": 1,
    }

    plt.figure()

    for col in df.columns:
        plt.plot(
            df[col],
            label=col,
            color=colors[col],
            zorder=zorder[col],
            linewidth=linewidth[col],
        )

    plt.title("People get news", fontsize=16)

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    first_year = df.index[0]
    for col in df.columns:
        plt.scatter(first_year, df[col].iloc[0], color=colors[col], zorder=zorder[col])

    last_year = df.index[-1]
    for col in df.columns:
        plt.scatter(last_year, df[col].iloc[-1], color=colors[col], zorder=zorder[col])

    for col in df.columns:
        plt.text(
            first_year - 0.2,
            df[col].iloc[0],
            f"{col} {df[col].iloc[0]}%",
            ha="right",
            va="center",
            color=colors[col],
        )

    for col in df.columns:
        plt.text(
            last_year + 0.2,
            df[col].iloc[-1],
            f"{df[col].iloc[-1]}%",
            ha="left",
            va="center",
            color=colors[col],
        )

    plt.xticks(ticks=df.index, labels=[str(y) for y in df.index], ha="center")

    os.makedirs("files/plots", exist_ok=True)
    plt.tight_layout()
    plt.savefig("files/plots/news.png")
