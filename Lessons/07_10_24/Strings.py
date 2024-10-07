proem: str = "Cantami, o Diva, del pelide Achille" 

print(proem.lower())
print(proem.upper())
print(proem[proem.index("Diva"):proem.index("Diva") + len("Diva")])
print(proem[::-1].capitalize())
print(proem.replace("e", "dio cane"))
print(proem)