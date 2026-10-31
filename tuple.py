habit_info=tuple()
habit_info=("10 pushups a day",True,10,1.5)

weekly_habbit=tuple()
weekly_habbit=1,0,0,1,0,0,1
print("this is the length of the weekly habbit tuple",len(weekly_habbit))
print("on monday in the tuple its",weekly_habbit[0],"and on thursday its ",weekly_habbit[3])
print("if your wondering from monday to thursday is dont worry:",weekly_habbit[0:3])

new_habit_info=habit_info+(9,)

print("this is the tuple with an added number",new_habit_info)

completed=weekly_habbit.count(1)
missed=weekly_habbit.count(0)

print("you completed",completed,"days")
print("you missed",missed,"days")
done=0
not_done=0
for i in range(len(weekly_habbit)):
    if i == 1:
        done+=1

    else:
        not_done+=1
if done>not_done:
    print("good habbit progress keep it going\n")
else:
    print("try be more consistent\n")
print("="*5,"weekly habit traker","="*5)
print("the habbit was ",habit_info[0])
print("your consisency was ",weekly_habbit)
print("you completed",completed)
print("you missed",missed)
print("="*10)

