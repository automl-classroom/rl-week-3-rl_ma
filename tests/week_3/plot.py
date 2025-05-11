import matplotlib.pyplot as plt
import pandas as pd

# CSV-Datei einlesen
df = pd.read_csv("./tmp/sarsa_rs/runhistory.csv")

# Punkte plotten
plt.figure(figsize=(10, 6))  # Größe des Plots anpassen
plt.scatter(df.iloc[:, 3], df.iloc[:, 2], marker="o", label="Alle Punkte")
plt.xlabel("gamma")
plt.ylabel("Performance")
plt.title("Plot aus CSV")
plt.grid(True)

# Maximalen Punkt finden und markieren
max_index = df.iloc[:, 2].idxmax()
corresponding_value = df.iloc[max_index, 3]
plt.scatter(
    corresponding_value,
    df.iloc[max_index, 2],
    color="red",
    label="Maximaler Punkt",
    zorder=5,
)
plt.annotate(
    f"Max: ({corresponding_value:.2f}, {df.iloc[max_index, 2]:.2f})",
    xy=(corresponding_value, df.iloc[max_index, 2]),
    xytext=(corresponding_value + 0.1, df.iloc[max_index, 2] + 0.1),
    arrowprops=dict(facecolor="black", arrowstyle="->"),
    fontsize=10,
    color="black",
)

# Legende hinzufügen
plt.legend()


# varepsilon_1:    "alpha=0.5, gamma=0.6, epsilon=var, n_trials: 1000, num_episodes: 100  ",
# alpha variation --> epsilon= 0.35 gamma=0.6 alpha variation --> ??? 11 episodes --> alles 0 ab 12 alles hoch
# --> alpha nicht so relevant solange nicht zu groß

# Plot anzeigen
plt.show()

print(f"Maximaler Wert in Spalte 2: {df.iloc[max_index, 2]}")
print(f"Zugehöriger Wert in Spalte 3: {corresponding_value}")
