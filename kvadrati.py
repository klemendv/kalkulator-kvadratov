def izracun_kvadrata():
    print("Program za izračun lastnosti kvadrata")
    print("Izberite eno od možnosti:")
    print("1. Izračun površine kvadrata")
    print("2. Izračun obsega kvadrata")
    print("3. Izračun diagonale kvadrata")
    print("4. Izhod")

    izbira = input("Vaša izbira (1/2/3/4): ")

    if izbira == "1":
        stranica = float(input("Vnesite dolžino stranice kvadrata: "))
        povrsina = stranica ** 2
        print(f"Površina kvadrata je {povrsina}")
    elif izbira == "2":
        stranica = float(input("Vnesite dolžino stranice kvadrata: "))
        obseg = 4 * stranica
        print(f"Obseg kvadrata je {obseg}")
    elif izbira == "3":
        stranica = float(input("Vnesite dolžino stranice kvadrata: "))
        diagonala = stranica * (2 ** 0.5)
        print(f"Diagonala kvadrata je {diagonala}")
    elif izbira == "4":
        return
    else:
        print("Neveljavna izbira. Prosimo, izberite 1, 2, 3 ali 4.")

    izracun_kvadrata()

if __name__ == "__main__":
    izracun_kvadrata()
