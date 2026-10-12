#KEGIATAN 2 (PASANG 1) -> ikhwan
def nilai_tertinggi_A(nilai):
    tertinggi = nilai[0]
    for n in nilai:
        if n > tertinggi:
            tertinggi = n
    return tertinggi

def nilai_tertinggi_B(nilai):
    return sorted(nilai)[-1]

data_mahasiswa = [{"nama": "Nurul Fitria", "nilai": 100},
                  {"nama": "Adyuta Nala Insani", "nilai": 98},
                  {"nama": "Ikhwan Nurhakim P.", "nilai": 85},
                  {"nama": "Angga Faisal Abi", "nilai": 88},
                  {"nama": "Raysah Naysila U.B", "nilai": 95},

print("Versi A:", nilai_tertinggi_A(nilai))
print("Versi B:", nilai_tertinggi_B(nilai))