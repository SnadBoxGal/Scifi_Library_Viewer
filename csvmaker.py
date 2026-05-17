FileName = "library.csv"

# All Shelf Codes follow the format of XX-Y-Z or XX-Y
# XX refers to the shelf, it is always the letter I or O followed by a number (I1, I2, O3), 0 is not a valid number
# Y refers to the shelf, it is always a letter
# Z refers to wheter the item is at the front or back of a shelf. It can be empty if a shelf is not double stacked
# Z is always the letter F or B 

def validate_shelf_code(shelf_code):
    length = len(shelf_code)
    if not (length == 4 or length == 6):
        return False
    if shelf_code[0] not in ("I","O"):
        return False
    if not shelf_code[1].isdigit():
        return False
    if not shelf_code[2] == "-":
        return False
    if not shelf_code[3].isalpha():
        return False
    if length == 6:
        if not shelf_code[4] == "-":
            return False
        if shelf_code[5] not in ("F","C"):
            return False
    return True


def add_item(name,ISBN,location): 
    if not(len(ISBN) == 10 or len(ISBN) == 13):
        print("ISBN is not 10 or 13 digits long. Try again")
        return
    
    if not validate_shelf_code(location):
        print("Shelf Code not valid, please try again")
        return
    
    with open(FileName,"a") as f:
        f.write(f"{name},{ISBN},{location}\n")
    print(name + " Got added successfully")


while True:
    A = input("Book Name:")
    B = input("ISBN:")
    C = input("Shelf Code:")
    add_item(A,B,C)