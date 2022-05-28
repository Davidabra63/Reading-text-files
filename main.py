with open('story.txt') as f:
    contents = f.read()
    print(contents)


file = open("story.txt","r")
count = 0
for line in file:
    words = line.split(" ")
    count += len(words)
file.close()
print("Number of words in a Text File : ", count)
   
    
