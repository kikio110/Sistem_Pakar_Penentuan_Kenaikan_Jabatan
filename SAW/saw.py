import normalisasi

def hitung_saw(data, bobot):
    norm_data = normalisasi.normalisasi(data)

    nilai_preferensi = []
    for i in range(len(norm_data)):
        total = 0
        for j in range(len(bobot)):
            total += norm_data[i][j] * bobot[j] 
        nilai_preferensi.append(total)

    return nilai_preferensi
