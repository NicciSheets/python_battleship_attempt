import string

def create_rows():
    rows = int(input("How many rows would you like on the board: "))
    return list(string.ascii_uppercase)[0:rows]


def createList(r1, r2): 
    return list(range(r1, r2+1)) 
      

def create_columns():
    columns = int(input("How many columns would you like on the board: "))
    r1, r2 = 1, columns
    return createList(r1, r2)



# print(create_rows())
# print(create_columns())



    