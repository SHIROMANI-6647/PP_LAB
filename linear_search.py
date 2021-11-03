def linear_search(list, n, ele):
  for i in range(0,n):  
    if( list[i] == ele):
      return i
  return -1
list = [4,9,3,1,8,2]
ele = 9
n = len(list)
result = linear_search(list, n, ele)
if(result == -1):
  print("element not found")
else:
  print("element found at index:", result)

