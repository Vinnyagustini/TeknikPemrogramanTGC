import pandas as pd

# Membaca file CSV
data = pd.read_csv('survey_gravitasi.csv', sep=',')

print("Data Awal:")
print(data.head())

print("\nInfo Data:")
print(data.info())

print("\nStatistik:")
print(data.describe())

# --- Analisis Anomali ---
anomali_max = data['Anomali_Gravitasi_mGal'].max()
anomali_min = data['Anomali_Gravitasi_mGal'].min()

lokasi_max = data[data['Anomali_Gravitasi_mGal'] == anomali_max][['X', 'Y']]
lokasi_min = data[data['Anomali_Gravitasi_mGal'] == anomali_min][['X', 'Y']]

print("\n=== Analisis Anomali ===")
print(f"Anomali Positif Tertinggi : {anomali_max:.2f} mGal")
print(lokasi_max)
print(f"\nAnomali Negatif Terendah  : {anomali_min:.2f} mGal")
print(lokasi_min)

# --- Visualisasi Data Anomali ---
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
scatter = plt.scatter(
    data['X'], data['Y'], 
    c=data['Anomali_Gravitasi_mGal'], 
    cmap='coolwarm', 
    s=80, 
    edgecolors='k'
)

plt.colorbar(scatter, label='Anomali Gravitasi (mGal)')
plt.xlabel('Koordinat Timur (m)')
plt.ylabel('Koordinat Utara (m)')
plt.title('Peta Sebaran Anomali Gravitasi')
plt.grid(True)
plt.show()