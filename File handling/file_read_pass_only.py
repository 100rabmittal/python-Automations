# opening a file from pwd in read only mode
f = open('File handling/input_file_read_pass_only.txt', 'r')

#reading the whole file
#print(f.read())

#creating new output file with write mode
pass_file = open('File Handling/pass_file.txt', 'w')

#now i want to read only lines where status = pass (p)
for line in f:
    if line.split()[2].lower() == 'p':
        #writing it to a file named as pass_file
        pass_file.write(line)

#close the file after use
f.close()
pass_file.close()