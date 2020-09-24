import math
import string

import matplotlib.pyplot as plt

# message_1 = "I m having work"
#
# print(len(message_1))
# #function for filtering messages to get only a-z small alphabets
# # def filter(message):
# #     message = message.lower()
# #
# #     new = ""
# #     for i in range(len(message)):
# #         if message[i] in string.ascii_lowercase:
# #             new += message[i]
# #     return new
#
# # function to get a key from a given dictionary value
# def get_key(the_dict,value):
#     for i,j in the_dict.items():
#         if j == value:
#             return i
#
# # defining a tree
# class Node:
#     #defining constructor
#     def __init__(self,key):
#         self.value = key
#         self.left = None
#         self.right = None
#         self.character = None
#
# class codes:
#     def __init__(self):
#         self.frequency = None
#         self.code = None
#         self.character = None
#
# # formation of a tree
# def tree_creation(char_occur_list : list):
#     # forming nodes for each element in the list
#     print('im here')
#     print(char_occur_list)
#     char_occur_list = list(Node(char_occur_list[i]) for i in range(len(char_occur_list)))
#
#     while len(char_occur_list) != 0:
#         if len(char_occur_list) > 1:
#             min1 = Node(math.inf)
#             for i in range(len(char_occur_list)):
#                 if char_occur_list[i].value < min1.value:
#                     min1 = char_occur_list[i]
#                     index = i
#             char_occur_list.pop(index)
#
#             min2 = Node(math.inf)
#             for i in range(len(char_occur_list)):
#                 if char_occur_list[i].value < min2.value:
#                     min2 = char_occur_list[i]
#                     index = i
#             char_occur_list.pop(index)
#
#             neww = Node(min1.value + min2.value)
#             if min1.value < min2.value:
#                 neww.left = min1
#                 neww.right = min2
#             else:
#                 neww.right= min1
#                 neww.left = min2
#             char_occur_list.append(neww)
#         else:
#             root = char_occur_list[0]
#             break
#
#     return root
#
# #function for printing inorder of a binary tree
# def inorder_tree(root):
#     if root != None:
#         print(root.value, end=" ")
#         inorder_tree(root.left)
#         inorder_tree(root.right)
#
# # function to get the path to the leaf
# def gimme_code(root,code_list,code):
#     if root:
#         if root.left == None and root.right==None:
#             c = codes()
#             c.frequency = root.value
#             c.code = code
#             c.character = root.character
#
#             code_list.append(c)
#         gimme_code(root.left, code_list, code+'0')
#         gimme_code(root.right, code_list, code+'1')
#
#
# # THE MAIN!
# if __name__ == '__main__':
#     timez = []
#     costz = []
#     #filtering messages
#     # message_1 = filter(message_1)
#     # message_2 = filter(message_2)
#
#     #------------------------------------- Huffman -------------------------------------
#     start_time = timeit.default_timer()
#
#     # creating a dictionary { character : total no. of times that character occured}
#
#     frequency_table = {i: message_1.count(i) for i in set(message_1)}
#     print(frequency_table)
#
#     # sorting the dictionary w.r.t total no. of times any character occured
#     frequency_table = { i: get_key(frequency_table, i) for i in sorted(frequency_table.values()) }
#     print(frequency_table)
#
#     #list of character occurences
#     char_occur_list = []
#     for i, j in frequency_table.items():
#         char_occur_list.append(i)
#     print('looooooooooooooool')
#     print(char_occur_list)
#     #forming the tree with no. of occurences of characters
#     root = tree_creation(char_occur_list)
#
#     print('Inorder of the tree: ',end="")
#     inorder_tree(root)
#     print('\n')
#
#     #formulating the binary code of each letters occurence
#     code_list = []
#     code = ""
#     gimme_code(root, code_list, code)
#
#     #the value table and cost caalculation
#     print('THE VALUE TABLE')
#     cost = 0
#     for i in range(0,len(code_list)):
#         print(code_list[i].character, end=" ")
#         print(":",end=" ")
#         print(code_list[i].code)
#
#     costz.append(cost)
#     print('The Cost with Huffman Coding: {}'.format(cost))
#
#     end_time = timeit.default_timer()
#     time_taken = end_time - start_time
#     timez.append(time_taken)
#
#     # ------------------------------------- Ascii -------------------------------------
#
#     start_time = timeit.default_timer()
#
#     cost = len(message_1) * 8
#
#     costz.append(cost)
#     print('The Cost with Ascii: {}'.format(cost))
#
#     end_time = timeit.default_timer()
#     time_taken = end_time - start_time
#     timez.append(time_taken)
#
#     # ------------------------------------- 5 bit -------------------------------------
#
#     start_time = timeit.default_timer()
#
#     lib = { character : index for index, character in enumerate(string.ascii_lowercase) }
#
#     frequency_table = {i: message_1.count(i) for i in set(message_1)}
#
#     cost = 0
#     for i,j in frequency_table.items():
#         cost += j * 5
#
#     cost += len(frequency_table) * 8
#
#     costz.append(cost)
#     print('The Cost with 5 bit: {}'.format(cost))
#
#     end_time = timeit.default_timer()
#     time_taken = end_time - start_time
#     timez.append(time_taken)


    #the GRAPH
costsss = [2379,2491,3112]
timeee = [9,  1, 1]
costsss2 = [ 1648,1810,1248]
timeee2 = [6,  1, 0]
costsss3 = [ 38064,37365,6680]
timeee3 = [7,  1, 1]
print("-------GRAPH-------")
plt.scatter(costsss[0], timeee[0], label='Huffman Coding')
plt.scatter(costsss[1], timeee[1], label='5-bit')
plt.scatter(costsss[2], timeee[2], label='ASCII')
plt.scatter(costsss2[0], timeee2[0], label='Huffman Coding')
plt.scatter(costsss2[1], timeee2[1], label='5-bit')
plt.scatter(costsss2[2], timeee2[2], label='ASCII')
plt.scatter(costsss3[0], timeee3[0], label='Huffman Coding')
plt.scatter(costsss3[1], timeee3[1], label='5-bit')
plt.scatter(costsss3[2], timeee3[2], label='ASCII')
plt.xlabel('Cost')
plt.ylabel('Time (in ms)')
plt.title('GRAPH')
plt.legend()
plt.show()

















