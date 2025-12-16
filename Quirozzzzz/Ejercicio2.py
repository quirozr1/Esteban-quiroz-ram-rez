import random
Velocidad= random.randint(0,100)
if (Velocidad <= 30):
    print(f"Vas a una velocidad de {Velocidad:.1f} km/h y esta velocidad es ideal para zonas escolares.")
elif (Velocidad >= 31 and Velocidad <= 59):
    print(f"Vas a una velocidad de {Velocidad:.1f} km/h, por lo tanto estas infringirndo los limites de velocidad y debes ir a una velocidad de 30 km/h para transitar en zonas escolares.")
elif (Velocidad <= 60):
    print(f"Vas a una velocidad de {Velocidad:.1f} km/h y esta velocidad es ideal para vías urbanas.")
elif (Velocidad >= 61 and Velocidad <= 79):
    print(f"Vas a una velocidad de {Velocidad:.1f} km/h, por lo tanto estas infringirndo los limites de velocidad y debes ir a una velocidad de 60 km/h para transitar en vías urbanas.")
elif (Velocidad <= 80):
    print(f"Vas a una velocidad de {Velocidad:.1f} km/h y esta velocidad es ideal para vías rurales.")
elif (Velocidad >= 81 and Velocidad <= 99):
    print(f"Vas a una velocidad de {Velocidad:.1f} km/h, por lo tanto estas infringirndo los limites de velocidad y debes ir a una velocidad de 80 km/h para transitar en vías rurales.")    
elif (Velocidad <= 100):
    print(f"Vas a una velocidad de {Velocidad:.1f} km/h y esta velocidad es ideal para rutas nacionales.")
elif (Velocidad >= 101):
    print(f"Vas a una velocidad de {Velocidad:.1f} km/h, por lo tanto estas infringirndo los limites de velocidad y debes ir a una velocidad de 100 km/h para transitar en rutas nacionales.")
else:
    print(f"Vas a una velocidad de {Velocidad:.1f} km/h.")