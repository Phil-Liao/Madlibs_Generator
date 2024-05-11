with open("story.txt", 'r') as file:
    readlines = file.readlines()

new_paragraph = []

for i in readlines:
    #print(i, end='')
    lst = []
    for j in range(len(i)):
        if i[j] == '_':
            lst.append(j)
    #print(lst)

    #print(len(lst)/6)
    line = i
    for j in range(1, int((len(lst)/6)+1)):
        start = lst[(3*((j*2)-1))-1]+2
        end = lst[(3*((j*2)-1))]-2
        #print(i[start])
        #print(i[end])
        #print(i[start:end+1])
        if i[end].isnumeric():
            answer = input("Enter a " + i[start:end] + ':')
            answer = answer.upper()
        else:
            answer = input("Enter a " + i[start:end+1] + ':')
            answer = answer.upper()
        #print("___("+i[start:end+1]+")___")
        #print(answer)
        line = line.replace(f"___({i[start:end+1]})___", answer.upper(), 1)
        #print(line)
    new_paragraph.append(line)
print("\nHere is what you've generated:")
for i in new_paragraph:
    print(i)