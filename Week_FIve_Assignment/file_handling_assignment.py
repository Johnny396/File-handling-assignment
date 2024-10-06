"""File handling Assignment"""

f = open("my_file.txt", "w", encoding="utf-8")
f.write("How old are you?\n")
f.write("October 9 is your birth date\n")
f.write("Would you like to have your birth day celebrated in a 5-star hotel?")
f.close()


#File Appending
file = open("my_file.txt", "a", encoding="utf-8")
file.writelines(["\nI am an African", "\nFrom Nigeria", "\nThat currently lives in Lagos"])


#File reading and display
file = open("my_file.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()


#Error Handling
try:
    f = open("my_file.txt", "r", encoding = "utf-8")
except FileNotFoundError as e:
    print(e)
except PermissionError as e:
    print(e)
else:
    content = f.read()
    print(content)
    f.close()
finally:
    print("Program exited")
    