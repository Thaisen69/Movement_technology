import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# === Filnavne ===
file_left = "sensor_dataL106.csv"
file_right = "sensor_dataR106.csv"

# === Indlæs data ===
df_left = pd.read_csv(file_left, header=None)
df_right = pd.read_csv(file_right, header=None)

# === Beregn samlet acceleration magnitude ===
def compute_acc_magnitude(df):
    return np.sqrt(df[0]**2 + df[1]**2 + df[2]**2)

acc_left = compute_acc_magnitude(df_left)
acc_right = compute_acc_magnitude(df_right)

# === Cross-correlation for at finde optimal forskydning ===
corr = np.correlate(acc_left - np.mean(acc_left), acc_right - np.mean(acc_right), mode='full')
lag = np.argmax(corr) - (len(acc_right) - 1)
print(f"Optimal lag (forskel i samples): {lag}")

# === Synkronisér data ===
if lag > 0:
    df_left_sync = df_left.iloc[lag:].reset_index(drop=True)
    df_right_sync = df_right
else:
    df_right_sync = df_right.iloc[-lag:].reset_index(drop=True)
    df_left_sync = df_left

# === Trim til samme længde ===
min_len = min(len(df_left_sync), len(df_right_sync))
df_left_sync = df_left_sync.iloc[:min_len]
df_right_sync = df_right_sync.iloc[:min_len]

# === Gem synkroniserede filer ===
df_left_sync.to_csv("sensor_dataL106_sync.csv", index=False, header=False)
df_right_sync.to_csv("sensor_dataR106_sync.csv", index=False, header=False)

# === Plot alle 6 akser ===
fig, axs = plt.subplots(3, 2, figsize=(14, 10))
titles = ['Acc X', 'Acc Y', 'Acc Z', 'Gyro X', 'Gyro Y', 'Gyro Z']

for i, ax in enumerate(axs.flatten()):
    ax.plot(df_left_sync[i], label='Left', alpha=0.7)
    ax.plot(df_right_sync[i], label='Right', alpha=0.7)
    ax.set_title(titles[i])
    ax.set_xlabel("Tid (samples)")
    ax.set_ylabel("Værdi")
    ax.grid(True)
    ax.legend()

plt.suptitle("Synkroniserede sensordata – alle 6 akser", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()
