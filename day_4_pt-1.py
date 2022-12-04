

# opening the file in read mode
readin = open("readin.txt", "r")
  
# reading the file
readin_list = readin.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = readin_list.split("\n")
# print(data_into_list)
score = 0
first_pairs_1 = 0
first_pairs_2 = 0
second_pairs_1 = 0
second_pairs_2 = 0
for x in range(len(data_into_list)):
    first_pairs_1 = (int((data_into_list[x].split(",")[0]).split("-")[0]))
    first_pairs_2 = (int((data_into_list[x].split(",")[0]).split("-")[1]))
    second_pairs_1 = (int((data_into_list[x].split(",")[1]).split("-")[0]))
    second_pairs_2 = (int((data_into_list[x].split(",")[1]).split("-")[1]))

    if (first_pairs_1 <= second_pairs_1 and first_pairs_2 >= second_pairs_2) or (first_pairs_1 >= second_pairs_1 and first_pairs_2 <= second_pairs_2):
        print("match!", first_pairs_1,first_pairs_2,second_pairs_1,second_pairs_2)
        score = score + 1
    print(first_pairs_1,first_pairs_2,second_pairs_1,second_pairs_2)
print("score:", score)