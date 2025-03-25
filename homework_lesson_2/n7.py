text = b'salom dunyo'

katta_text = text.decode().upper()
text = bytearray(katta_text.encode())
print(text)