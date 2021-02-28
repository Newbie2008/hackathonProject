import random
import sys

rows = input("Enter the number of rows: ")
columns = input("Enter the number of columns: ")

rows = int(rows)
columns = int(columns)

x = 0
map_arr = ['.', '1']
i = 0
while i in range(0,rows):
    if i == 0:
        for k in range(0, columns):
            sys.stdout.write("1")
    elif i == columns-1:
        for l in range(0, columns):
            sys.stdout.write("1")
    else:
        for j in range(0, columns):
            if j == 0:
                sys.stdout.write("1")
            elif j == columns-1:
                sys.stdout.write("1")
            else:
                x = random.randint(0,1)
                sys.stdout.write(map_arr[x])
    i = i+1
    print("")