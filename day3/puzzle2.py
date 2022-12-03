import sys
total=0
def prioritise(char):
    if char.isupper():
        return ord(char)-38
    return ord(char)-96

def chunks(list, n):
    n = max(1, n)
    gen=(list[i:i+n] for i in range(0, len(list), n))
    return [x for x in gen]
with open("rucksacks.txt", "r") as f:
    list=f.read().replace("\r", "").split("\n")
    
    for i in range(0,len(list)):
        temp=[]
        for t in range(0,len(list[i])):
            temp.append(prioritise(list[i][t]))
        list[i]=temp
    groups=chunks(list, 3)
    for i in range(0,len(groups)):
        for t in groups[i][0]:
            if t in groups[i][1] and t in groups[i][2]: 
                total+=t
                break

print(total)