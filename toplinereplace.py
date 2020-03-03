#creat a py file where top line replaces "this is a new line" 
#Note if the file we want to write already exists, then Python will open it but it will delete the existing content!
#We will just use one command to write to files, file.write().
#The perameter we pass will be what is written to the file.
#Note, each time we use the write() command, it will write the content wherever it was left off.
#file = open("filename.txt", "w")

file = open("replacetopline.txt", "w")
for n in range(0):
    newline = "This is a new line" + str(n) + "\n"
    file.write(newline)
file.close()