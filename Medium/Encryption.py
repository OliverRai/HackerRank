import math
import os
import random
import re
import sys

def encryption(s):
    s = re.sub('\s+', '', s)
    stringlen = len(s)
    root = math.sqrt(stringlen)
    row = math.floor(root)
    column = math.ceil(root)
    while row*column < stringlen:
        if row >= column:
            column += 1
        else:
            row += 1
    modulo = row*column - stringlen
    s = s + ' '*modulo
    matrix = []
    i = 0
    for _ in range(row):
        matrix.append(s[i:i+column])
        i = i+column
    parsedmatrix = list(zip(*matrix))
    finalresult = ''
    for i in parsedmatrix:
        finalresult += ''.join(i)
        finalresult += ' '
    finalresult = re.sub('\s+', ' ', finalresult)
    return finalresult
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
