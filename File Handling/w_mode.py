# W mode >> Open the file for writing, It overwrites the file or truncate the file
# Creates a new file if file don't exist

fh = open("file.txt", 'wt')
fh.write("This is over written. Hello World.\n")
fh.close()