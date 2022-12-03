total=0
def prioritise(char):
    if char.isupper():
        return ord(char)-38
    return ord(char)-96

with open("rucksacks.txt", "r") as f:
    rucksacks=f.read().replace("\r", "").split("\n")
    for i in range(0,len(rucksacks)):
        list=[]
        for t in range(0,len(rucksacks[i])):
            list.append(prioritise(rucksacks[i][t]))
        rucksacks[i]=list
        temp=[rucksacks[i][:int(len(rucksacks[i])/2)],rucksacks[i][int(len(rucksacks[i])/2):]]
        rucksacks[i]=temp
        for t in rucksacks[i][0]:
            if t in rucksacks[i][1]:
                total+=t
                break


print(total)