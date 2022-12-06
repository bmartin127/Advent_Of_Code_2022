

# opening the file in read mode
readin = open("readin.txt", "r")
  
# reading the file
readin_list = readin.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = readin_list.split("\n")
# print(data_into_list)

# readin original state
length = len(data_into_list)
crates1 = []
crates2 = []
crates3 = []
crates4 = []
crates5 = []
crates6 = []
crates7 = []
crates8 = []
crates9 = []

for i in range(8):
    crates1.append(data_into_list[i][1])
    crates2.append(data_into_list[i][5])
    crates3.append(data_into_list[i][9])
    crates4.append(data_into_list[i][13])
    crates5.append(data_into_list[i][17])
    crates6.append(data_into_list[i][21])
    crates7.append(data_into_list[i][25])
    crates8.append(data_into_list[i][29])
    crates9.append(data_into_list[i][33])
for i in range(8):
    print(crates1[i],crates2[i],crates3[i],crates4[i],crates5[i],crates6[i],crates7[i],crates8[i],crates9[i])
while(" " in crates1):
    crates1.remove(" ")
while(" " in crates2):
    crates2.remove(" ")
while(" " in crates3):
    crates3.remove(" ")
while(" " in crates4):
    crates4.remove(" ")
while(" " in crates5):
    crates5.remove(" ")
while(" " in crates6):
    crates6.remove(" ")
while(" " in crates7):
    crates7.remove(" ")
while(" " in crates8):
    crates8.remove(" ")
while(" " in crates9):
    crates9.remove(" ")
crates1.reverse()
crates2.reverse()
crates3.reverse()
crates4.reverse()
crates5.reverse()
crates6.reverse()
crates7.reverse()
crates8.reverse()
crates9.reverse()

cratesById = {1: crates1, 2: crates2, 3: crates3, 4: crates4, 5: crates5, 6: crates6, 7: crates7, 8: crates8, 9: crates9}


def move(where,howmuch,to):
    temp = []
    for x in range(howmuch):
        temp.append(where.pop())
    for i in range(howmuch):
        to.append(temp.pop())

count = (10)
steps = []
while count < length:
    steps.append([int(i) for i in data_into_list[count].split() if i.isdigit()])
    count = count+1

for p in steps:
    numToMove, startCrate, endCrate = p
    move(cratesById[startCrate], numToMove, cratesById[endCrate])
    print(numToMove, ' start: ', startCrate, ' end: ', endCrate)

print(crates1[len(crates1)-1],crates2[len(crates2)-1],crates3[len(crates3)-1],crates4[len(crates4)-1],crates5[len(crates5)-1],crates6[len(crates6)-1],crates7[len(crates7)-1],crates8[len(crates8)-1],crates9[len(crates9)-1])


    