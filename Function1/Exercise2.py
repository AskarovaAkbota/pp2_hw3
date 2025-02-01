def temperature(F):
    C = (5 / 9) * (F - 32)
    return C
F=float(input("Frongate:"))
print("Celcies:",temperature(F))