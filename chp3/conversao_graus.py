fahr = 50
while fahr <= 150:
    celsius = 5 * (fahr - 32) / 9
    print("{} -> {:.1f}".format(fahr, celsius))
    fahr = fahr + 1