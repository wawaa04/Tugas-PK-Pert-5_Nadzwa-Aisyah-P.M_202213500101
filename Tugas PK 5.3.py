def hitung_ips():
    # Input jumlah mata kuliah
    jumlah_mk = int(input("Masukkan jumlah mata kuliah: "))
    
    total_sks = 0
    total_nilai = 0.0
    
    for i in range(jumlah_mk):
        print(f"\nMata Kuliah ke-{i + 1}:")
        sks = int(input("Masukkan jumlah SKS: "))
        nilai = input("Masukkan nilai (A/B/C/D): ").upper()
        
        # Menentukan nilai numerik berdasarkan input
        if nilai == 'A':
            nilai_numerik = 4.0
        elif nilai == 'B':
            nilai_numerik = 3.0
        elif nilai == 'C':
            nilai_numerik = 2.0
        elif nilai == 'D':
            nilai_numerik = 1.0
        else:
            print("Nilai tidak valid. Nilai dianggap 0.")
            nilai_numerik = 0.0
        
        # Menghitung total SKS dan total nilai
        total_sks += sks
        total_nilai += (nilai_numerik * sks)
    
    # Menghitung IPS
    if total_sks > 0:
        ips = total_nilai / total_sks
        print(f"\nIndeks Prestasi Semester (IPS): {ips:.2f}")
    else:
        print("Jumlah SKS tidak valid.")

# Menjalankan fungsi
hitung_ips()
