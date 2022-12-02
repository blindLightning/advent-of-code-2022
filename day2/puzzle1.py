score=0

with open("game.txt", "r") as f:
    file=f.read()
    file=file.replace("\r", "")
    file=file.split("\n")
    for i in range(0,len(file)):
        file[i]=file[i].split(" ")
        play=file[i][0]
        response=file[i][1]
        if response=="X": score+=0
        elif response=="Y": score+=3
        elif response=="Z": score+=6
        if play=="A" and response=="Y" or play=="B" and response=="X" or play=="C" and response=="Z": score+=1
        if play=="A" and response=="Z" or play=="B" and response=="Y" or play=="C" and response=="X": score+=2
        if play=="A" and response=="X" or play=="B" and response=="Z" or play=="C" and response=="Y": score+=3

print(score)