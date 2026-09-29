def convert_temperature(value, unit):
    if unit.upper() == 'C':
        return (value * 9/5) + 32
    elif unit.upper() == 'F':
        return (value - 32) * 5/9
    
    else:
        return "Pesan: unit tidak valid. Harap gunakan 'C' atau 'F'."
    
print("======== Konversi Suhu ====")

input_suhu = float(input("Masukkan suhu: "))

