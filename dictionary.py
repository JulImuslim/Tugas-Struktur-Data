mahasiswa = {
    "Andi": {
        "NIM": "1010101",
        "Jurusan": "Teknik Informatika",
        "Alamat": "Jl. Sudirman No. 10",
        "Nilai": {
            "Matematika": 80,
            "Fisika": 70,
            "Kimia": 85
        }
    },
    "Budi": {
        "NIM": "1010102",
        "Jurusan": "Sistem Informasi",
        "Alamat": "Jl. Thamrin No. 20",
        "Nilai": {
            "Matematika": 75,
            "Fisika": 80,
            "Kimia": 90
        }
    },
    "Citra": {
        "NIM": "1010103",
        "Jurusan": "Teknik Elektro",
        "Alamat": "Jl. Gajah Mada No. 30",
        "Nilai": {
            "Matematika": 90,
            "Fisika": 85,
            "Kimia": 70
        }
    },
    "Dedi": {
        "NIM": "1010104",
        "Jurusan": "Teknik Mesin",
        "Alamat": "Jl. Pemuda No. 40",
        "Nilai": {
            "Matematika": 70,
            "Fisika": 90,
            "Kimia": 75
        }
    },
    "Eka": {
        "NIM": "1010105",
        "Jurusan": "Teknik Sipil",
        "Alamat": "Jl. Merdeka No. 50",
        "Nilai": {
            "Matematika": 85,
            "Fisika": 75,
            "Kimia": 80
        }
    }
}

# Menampilkan data mahasiswa
for nama, data in mahasiswa.items():
    print("Nama:", nama)
    print("NIM:", data["NIM"])
    print("Jurusan:", data["Jurusan"])
    print("Alamat:", data["Alamat"])
    nilai = data["Nilai"]
    total = nilai["Matematika"] + nilai["Fisika"] + nilai["Kimia"]
    rata_rata = total / 3
    print("Nilai Akumulasi:", total)
    print("Rata-rata Nilai:", rata_rata)
    print("======================")
