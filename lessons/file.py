fw = open('../test/test.txt', 'a')
fw.write('Hello World\n')
fw.close()

fw = open('../test/test1.txt', 'w')
fw.write('Privet mir!!!')
fw.close()

fw = open('../test/test1.txt', 'r')
text = fw.read()
fw.close()
print(text)

