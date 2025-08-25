#  Create a file
file = open('assignment.txt', 'a')
file.write('Hello world.\n')
file.close()

# Read file
file = open('assignment.txt', 'r')
data = file.read()
print(data)
file.close()

# Modify content inside file
file = open('assignment.txt', 'a')
file.write("I am learning file handling in Python!")
file.close()

file = open('assignment.txt', 'r')
edit = file.read()

# Update content to a new file
file = open('modified.txt', 'a')
file.write(edit)
file.close()

# Error handling
request = input("Enter file name (e.g- name.txt, name.pdf): ")
try:
    file = open(request, 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")