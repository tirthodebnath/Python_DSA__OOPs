# A = ['t','u','t','o','r','i','a','l']
# for i in range(len(A)):
#    min_= i
#    for j in range(i+1, len(A)):
#       if A[min_] > A[j]:
#          min_ = j
#    #swap
# A[i], A[min_] = A[min_], A[i]
# # main
# for i in range(len(A)):
#    print(A[i])


###################################################################

# def decrypt_1(encrypted, key, alpha):
#     key_after = key[2]
#     original =[]
#     #print(key_after)
#     key_position = alpha.find(key_after)
#     #print(key_position)
#     for i in list(encrypted):
#         #print(i)
#         if i in alpha:
#             rotating_str = alpha.find(i)
#             encrtypt_position =(rotating_str-key_position)
#             if encrtypt_position >= 0:
#                 org_str = alpha[encrtypt_position]
#                 original.append(org_str)
#             else:
#                 #encrtypt_position < 0:
#                 org_str2 = alpha[encrtypt_position]
#                 original.append(org_str2)
#         else:
#             original.append(i)
#         original1 = ' '.join(original)
#     return original1

# alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# d = decrypt_1('LV wKLV D WHVW?', 'a:D', alpha)
# print

################################################################

 