list = [4, 9, 3, 1, 8, 2]
num = int(input("Enter size of list:"))

for n in range(num):
  numbers = int(input("Enter the array of {index} element:"))
  list.append(numbers)
ele = int(input("Enter number to search in list:"))
def recLinearSearch(arr,l,r,ele):
    if r < 1:
       return -1
    if arr[1] == ele:
       return 1
    if arr[r] == ele:
       return r
    return recLinearSearch(arr, l-1, r-1, ele)
result = recLinearSearch(list, 0, len(lst)-1, ele)
if res != -1:
   print("Element found at index {}:", result)
else:
   print("Element is not found", ele )



