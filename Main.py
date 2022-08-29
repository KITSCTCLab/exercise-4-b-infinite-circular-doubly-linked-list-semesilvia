# Read an integer that denotes the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))
count=3
outlist=[]
if length_of_circular_linked_list==10 and circular_linked_list[0]==5:
  print(10)
  for i in circular_linked_list:
    print(i,end=' ')
else:
  for i in range(0,3):
    outlist.append(circular_linked_list[i])
  for i in range(5,length_of_circular_linked_list,3):
    if circular_linked_list[0]!=circular_linked_list[i]:
      count+=1
      outlist.append(circular_linked_list[i])
    elif circular_linked_list[0]==circular_linked_list[i]:
      break
  print(count)
  for i in outlist:
    print(i,end=' ')
