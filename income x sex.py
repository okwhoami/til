
# Using a Vertical Dumbbell Dot plot 

#Education level             Overall   Male      Female
#NO HIGH SCHOOL DIPLOMA      36,833    40,578    35,479
#HIGH SCHOOL DIPLOMA/GED      46,939    50,405    41,987
#SOME COLLEGE/ASSOCIATE       53,896    62,081    46,390
#BACHELOR DEGREE             110,135   130,142   97,210
#GRADUATE/PROFESSIONAL        153,014   174,355   135,456

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator

education = [
    "NO HIGH SCHOOL\nDIPLOMA",
    "HIGH SCHOOL\nDIPLOMA/GED",
    "SOME COLLEGE/\nASSOCIATE",
    "BACHELOR\nDEGREE",
    "GRADUATE/\nPROFESSIONAL",
]

overall = np.array([36833, 46939, 53896, 110135, 153014])
male = np.array([40578, 50405, 62081, 130142, 174355])
female = np.array([35479, 41987, 46390, 97210, 135456])

x = np.arange(len(education))
fig, ax = plt.subplots(figsize=(12, 7))

# Horizontal gridlines behind the plot.
ax.set_axisbelow(True)
ax.grid(axis="y", color="#D9D9D9", linewidth=1.2)

# Connect male and female values for each education level.
ax.vlines(
    x,
    ymin=np.minimum(male, female),
    ymax=np.maximum(male, female),
    color="#808080",
    linewidth=4,
    zorder=2,
)

# Circular markers.
ax.scatter(
    x, male, s=170, color="#00B5E2",
    edgecolors="none", label="Male", zorder=3,
)
ax.scatter(
    x, female, s=170, color="#000000",
    edgecolors="none", label="Female", zorder=3,
)
ax.scatter(
    x, overall, s=170, color="#BFBFBF",
    edgecolors="none", label="Overall", zorder=4,
)

for i, (m, f) in enumerate(zip(male, female)):
    ax.annotate(f"${m:,.0f}", (i, m), xytext=(0, 10), textcoords="offset points", ha="center", va="bottom", fontsize=9, color="#00B5E2")
    ax.annotate(f"${f:,.0f}", (i, f), xytext=(0, -10), textcoords="offset points", ha="center", va="top", fontsize=9, color="#222222")


# Labels and earnings scale.
ax.set_xticks(x)
ax.set_xticklabels(education, fontsize=11)
ax.set_xlim(-0.55, len(x) - 0.45)
ax.set_ylim(0, 200000)
ax.yaxis.set_major_locator(MultipleLocator(25000))
ax.yaxis.set_major_formatter(
    FuncFormatter(lambda value, _: f"${value:,.0f}")
)

ax.set_ylabel("Median earnings (USD)", fontsize=12)
ax.set_title(
    "MEDIAN EARNINGS by EDUCATION LEVEL & GENDER (2024)",
    loc="left",
    fontsize=19,
    color="#333333",
    pad=24,
)

# Minimal styling.
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="both", length=0, pad=10, colors="#444444")
ax.legend(
    loc="upper left",
    frameon=False,
    ncol=3,
    fontsize=11,
)

fig.tight_layout()
plt.show()
