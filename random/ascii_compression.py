message_1 = "In computer science, a Huffman Code is a particular type of optimal prefix code that " \
            "is commonly used for lossless data compression. The process of finding or using such a code" \
            "proceeds by means of Huffman coding, an algorithm developed by David A. Huffman while he was a Sc.D. " \
            "student at MIT, and published in the 1952 paper Amethod for the construction of Minimum-Redundancy Codes."


binary_equivalent = ''.join( format( message_1[i] , 'b') for i in message_1)


if __name__ == '__main__':
