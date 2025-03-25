with open("test_9.txt","rb") as file:
    text_fayl = bytearray(file.read())

for x in range(len(text_fayl)):
    if text_fayl[x] == 32:
        text_fayl[x] = 45

print(text_fayl)