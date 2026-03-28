# ===============================================================
# Open, read and write to files
# ===============================================================

# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

# # mode Parameters - read(r)(default), write(w), append(a)
# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew Text")

# with open("my_file.txt", mode="r") as file:
#     content = file.read()
#     print(content)

# with open("new_file.txt", mode="w") as file:
#     file.write("New Text")

# Absolute Path
# with open("/Python/course-files/data.txt") as file:
#     content = file.read()
#     print(content)

# Relative Path
with open("../course-files/data.txt") as file:
    content = file.read()
    print(content)