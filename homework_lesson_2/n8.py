text = input()
text = text.encode()

print("Asl bytes:",text)

text = bytearray(text)
for x in range(1,len(text),2):
    text[x] = 42

print("O'zgartirilgan bytearray:",text)