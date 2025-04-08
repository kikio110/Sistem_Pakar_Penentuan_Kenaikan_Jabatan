import numpy as np
import kriteria
import saw

# Bobot Kriteria
bobot = [0.25, 0.5, 0.25]  # [Masa Kerja, Kinerja, Sikap]

# Input Data 
n = int(input("Masukkan jumlah karyawan: "))
karyawan = []
data = []

for i in range(n):
    nama = input(f"\nMasukkan nama karyawan {i+1}: ")
    masa_kerja = int(input("  - Masa Kerja (tahun): "))
    kinerja = float(input("  - Persentase Kinerja (%): "))
    sikap = float(input("  - Persentase Sikap (%): "))
    
    karyawan.append(nama)
    data.append([masa_kerja, kinerja, sikap])

# Konversi ke bobot kriteria
data_terkonversi = [
    [kriteria.Masa_Kerja(d[0]), kriteria.Penilaian_Kinerja(d[1]), kriteria.Penilaian_Sikap(d[2])]
    for d in data
]

# Hitung SAW
nilai_saw = saw.hitung_saw(data_terkonversi, bobot)

# Menentukan karyawan terbaik
best_index = np.argmax(nilai_saw)

# Menampilkan hasil
print("\n=== Hasil Perhitungan SAW ===")
for i, (alt, nilai) in enumerate(zip(karyawan, nilai_saw)):
    print(f"{alt}: {nilai:.3f}")

print(f"\nRekomendasi kenaikan jabatan karyawan adalah {karyawan[best_index]} dengan nilai {nilai_saw[best_index]:.3f}")
