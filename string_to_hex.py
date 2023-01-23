asc = input()
hexa = ""
for i in range(len(asc)):
    
    c = asc[i]
    ch = ord(c)
    p = hex(ch).lstrip("0x").rstrip("L")
    hexa = hexa+" "+ p
print(hexa)