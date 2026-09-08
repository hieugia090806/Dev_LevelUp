- Techniques Frequently Used: 
  + Prefix Sum 
  + Two Pointers 
  + Sliding Window
  + Binary Search 
  + Greedy 
  + Quy hoạch động 
  + Backtracking
  
- Signals:
  + Hỏi tổng của nhiều đoạn con khác nhau -> Prefix Sum
  + Mảng đã sắp, tìm cặp theo tổng -> Two Pointers
  + Đoạn con LIÊN TIẾP tối ưu -> Sliding Window
  + Tìm trong mảng sắp xếp lớn/ngưỡng nhỏ nhất -> Binary Search
  + Mỗi bước chọn 'to nhất' và bài cho phép -> Greedy
  + Đếm số cách/tối ưu, bài con chồng lấp -> Dynamic Programming
  + Liệt kê mọi cấu hình có ràng buộc -> Backtracking

# Prefix Sum Technica Description. #
>
- Definition: A preprocessing technique that computes and stores the cumulative sum of elements from the beginning of the array up to the current index.
- Purpose: Optimizes range sum queries for any interval [L, R].
- Time Complexity:
  + Preprocessing: O(N) - Executed once to build the Prefix Sum array.
  + Query: O(1) - Retrieves the sum of range [L, R] instantly, highly efficient for multiple recurring queries.
- Formula:
  + P[i] = P[i-1] + A[i]
  + Sum(L, R) = P[R] - P[L-1] (for L > 0)
================================================================================