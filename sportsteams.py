file = open ("sportsteams.txt", "r")

for i in range(5):
    line = file.readline()
    if i == 0:
        print(line)
    if i == 3:
        print(line)
file.close()
