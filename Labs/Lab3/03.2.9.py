wave_lenght: float = float(input("Wave lenght : "))

if(wave_lenght > 1E-1):
    print("Radio wave")
elif(wave_lenght > 1E-3):
    print("Micro wave")
elif(wave_lenght > 7E-7):
    print("Infrared")
elif(wave_lenght > 4E-7):
    print("Visible light")
elif(wave_lenght > 1E-8):
    print("Ultraviolet")
elif(wave_lenght > 1E-11):
    print("X ray")
else:
    print("Gamma ray")