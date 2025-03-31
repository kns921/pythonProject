file_name = 'file.txt'
data = 'Hello World'

# fw = open('test/file_name', 'a')
# fw.write(data)
# fw.close()

with open('../file_name', 'a') as f:
    f.write(data)
