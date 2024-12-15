temperatura = int(input("Unesite temperaturu: "))
test_temperatura = -1
temperatura = test_temperatura
poruka = ""
if temperatura < 0:
    poruka ="Oprez! Klizavo!"

    if temperatura > 0:
        poruka = "temperatura iznad nule!"
        if temperatura > 30:
            poruka ="Ukljucite klima uredjaj!"

ocekivana_poruka = "Oprez! Klizavo!"
if poruka == ocekivana_poruka:
    print("Case - ispod nule - Test prosao!")