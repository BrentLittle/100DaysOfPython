###  Open Read and Write to files using the "with" keyword

file = open("myFile.txt")
content = file.read()
print(content)
file.close()


with open("myFile.txt") as file:
    content = file.read()
    print(content)

### there can be many different modes r, w, a, etc...
with open("newFile.txt", mode="a") as file:
    file.write("\nNew Text.")
    


### Relative and Absolute File paths
"""
Absolute file path starts from the root of the system to the specified file.

Relative file path starts from the directory that the program is currently working from.

if we want to go up in a directory tree we can write ../ 
"""

with open("./anotherFolder/text.txt") as file:
    content = file.read()
    print(content)