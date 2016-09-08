from random import randint
name=raw_input('input your name:')
f=open('1.txt')
lines=f.readlines()
f.close()

scores={}
for i in lines:
    s=i.split()
    scores[s[0]]=s[1:]
score=scores.get(name)
if score is None:
    score=[0,0,0]

game_times=int(score[0])
min_times=int(score[1])
total_times=int(score[2])
if game_times>0:
    avg_times=float(total_times)/game_times
else:
    avg_times=0
print '%s,round %d,fast %d,average %.2f'%(name,game_times,min_times,avg_times)

num=randint(1,5)
times=0
print'guess what i think'
bingo=False
while bingo==False:
    times+=1
    answer=input()
    if answer<num:
        print'too small'
    if answer>num:
        print'too big'
    if answer==num:
        print'bingo'
        bingo=True
if game_times==0 or times<min_times:
    min_times=times
total_times+=times
game_times+=1
scores[name]=[str(game_times),str(min_times),str(total_times)]
result=''
for n in scores:
    line=n+' '+' '.join(scores[n])+'\n'
    result+=line
f=open('1.txt','w')
f.write(result)
f.close()
