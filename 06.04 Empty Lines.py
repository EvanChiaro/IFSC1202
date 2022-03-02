empty = open("06.04 EmptyLinesInput.txt")
new = open("06.04 EmptyLinesOutput.txt", "a")
read = 0
write = 0
e = empty.readline()
while e != "":
    read += 1
    if e != "\n":
        new.write(e)
        write += 1
    e = empty.readline()
print(str(read) + " Records read")
print(str(write) + " Records written")