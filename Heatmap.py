# viz_table6.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------- 1) Load CSV ----------
# Replace with your filename
csv_path = "BT-large-2c-dataset_results_finetune_ALL_Models.csv"
df_raw = pd.read_csv(csv_path)

# Expected structure like Table 6:
# columns: ["Deep Feature from the Pre-Trained ViT Model", "XGBoost", "MLP", ..., "SVM_RBF", "Average"]
#  - If your column names differ slightly, adjust the names below.

# Identify the model column and metric columns
model_col = [c for c in df_raw.columns if "Deep" in c or "Model" in c][0]
# Drop any total/summary rows and columns if present
df = df_raw.copy()
df = df[~df[model_col].str.contains("Average", case=False, na=False)]
metric_cols = [c for c in df.columns if c != model_col and "Average" not in c]

# Convert metrics to numeric (in case CSV has strings)
for c in metric_cols:
    df[c] = pd.to_numeric(df[c], errors="coerce")

# Optional: sort rows by mean across classifiers so trends are clearer
df["__row_mean__"] = df[metric_cols].mean(axis=1)
df = df.sort_values("__row_mean__", ascending=False).drop(columns="__row_mean__")

# Set model names as index for heatmap
df_hm = df.set_index(model_col)[metric_cols]

# ---------- 2) Heatmap (Matplotlib-only) ----------
fig, ax = plt.subplots(figsize=(12, 7))
im = ax.imshow(df_hm.values, aspect="auto")  # default colormap

# ticks & labels
ax.set_xticks(np.arange(df_hm.shape[1]))
ax.set_xticklabels(df_hm.columns, rotation=45, ha="right")
ax.set_yticks(np.arange(df_hm.shape[0]))
ax.set_yticklabels(df_hm.index)

# annotate each cell (values ×100 if they’re accuracies in 0–1)
for i in range(df_hm.shape[0]):
    for j in range(df_hm.shape[1]):
        val = df_hm.iloc[i, j]
        if pd.notnull(val):
            ax.text(j, i, f"{val:.3f}", ha="center", va="center", fontsize=8)

ax.set_title("Accuracy Heatmap — ViT Deep Features × ML Classifiers")
cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label("Accuracy", rotation=270, labelpad=12)

plt.tight_layout()
plt.savefig("table6_heatmap.png", dpi=300)
# plt.show()

# ---------- 3) Color-highlighted HTML table ----------
# Bold the top-3 per column and apply a gradient for readability
def topk_style(col, k=3):
    # handle NaNs safely
    ranks = col.rank(ascending=False, method="min")
    styles = []
    for r, v in zip(ranks, col):
        if pd.isna(v):
            styles.append("")
        elif r <= k:
            styles.append("font-weight: bold; border: 1px solid #444;")
        else:
            styles.append("")
    return styles

styled = (df_hm.style
          .format("{:.3f}")
          .background_gradient(axis=0)                    # smooth per-column gradient
          .apply(topk_style, axis=0, k=3)                 # bold top-3 per classifier
          .set_caption("Accuracies of ViT features with ML classifiers (top-3 per column highlighted)")
          )

styled.to_html("table6_highlighted.html")  # open this in a browser
print("Saved: table6_heatmap.png and table6_highlighted.html")
