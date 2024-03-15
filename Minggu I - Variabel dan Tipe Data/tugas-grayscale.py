def togray(R, G, B):
    grayscale = int((0.3 * R) + (0.59 * G) + (0.11 * B))
    return grayscale

print("\n Program menentukan Grayscale \n")
R = float(input("Masukan Value Red   : "))
G = float(input("Masukan Value Green : "))
B = float(input("Masukan Value Blue  : "))

operation = togray(R, G, B)

print("Hasil Konversi Dari RGB ke Grayscale :", operation)
