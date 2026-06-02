lst = [27]
b = bytes(lst)
ba = bytearray(lst)
ba.append(23) 
print("Bytes:", b)
print("Bytearray:", ba)