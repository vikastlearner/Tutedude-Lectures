# x mode >> to create a file


fh = open("file.txt", 'xt')

# Writing into the file
# Write (content)

fh.write("Hello World.\n")
fh.write("Next line")

# Close the file
fh.close()