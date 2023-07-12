with open("story.txt", 'r') as file:
    readlines = file.readlines()

new_paragraph = []

for i in readlines:
    #print(i, end='')
    lst = []
    for j in range(len(i)):
        if i[j] == '_':
            lst.append(j)
    print(lst)
    for i in range(1, (lst%(3*2))+1, 1):
        3 * (i * 2 -1)