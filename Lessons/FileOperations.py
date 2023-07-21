f = open('MyFiles/Lectures/file1.txt', 'r')
text=f.read()
print(text)
f.close()

# File Opening Modes
# 1. read(r): Open File In Read Mode/ Default Mode
# 2. write(w): Open File In Write Mode. In That we can add new content to file but previous file content is erase.
# 3. append(a): Open file in append mode in that new content added at the end without erasing previous content.
# 4. create(x): Create file and give error if file already exists.
# 5. text(t): Used to handle text Files (Default Mode).
# 6. binary(b): Used to open file in binary mode. useful to read jpeg,png,exe, etc.. 


# Writing into File
f=open('MyFiles/Lectures/file2.txt','w')
f.write("Hello, My name is Shubham!!")
f=open('MyFiles/Lectures/file2.txt','r')
file2data=f.read()
print(file2data)
f.close()


# Append Mode 
print("Append Mode:: ")
f=open('MyFiles/Lectures/file2.txt','a')
f.write("\nHey brother, How are you? ")
f=open('MyFiles/Lectures/file2.txt','r')
file2data=f.read()
print(file2data)
f.close()

# Using "with" Statement
print("Using with statement ::")
with open('MyFiles/Lectures/file2.txt','r') as f:
    with_data=f.read()
    print(with_data)
    
    
# readline() Method- Use to read file content line by line

f=open('MyFiles/Lectures/file3.txt','r')
while True:
    line=f.readline()
    if not line:
        break
    print(line)
    

# writeline() Method - to write Multiple Lines

f= open('MyFiles/Lectures/file4.txt','w')
lines=['Line1 \n''Line2  \n''Line3 \n''Line4\n']
f.writelines(lines)
f.close()
f=open('MyFiles/Lectures/file4.txt','r')
text=f.read()
print(text)
f.close()

# seek() Function - allows to move the current position within a file to specific point
with open('MyFiles/Lectures/file4.txt','r') as f:
    f.seek(10)
    data=f.read(5)
    print(data)


# tell() Function - Returns the current position of seek within the file 
f=open('MyFiles/Lectures/file4.txt','r')
f.seek(12)
print(f.tell())

# truncate() - We Can truncate the file from starting position
with open('MyFiles/Lectures/file5.txt','w') as f:
    f.write("This Is Truncate Method")
    f.truncate(10)

with open('MyFiles/Lectures/file5.txt','r') as f:
    filedata=f.read()
    print(filedata)
    f.close()