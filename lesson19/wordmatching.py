def mach_words(words):
  ctr=0
  lst=[]
  for i in words:
    if len(i)>1 and i[0]==i[-1]:
      ctr=ctr+1
      lst.append(i)
  print("list of word with first and last character",lst)
  return ctr
count=mach_words(["abc","121","321","475","343"])
print("number of words",count)