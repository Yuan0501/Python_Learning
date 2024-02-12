#read files
file = open("/Users/yuanyuanzhu/Coursera-lesson/Python/test.txt", mode = 'r')
data = file.readline()
print(data)
file.close()

# file.read() return entire file
# file.read(10) return 0-10 character in the file
# file.readline()return first line in the file'
# file.readline(10) return 0-10 characters in the file
# file.readlines() return all the lines in the file using list


#write files and catch the error
try:
    with open('newfile.txt', 'w') as file:
        file.writelines(["This is a new file created!", "\nThis is another line to added."])
except FileNotFoundError as e:
    print("ERROR", e)