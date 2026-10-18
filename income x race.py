# edu-gem.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator

education = [
    "ALL LEVELS",
    "HIGH SCHOOL\nOR HIGHER",
    "BACHELOR'S\nOR HIGHER",
]

# Each entry: Male values, Female values, y-axis maximum, tick interval.
data = {
    "WHITE": (
        [147619, 143686, 112032],
        [117399, 114635, 93271],
        160000, 40000,
    ),
    "ASIAN": (
        [114387, 96156, 63730],
        [130960, 103787, 68993],
        160000, 40000,
    ),
    "LATINO": (
        [52045, 42112, 19904],
        [45730, 38793, 19339],
        70000, 20000,
    ),
    "BLACK": (
        [15950, 14697, 5998],
        [14805, 13532, 4956],
        20000, 5000,
    ),
    "NATIVE AMERICAN": (
        [1933, 1627, 494],
        [1350, 871, 310],
        4000, 1000,
    ),
}

male_color = "#00B5E2"
female_color = "#000000"
x = np.arange(len(education))

fig, axes = plt.subplots(2, 3, figsize=(17, 10))
axes = axes.ravel()

for ax, (race, (male, female, ymax, step)) in zip(axes, data.items()):
    male = np.array(male)
    female = np.array(female)

    ax.set_axisbelow(True)
    ax.grid(axis="y", color="#D9D9D9", linewidth=1)

    # Gray connectors between Male and Female earnings.
    ax.vlines(
        x,
        np.minimum(male, female),
        np.maximum(male, female),
        color="#808080",
        linewidth=3.5,
        zorder=2,
    )

    ax.scatter(
        x, male, s=110, color=male_color,
        edgecolors="none", label="Male", zorder=3,
    )
    ax.scatter(
        x, female, s=110, color=female_color,
        edgecolors="none", label="Female", zorder=3,
    )

    # Place the higher value's label above and the lower one below.
    for i, (m, f) in enumerate(zip(male, female)):
        for value, color, above in [
            (m, "#008BB0", m >= f),
            (f, "#222222", f > m),
        ]:
            ax.annotate(
                f"${value:,.0f}",
                (i, value),
                xytext=(0, 12 if above else -12),
                textcoords="offset points",
                ha="center",
                va="bottom" if above else "top",
                fontsize=9,
                color=color,
            )

    ax.set_title(race, loc="left", fontsize=17, color="#444444", pad=18)
    ax.set_xticks(x)
    ax.set_xticklabels(education, fontsize=9)
    ax.set_xlim(-0.55, 2.55)
    ax.set_ylim(0, ymax)

    ax.yaxis.set_major_locator(MultipleLocator(step))
    ax.yaxis.set_major_formatter(
        FuncFormatter(lambda value, _: f"${value:,.0f}")
    )
    ax.tick_params(axis="both", length=0, pad=9, colors="#444444")

    for spine in ax.spines.values():
        spine.set_visible(False)

# Hide the unused sixth panel.
axes[5].set_visible(False)

# One shared legend.
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(
    handles, labels,
    loc="upper right",
    bbox_to_anchor=(0.97, 0.98),
    ncol=2,
    frameon=False,
    fontsize=12,
)

fig.suptitle(
    "EARNINGS BY RACE AND EDUCATION",
    x=0.06, y=0.97,
    ha="left",
    fontsize=22,
    color="#444444",
)

fig.supylabel("Earnings ($)", fontsize=13, x=0.01)
fig.text(
    0.06, 0.925,
    "Each panel uses a separate y-axis scale.",
    fontsize=11,
    color="#666666",
)

fig.subplots_adjust(
    left=0.075, right=0.98,
    top=0.86, bottom=0.09,
    wspace=0.35, hspace=0.48,
)

plt.show()