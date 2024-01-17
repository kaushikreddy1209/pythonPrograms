fname=input("Enter a filename: ")
try:
    fhand=open(fname,'r')
except:
    print("File could not be opened:",fname)
    quit()
count=0
for line in fhand:
    count+=1
    # line = line.rstrip()
    # print(line.upper())
print(f"The file has {count} number of lines in it")