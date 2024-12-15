temperatura = int(input("Unesite temperaturu: "))

if temperatura < 0:
    print("Oprez! Klizavo!")

    if temperatura > 0:
        print("temperatura iznad nule!")
        if temperatura > 30:
            print("Ukljucite klima uredjaj!")