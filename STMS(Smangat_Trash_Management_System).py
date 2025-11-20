from datetime import datetime

bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

siswa = ["KELAS X", "KELAS XI", "KELAS XII"]

data_kelas = ["A1", "A2", "B1", "B2", "C1", "C2", "D1", "D2", "E1", "E2", "F1", "F2"]

poin_pelanggaran = {
    "KELAS X": {k: 0 for k in data_kelas},
    "KELAS XI": {k: 0 for k in data_kelas},
    "KELAS XII": {k: 0 for k in data_kelas},
}

data_sampah = ["PLASTIK", "KERTAS", "ORGANIK"]

data_sampah_per_kelas = {
    "KELAS X": {k: {s: 0 for s in data_sampah} for k in data_kelas},
    "KELAS XI": {k: {s: 0 for s in data_sampah} for k in data_kelas},
    "KELAS XII": {k: {s: 0 for s in data_sampah} for k in data_kelas},
}

total_per_jenis = {"PLASTIK": 0, "KERTAS": 0, "ORGANIK": 0}
data_kelas_yang_melanggar = []

def tampilkan_menu_kelas():
    print("\n============================================================")
    print(" MASUKKAN ANGKA UNTUK MEMILIH KELAS")
    print("============================================================")
    for i, nama in enumerate(siswa, 1):
        print(f"{i}. {nama}")
    print("============================================================\n")

def tampilkan_data_kelas(x):
    tingkat = ["KELAS X", "KELAS XI", "KELAS XII"][x-1]
    print("\n============================================================")
    print(f" PILIH KELAS {tingkat}")
    print("============================================================")
    for i, kelas in enumerate(data_kelas, 1):
        print(f"{i}. {kelas}")
    print("============================================================\n")

def tampilkan_menu_sampah():
    print("\n============================================================")
    print(" PILIH JENIS SAMPAH")
    print("============================================================")
    for i, sampah in enumerate(data_sampah, 1):
        print(f"{i}. {sampah}")
    print("============================================================\n")

def input_data_sampah():
    while True:
        tampilkan_menu_kelas()
        kelas_apa = int(input())
        if 1 <= kelas_apa <= 3:
            break
        print("PILIHAN TIDAK TERSEDIA, MOHON MASUKKAN ANGKA 1-3!\n")
    while True:
        tampilkan_data_kelas(kelas_apa)
        jenis_kelas = int(input())
        if 1 <= jenis_kelas <= 12:
            break
        print("PILIHAN TIDAK TERSEDIA, MOHON MASUKKAN ANGKA 1-12!\n")
    while True:
        tampilkan_menu_sampah()
        jenis_sampah = int(input())
        if 1 <= jenis_sampah <= 3:
            break
        print("PILIHAN TIDAK TERSEDIA, MOHON MASUKKAN ANGKA 1-3!\n")
    berat = float(input("MASUKKAN BERAT SAMPAH (kg): "))
    kelas = siswa[kelas_apa - 1]
    nama_kelas = data_kelas[jenis_kelas - 1]
    sampah = data_sampah[jenis_sampah - 1]
    data_sampah_per_kelas[kelas][nama_kelas][sampah] += berat
    print("\nDATA BERHASIL DIINPUT!")
    print(f"Sampah {sampah} di {kelas} {nama_kelas}: {data_sampah_per_kelas[kelas][nama_kelas][sampah]} kg\n")

def input_poin_pelanggaran():
    while True:
        tampilkan_menu_kelas()
        kelas_apa = int(input())
        if 1 <= kelas_apa <= 3:
            break
        print("PILIHAN TIDAK TERSEDIA, MOHON MASUKKAN ANGKA 1-3!\n")
    while True:
        tampilkan_data_kelas(kelas_apa)
        jenis_kelas = int(input())
        if 1 <= jenis_kelas <= 12:
            break
        print("PILIHAN TIDAK TERSEDIA, MOHON MASUKKAN ANGKA 1-12!\n")
    kelas = siswa[kelas_apa - 1]
    nama_kelas = data_kelas[jenis_kelas - 1]
    poin_pelanggaran[kelas][nama_kelas] += 1
    print("\nPOIN BERHASIL DIINPUT!\n")

def statistik_keseluruhan():
    print("\n=================== TOTAL SAMPAH KESELURUHAN =================")
    for kelas in data_sampah_per_kelas:
        for nama_kelas in data_sampah_per_kelas[kelas]:
            for jenis, berat in data_sampah_per_kelas[kelas][nama_kelas].items():
                total_per_jenis[jenis] += berat
    for jenis, total in total_per_jenis.items():
        print(f"{jenis}: {total} kg")
    print("==============================================================\n")

def tampilkan_opsi_cek_statistik():
    print("\n====================== OPSI CEK STATISTIK ====================")
    print("1. TAMPILKAN STATISTIK KESELURUHAN")
    print("2. TAMPILKAN STATISTIK PER KELAS")
    print("==============================================================\n")

