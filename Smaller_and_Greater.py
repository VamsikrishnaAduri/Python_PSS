def solve(A):
  sorted_lst = sorted(A)
  Strictly_Smaller_el = sorted_lst[0]
  Srtictly_Larger_el = sorted_lst[-1]
  Dummy = 0
  for i in range(len(A)):
    if A[i]>Strictly_Smaller_el:
      if A[i]<Srtictly_Larger_el:
        Dummy +=1
  return Dummy
 
