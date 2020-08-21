import math
import string

message_1 = "In computer science, a Huffman Code is a particular type of optimal prefix code that " \
            "is commonly used for lossless data compression. The process of finding or using such a code" \
            "proceeds by means of Huffman coding, an algorithm developed by David A. Huffman while he was a Sc.D. " \
            "student at MIT, and published in the 1952 paper, A method for the construction of Minimum-Redundancy Codes."

message_2 = "abbcccddddeeeeeffffff"

#function for filtering messages to get only a-z small alphabets
def filter(message):
    message = message.lower()

    new = ""
    for i in range(len(message)):
        if message[i] in string.ascii_lowercase:
            new += message[i]
    return new

#function to get a key from a given dictionary value
def get_key(the_dict,value):
    for i,j in the_dict.items():
        if j == value:
            return i

#defining a tree
class Node:
    #defining constructor
    def __init__(self,key):
        self.value = key
        self.left = None
        self.right = None

#formation of a tree
def tree_creation(char_occur_list : list):
    #forming nodes for each element in the list
    char_occur_list = list(Node(char_occur_list[i]) for i in range(len(char_occur_list)))

    while len(char_occur_list) != 0:
        if len(char_occur_list) > 1:
            min1 = Node(math.inf)
            for i in range(len(char_occur_list)):
                if char_occur_list[i].value < min1.value:
                    min1 = char_occur_list[i]
                    index = i
            char_occur_list.pop(index)

            min2 = Node(math.inf)
            for i in range(len(char_occur_list)):
                if char_occur_list[i].value < min2.value:
                    min2 = char_occur_list[i]
                    index = i
            char_occur_list.pop(index)

            neww = Node(min1.value + min2.value)
            if min1.value < min2.value:
                neww.left = min1
                neww.right = min2
            else:
                neww.right= min1
                neww.left = min2
            char_occur_list.append(neww)
        else:
            root = char_occur_list[0]
            break

    return root

#function for printing inorder of a binary tree
def inorder_tree(root):
    if root != None:
        print(root.value, end=" ")
        inorder_tree(root.left)
        inorder_tree(root.right)

#function to get the path to the leaf
def gimme_code(root,code_list,code):
    if root:
        if root.left == None and root.right==None:
            code_list.update({root.value : code})
        gimme_code(root.left, code_list, code+'0')
        gimme_code(root.right, code_list, code+'1')


#THE MAIN!
if __name__ == '__main__':
    #filtering messages
    message_1 = filter(message_1)
    message_2 = filter(message_2)


    # creating a dictionary { character : total no. of times that character occured}
    frequency_table = {i: message_1.count(i) for i in set(message_1)}

    # sorting the dictionary w.r.t total no. of times any character occured
    frequency_table = { i: get_key(frequency_table, i) for i in sorted(frequency_table.values()) }
    print(frequency_table)

    #list of character occurences
    char_occur_list = [ item for item in frequency_table.keys() ]

    #forming the tree with no. of occurences of characters
    root = tree_creation(char_occur_list)

    print('Inorder of the tree: ',end="")
    inorder_tree(root)
    print('/n')

    #formulating the binary code of each letters occurence
    code_list = {}
    code = ""
    gimme_code(root, code_list, code)

    #the value table and cost caalculation
    print('THE VALUE TABLE')
    cost = 0
    for i, j in frequency_table.items():
        print(j+"       :"+code_list[i])
        cost += (i * len(code_list[i]))
    print('The Cost with Huffman Coding: {}'.format(cost))




















