# Appending text in a file
sf = "\nThis is how we append in a file."
f = open("main.txt", "a")
f.write(sf)
f.close()
