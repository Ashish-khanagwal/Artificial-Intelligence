# Appending text in a file
sf = "\nThis is how we append in a file."
f = open("main.txt", "a")
f.write(sf)
f.close()

# Copy a File
with open("text.txt", "rb") as src, open("text2.txt", "wb") as dst:
    while True:
        chunk = src.read(1024)
        if not chunk:
            break
        dst.write(chunk)
