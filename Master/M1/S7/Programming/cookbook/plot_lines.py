"""Plot one or more series against a shared x-axis, and save the figure.

Run it to see it work:

    python plot_lines.py          # writes plot_lines_demo.png
"""

import matplotlib.pyplot as plt

# ---------------------------------------------------------------- THE PATTERN
#  Always go through fig, ax = plt.subplots(). The plt.plot() shortcut draws
#  into a hidden "current figure", which silently puts two charts on top of
#  each other the moment you plot twice in one script.


def plot_lines(
    x_values: list,
    series: dict[str, list[float]],
    title: str = "",
    x_label: str = "",
    y_label: str = "",
    save_to: str | None = None,
) -> None:
    """Draw every series in `series` against the same x-axis.

    Args:
        x_values: Shared x-axis, e.g. dates as strings.
        series: One entry per line: {"Maximum": [...], "Minimum": [...]}.
            The key becomes the legend label.
        title, x_label, y_label: Text. Empty strings are simply not drawn.
        save_to: A filename to write to. If None, opens a window instead.

    Example:
        >>> plot_lines(["Mon", "Tue"], {"High": [8.1, 6.4]}, save_to="a.png")
    """
    fig, ax = plt.subplots(figsize=(8, 4))

    for label, values in series.items():
        ax.plot(x_values, values, marker="o", label=label)

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.grid(True, alpha=0.3)
    if len(series) > 1:
        ax.legend()  # a legend for one line just repeats the title

    #  Date strings overlap as soon as there are more than a handful.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
    fig.tight_layout()  # stops the rotated labels being cut off

    if save_to:
        fig.savefig(save_to, dpi=150)
        plt.close(fig)  # frees the figure; forgetting this leaks in a loop
    else:
        plt.show()


# -------------------------------------------------------------- END OF PATTERN


if __name__ == "__main__":
    days = ["2025-12-01", "2025-12-02", "2025-12-03", "2025-12-04", "2025-12-05"]
    plot_lines(
        days,
        {"Maximum": [8.1, 6.4, 9.9, 11.2, 7.3],
         "Minimum": [1.2, -0.4, 3.1, 4.8, 0.9]},
        title="Grenoble, first days of December",
        x_label="Date",
        y_label="Temperature (°C)",
        save_to="plot_lines_demo.png",
    )
    print("wrote plot_lines_demo.png")