def cek_statistik_sampah():
    tampilkan_opsi_cek_statistik()
    while True:
        opsi = int(input())
        if opsi in [1, 2]:
            break
        print("PILIHAN TIDAK TERSEDIA, MOHON MASUKKAN ANGKA 1 ATAU 2!")
    if opsi == 1:
        statistik_keseluruhan()
        return
    while True:
        tampilkan_menu_kelas()
        kelas_apa = int(input())
        if 1 <= kelas_apa <= 3:
            break
        print("PILIHAN TIDAK TERSEDIA, MOHON MASUKKAN ANGKA 1-3!\n")
    while True:
        tampilkan_data_kelas(kelas_apa)
        jenis_kelas = int(input())
        if 1 <= jenis_kelas <= 12:
            break
        print("PILIHAN TIDAK TERSEDIA, MOHON MASUKKAN ANGKA 1-12!\n")
    kelas = siswa[kelas_apa - 1]
    nama = data_kelas[jenis_kelas - 1]
    print(f"\n========== STATISTIK SAMPAH {kelas} {nama} ==========")
    for jenis, berat in data_sampah_per_kelas[kelas][nama].items():
        print(f"{jenis}: {berat} kg")
    print("====================================================\n")

def cek_statistik_poin():
    while True:
        tampilkan_menu_kelas()
        k = int(input())
        if 1 <= k <= 3:
            break
        print("PILIHAN TIDAK TERSEDIA, MOHON MASUKKAN ANGKA 1-3!\n")
    while True:
        tampilkan_data_kelas(k)
        jenis_kelas = int(input())
        if 1 <= jenis_kelas <= 12:
            break
        print("PILIHAN TIDAK TERSEDIA, MOHON MASUKKAN ANGKA 1-12!\n")
    kelas = siswa[k - 1]
    nama = data_kelas[jenis_kelas - 1]
    poin = poin_pelanggaran[kelas][nama]
    print(f"\n============= POIN PELANGGARAN {kelas} {nama} =============")
    print(f"Poin: {poin}")
    print("============================================================\n")

def list_kelas_yang_melanggar():
    data_kelas_yang_melanggar.clear()
    for tingkat, kelas2 in poin_pelanggaran.items():
        for nama_kelas, poin in kelas2.items():
            if poin > 0:
                data_kelas_yang_melanggar.append((tingkat, nama_kelas))

def main():
    while True:
        print("============================================================")
        print("=              MASUKKAN ANGKA UNTUK MEMILIH MENU          =")
        print("============================================================")
        print("1. INPUT DATA SAMPAH")
        print("2. INPUT POIN PELANGGARAN")
        print("3. CEK STATISTIK SAMPAH")
        print("4. CEK POIN PELANGGARAN")
        print("5. SELESAI & CETAK REKAP")
        print("============================================================")
        s = int(input("MASUKKAN PILIHAN ANDA: "))
        if s == 1:
            input_data_sampah()
        elif s == 2:
            input_poin_pelanggaran()
        elif s == 3:
            cek_statistik_sampah()
        elif s == 4:
            cek_statistik_poin()
        elif s == 5:
            waktu = datetime.now()
            list_kelas_yang_melanggar()
            print("\n============================================================")
            print("=============== HASIL REKAP SAMPAH HARI INI ================")
            print(f"              Tanggal {waktu.day} Bulan {bulan[waktu.month-1]} Tahun {waktu.year}")
            print("============================================================\n")
            if not data_kelas_yang_melanggar:
                print("Tidak ada kelas yang memiliki poin pelanggaran.")
                print("Terima kasih kepada seluruh kelas yang sudah tertib.")
                print("Tetap pertahankan kebiasaan baik ini!")
                print("demi lingkungan sekolah yang nyaman\n")
            else:
                print("Kelas yang masih ditemukan sampah dan mendapatkan poin:")
                for i, (tingkat, nama) in enumerate(data_kelas_yang_melanggar, 1):
                    print(f"{i}. {tingkat} {nama}")
                print("\nTerima kasih kepada kelas yang sudah tertib membuang dan menyetorkan sampah dengan baik.")
                print("Bagi kelas yang belum setor, mohon diperhatikan untuk lebih disiplin kedepanya.")
                print("Mari bersama menjaga kebersihan sekolah demi lingkungan yang sehat dan nyaman.\n")
            print("TERIMAKASIH TELAH MENGGUNAKAN PROGRAM INI.")
            exit()
        else:
            print("PILIHAN TIDAK TERSEDIA, MOHON MASUKKAN ANGKA 1-5!\n")

main()
# THIS PROGRAM BUILD BY AREK_AS(AMERIKA SRENGAT)
# FIND ME IN TLX-> Krisnandaaa
