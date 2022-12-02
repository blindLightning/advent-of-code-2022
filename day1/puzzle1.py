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