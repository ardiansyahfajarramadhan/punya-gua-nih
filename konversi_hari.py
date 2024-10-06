# Fungsi untuk mengkonversi jumlah hari menjadi tahun, bulan, minggu, dan hari
def konversi_hari(total_hari):
    # Langkah 1: Hitung jumlah tahun
    tahun = total_hari // 365  # Hitung berapa tahun
    sisa_hari = total_hari % 365  # Hitung sisa hari setelah dihitung tahun

    # Langkah 2: Hitung jumlah bulan dari sisa hari
    bulan = sisa_hari // 30  # Hitung berapa bulan
    sisa_hari = sisa_hari % 30  # Hitung sisa hari setelah dihitung bulan

    # Langkah 3: Hitung jumlah minggu dari sisa hari
    minggu = sisa_hari // 7  # Hitung berapa minggu
    hari = sisa_hari % 7  # Hitung sisa hari yang tersisa

    # Langkah 4: Tampilkan hasil konversi
    print(f"{total_hari} hari setara dengan:")
    print(f"  {tahun} tahun")
    print(f"  {bulan} bulan")
    print(f"  {minggu} minggu")
    print(f"  {hari} hari")

# Bagian utama program (main program)
total_hari = int(input("Masukkan jumlah hari: "))
konversi_hari(total_hari)