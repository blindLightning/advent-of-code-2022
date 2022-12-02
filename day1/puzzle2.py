#loads calary list
with open("list.txt", "r") as f:
    list=f.read()
    list=list.replace("\r", "")
    list=list.replace("\n", "-")
    print(list)
    list=list.split("--")
    for i in range(0, len(list)):
        list[i]=list[i].split("-")
        elf_cal=0
        for t in list[i]:
            elf_cal+=int(t)
        list[i]=elf_cal
    print(len(list))
    maximum=max(list)
    num=list.index(maximum)+1
    print("The elf with the most calaries has: "+str(maximum)+" and is elf "+str(num))
    temp=list
    temp.pop(num-1)
    second=max(temp)
    num=list.index(second)+1
    print("The elf with the second most calaries has: "+str(second)+" and is elf "+str(num))
    temp.pop(num-1)
    third=max(temp)
    num=list.index(third)+1
    print("The elf with the third most calaries has: "+str(third)+" and is elf "+str(num))
    temp.pop(num-1)
    print("The total calaries of the elves is "+str(third+second+maximum))