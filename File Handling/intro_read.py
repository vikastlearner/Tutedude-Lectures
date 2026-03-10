# Opening a file in python
# Syntax: pen(file_name, mode to open)
# Modes: r,x,w,a,t,b. "rt" is the default mode

fh = open("file.txt","rt")

# Read Operation
# read(x) >> Read the contents of the file as str. Here x is number of character
"""
conent = fh.read(10)
print(conent)
print(type(conent))
"""

#readline() >> Read each line until next line. So after each line there will be space.
'''
line1 = fh.readline()
line2 = fh.readline()
line3 = fh.readline()

print(f"Line 1: {line1}\nLine2: {line2}\nLine3: {line3}\nLine4: {fh.readline()}")
# Empty line indicates the end of the lines.
'''

# readlines() >> It creates each line as elements of LIST
print(f"Line: {fh.readlines()}")
print(type(fh.readlines()))

fh.close()
