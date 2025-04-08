def Masa_Kerja(masa_kerja):
    if masa_kerja == 2:
        return 0.2
    elif masa_kerja == 3:
        return 0.4
    elif masa_kerja == 4:
        return 0.6
    elif masa_kerja == 5: 
        return 0.8
    elif masa_kerja >= 5: 
        return 1.0
    else:
        return 0.0
    
def Penilaian_Kinerja(persentase):
    if persentase < 60:
        return 0.2 
    elif 60 <= persentase < 75:
        return 0.3
    elif 75 <= persentase < 90:
        return 0.5 
    elif 90 <= persentase < 105:
        return 0.7
    elif 105 <= persentase < 120:
        return 0.8
    else:
        return 1.0 

def Penilaian_Sikap(persentase):
    if persentase < 40:
        return 0.2 
    elif 40 <= persentase < 60:
        return 0.3
    elif 60 <= persentase < 80:
        return 0.5 
    elif 80 <= persentase < 100:
        return 0.7
    elif 105 <= persentase < 120:
        return 0.8
    else:
        return 1.0 