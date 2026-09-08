#-- Initial Data Array. --#
A = [1, 2, 3, 4, 5] #-- Automaticaly create 5 index in the array. --#
n = len(A) #-- Len of the array. --#
#-- Step 1: Preprocessing - Creating a Prefix Sum. --#
P = [0] * n #-- Result: P = [0, 0, 0, 0, 0] --#
P[0] = A[0] #-- Result: P = [1, 0, 0, 0, 0] --#
for i in range(1,n):
    P[i] = P[i-1] + A[i] #-- Result: P = [1, 3, 6, 10, 15]. --#
#-- Query from L to R. --#
L, R = 1, 3 #-- Query indices. --#
if L == 0:
    result = P[R]
else:
    total_sum = P[R] - P[L-1]
print("Sum from index", L, "to", R, "is:", total_sum)