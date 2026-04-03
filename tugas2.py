# Informasi Mahasiswa
print("Nama: Mushthofaa Bakri")
print("Nim:  251011700669")
print("-" * 30)

# Perhitungan Waktu Proyek
x = int(input("Masukkan jumlah hari proyek: "))
tahun = x // 365
sisa = x % 365
bulan = sisa // 30
hari = sisa % 30

# Output Hasil
print(f"Proyek dikerjakan selama ({tahun} tahun, {bulan} bulan, {hari} hari)")