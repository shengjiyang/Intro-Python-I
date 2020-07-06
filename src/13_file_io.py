"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

f = open("shakespeare.txt", "r")
text = f.read()
print(text)

# Open up a file called "meng.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "meng.txt" and inspect it to make
# sure that it contains what you expect it to contain

f2 = open("meng.txt", "w")
f2.write("昔孟母，擇鄰處；子不學，斷機杼。")