""""
Here finally is always executed, whether there is error or not.
Else is executed when there is no error.
except is used to handle the various errors/exception
"""

try:
    fh = open("file.txt", "wt")
    fh.write("Hello World")
except FileNotFoundError as file_err:
    print("File not found")
    print(file_err)
else:
    print("File found")
    print(fh)
finally:
    print("Closing file")
    fh.close()

