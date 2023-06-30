

def promt_bands():
    bands = []

    while True:
        if len(bands) > 0:
            band = input("Enter a Band or press Enter to Continue: ")
            
        else:
            band = input("Enter a Band: ")

        if band == "":
            break
        
        bands.append(band)

    print("Bands:", bands)
