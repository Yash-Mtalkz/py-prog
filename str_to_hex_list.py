string= input()
hexa = ""
lst = []
j=0
 
for letter in string:
    lst.append(letter)
   
for i in lst:
    ch = ord(lst[j])
    p = hex(ch).lstrip("0x").rstrip("L")
    hexa = hexa+" "+ p
    j+=1
print(hexa)