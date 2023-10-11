#https://www.youtube.com/watch?v=HRJRq2r7eL8
score = 0
question = int(input("what is 5x5: "))
if question ==25:
    print("Correct")
    score=score+2
else:
    print("Incorrect")
name=input("enter your name: ")
file=open("score.txt","a")
file.write(str(score)+","+name+"\n")
file.close()

file=open("score.txt","r")
readthefile = file.readlines()
sortedData = sorted(readthefile,reverse=True)
print("Top 5 Scores")
print("Pos\tPoints,Name")
for line in range (5):
    print(str(line+1)+"\t"+str(sortedData[line]))
