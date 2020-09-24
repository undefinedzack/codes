import numpy as np

print('-------TRANSPOSITION CIPHER-------')
text = str(input("Enter the text"))

rows = int(input('Rows? '))
columns = int(input('Columns? '))

matrix = [ [-99 for i in range(columns)] for j in range(rows)]
print(matrix)
if len(text) > (rows*columns):
    print('error : insufficient matrix size')
else:
    knt = 0
    for h in range(rows):
        for k in range(columns):
            matrix[h][k] = text[knt]
            knt += 1
            if knt == len(text):
                break
        if knt == len(text):
            break
    print(matrix)
    matrix = np.transpose(matrix)
    print(matrix)

    