

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
def overlap(start1, end1, start2, end2):
    """Does the range (start1, end1) overlap with (start2, end2)?"""
    return (
        start1 <= start2 <= end1 or
        start1 <= end2 <= end1 or
        start2 <= start1 <= end2 or
        start2 <= end1 <= end2
    )
for x in range(len(data_into_list)):
    first_pairs_1 = (int((data_into_list[x].split(",")[0]).split("-")[0]))
    first_pairs_2 = (int((data_into_list[x].split(",")[0]).split("-")[1]))
    second_pairs_1 = (int((data_into_list[x].split(",")[1]).split("-")[0]))
    second_pairs_2 = (int((data_into_list[x].split(",")[1]).split("-")[1]))

    if overlap(first_pairs_1, first_pairs_2, second_pairs_1, second_pairs_2):
        print("match!", first_pairs_1,first_pairs_2,second_pairs_1,second_pairs_2)
        score = score + 1
print("score:", score)