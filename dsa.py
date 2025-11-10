# class pal_str:
#     def pal_string(self,s):
#         i = len(s) - 1
#         new_s = ""
#         while i>=0:
#             new_s += s[i]
#             i -= 1
#         return new_s == s
    
# obj = pal_str()
# s = str(input())
# result = obj.pal_string(s)
# print(result)


# class rev_str:
#     def reverse_string(self,s):
#         i = len(s)-1
#         new_s = ""
#         while i>=0:
#             new_s += s[i]
#             i -= 1
#         return new_s

# obj = rev_str()
# s = str(input())
# result = obj.reverse_string(s)
# print(result)            



# class c_vow:
#     def count_vow(self,s):
#         vow = ["A","E","I","O","U","a","e","i","o","u"]
#         cnt = 0
#         for i in s:
#             if i in vow:
#                 cnt += 1
#         return cnt
# obj = c_vow()
# s = str(input())
# result = obj.count_vow(s)
# print(result)



# class r_spa:
#     def remove_spa(self,s):
#         lst = [i for i in s]
#         spa = " "
#         for i in lst:
#             if i==spa:
#                 lst.remove(i)
#         return "".join(lst)
# obj = r_spa()
# s = str(input())
# result = obj.remove_spa(s)
# print(result)


# class fre:
#     def find_freq(self,s):
#         char_count = {}
#         for ch in s:
#             if ch in char_count:
#                 char_count[ch] += 1
#             else:
#                 char_count[ch] = 1
#         return char_count
# obj = fre()
# s = "hello"
# result = obj.find_freq(s)
# print(result)


# class len:
#     def f_len(self, s):
#         count = 0
#         for i in s:
#             count += 1
#         return count
# obj = len()
# s = str(input())
# result = obj.f_len(s)
# print(result)


####----------------------------------#######

# class max_n:
#     def max_num(self,s):
#         max = s[0]
#         for i in s:
#             if i > max:
#                 max = i
#         return max
# obj = max_n()
# s = [int(i) for i in input().strip().split()]
# result = obj.max_num(s)
# print(result)

# class min_n:
#     def min_num(self,s):
#         min = s[0]
#         for i in s:
#             if i<min:
#                 min = i
#         return min
# obj = min_n()
# s = [int(i) for i in input().strip().split()]
# result = obj.min_num(s)
# print(result)

# class rev_lst:
#     def reverse_list(self,s):
#         i = len(s)-1
#         new_lst = []
#         while i>=0:
#             new_lst.append(s[i])
#             i -= 1
#         return "".join(new_lst)
# obj = rev_lst()
# s = [i for i in input().strip().split()]
# result = obj.reverse_list(s)
# print(result)


# class rem_dup:
#     def remove_dup(self,s):
#         return set(s)
# obj = rem_dup()
# s = [i for i in input().strip().split()]
# result = obj.remove_dup(s)
# print(result)


# class freq:
#     def freq_cnt(self,s):
#         char_count = {}
#         for ch in s:
#             if ch in char_count:
#                 char_count[ch] += 1
#             else:
#                 char_count[ch] = 1
#         return char_count
# obj = freq()
# s = [i for i in input().strip().split()]
# result = obj.freq_cnt(s)
# print(result)


#####------------patterns----------------#####


# class r_t:
#     def right_tri(self,s):
#         for i in range(1,s+1):
#             print("*"*i)
# obj = r_t()
# s = int(input())
# result = obj.right_tri(s)
# print(result)

# class in_t:
#     def inverted_tri(self,s):
#         for i in range(1,s+1):
#             print("*"*(s-i+1))
# obj = in_t()
# s = int(input())
# result = obj.inverted_tri(s)
# print(result)

# class sq:
#     def square(self,s):
#         for i in range(s):
#             print("*"*s)
# obj = sq()
# s = int(input())
# result = obj.square(s)
# print(result)



