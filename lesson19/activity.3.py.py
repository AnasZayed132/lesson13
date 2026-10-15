og_l=[1,2,3,4,7,6,5]
print(og_l)
count=0
for i in og_l:
    count=count+i
average=count/len(og_l)
print("sum is ",count,"and average is",average)

og_l.sort()
print("smallest element is",og_l[0])

print("the last number of the list is ",og_l[-1])