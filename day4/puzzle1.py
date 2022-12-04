total=0
with open("input.txt", "r") as f:
    data=f.read().replace("\r", "").split("\n")
    for pair in data:
        temp=pair.split(",")
        list=[]
        for i in temp:
            list.append(i.split("-"))
        for i in range(0,len(list)):
            for n in range(0,len(list[i])):
                list[i][n]=int(list[i][n])
        if list[0][0]>=list[1][0] and list[0][1]<=list[1][1] or list[1][0]>=list[0][0] and list[1][1]<=list[0][1]: 
            print(f"{list[0][0]} - {list[0][1]}, {list[1][0]} - {list[1][1]}")
            total+=1

print(total)