try:
    # Open the file in write mode ('w')
    with open("my_file.txt", 'w') as file:
        # Perform any write operations if needed
        # For example:
        file.write("This is line 1\n")
        file.write("This is line 2\n")
        file.write("This is line 3\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to create the file.")


    #Quiz2
file_content=open('my_file.txt').read()
print(file_content)

#Quiz3

with open('my_file.txt', 'a') as file:
    file.write('this is my 1st append lin\n')
    file.write('this is my 2st append lin\n')
    file.write('this is my 3st append lin\n')

#Quiz 4
try:
    # Open the file in append mode ('a')
    with open("my_file.txt", 'a') as file:
        # Append three additional lines of text to the existing content
        file.write("This is an appended line 4\n")
        file.write("This is an appended line 5\n")
        file.write("This is an appended line 6\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to append to the file.")
finally:
    print("File appending process completed.")





        