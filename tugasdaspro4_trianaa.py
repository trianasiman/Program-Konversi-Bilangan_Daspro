angka_input = input("Masukkan angka: ")

if angka_input.isdigit():
    angka = int(angka_input)
    print("Angka Desimal:", angka)

    angka_biner = angka
    biner = ""
    for _ in range(angka.bit_length()):
        sisa = angka_biner % 2
        biner = str(sisa) + biner
        angka_biner //= 2
    print("Angka Biner:", biner)

    angka_oktal = angka
    oktal = ""
    for _ in range(angka.bit_length()):
        sisa = angka_oktal % 8
        oktal = str(sisa) + oktal
        angka_oktal //= 8
    print("Angka Oktal:", oktal)

    heksadesimal_angka = angka
    heksa_digit = "0123456789ABCDEF"
    heksadesimal = ""  
    for _ in range(angka.bit_length()):
        sisa = heksadesimal_angka % 16
        heksadesimal = heksa_digit[sisa] + heksadesimal
        heksadesimal_angka //= 16
    print("Angka Heksadesimal:", heksadesimal)
else:
    print("Masukkan harus berupa bilangan bulat (integer).")
