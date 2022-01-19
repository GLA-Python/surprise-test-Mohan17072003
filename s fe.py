def expanding(lst):
    
diff=([])

for i in range(len(lst)):

 if(i<len(lst)-1):

  x=lst[i]-lst[i+1]

  if(x<0):

   x=-x

  diff.append(x)

for i in range(len(diff)):

 if(i<len(diff)-1):

  if(diff[i+1]>diff[i]):

   f=0

  else:

   f=1

   break

if(f==1):

  return  True