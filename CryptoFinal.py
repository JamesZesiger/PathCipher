import copy
from math import isqrt
import random

squares = {i: i**2 for i in range(1, 21)}
print(squares)

def RandomFill(length):
    # This function fills the input string with random ints until it reaches the specified length.
    Path = set()
    while len(Path) < length:
        Path.add(str(random.randint(0, length-1)))
    ListPath = list(Path)
    return ListPath

def List_to_Matrix(size, path):
    # This function converts a List of strings to a Matrix string.
    matrix = []
    for x in range(size):
        matrix.append([])
    for x in range(size):
        for y in range(size):
            num = path.pop(0)
            matrix[x].append(num)
    return matrix

def Encrypt_String_to_Matrix(string, matrix):
    # This function encrypts the input string using the matrix.
    char_list = list(string)
    Encrypted_String = ""
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            num = int(matrix[x][y])
            matrix[x][y] = char_list[num]
            Encrypted_String += char_list[num]
            
    return matrix, Encrypted_String

def Decrypt_String_to_Matrix(encrypted_string, matrix):
    # This function decrypts the input string using the matrix.
    char_list = list(encrypted_string)
    NumMatrix = copy.deepcopy(matrix)
    place = 0
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            matrix[x][y] = char_list[place]
            place += 1
    return matrix

def Get_String_From_Matrix(matrix, NumMatrix, length):
    # This function gets the string from the matrix.
    string = ""
    place = 0
    for num in range(length):
        for x in range(len(matrix)):
            if str(place) in NumMatrix[x]:
                for y in range(len(matrix)):
                    if NumMatrix[x][y] == str(place):
                        string += matrix[x][y]
                        place += 1
                        break

    return string

if __name__ == "__main__":
    print("What would you like to do?")
    print("1. Encrypt a string")
    print("2. Decrypt a string")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        String = input("Enter the string you wish to encrypt: ")
        FileName = input("Enter the name of the file you wish to save the encrypted string to (add the .txt extension): ")
        Str_length = len(String)
        String = String.replace(" ", "x")
        String = String.lower()
        print(f"The length of the string is: {Str_length}")
        size = 0
        for x in squares.keys():
            if squares[x] < Str_length:
                continue
            elif squares[x] == Str_length:
                print("The length of the string is a perfect square.")
                print("would you like to use the next perfect square as the size of the random string? (y/n)")
                answer = input()            
                if answer.lower() == 'y':
                    size = squares[x+1]
                if answer.lower() == 'n':
                    size = squares[x]
                break
            elif squares[x] > Str_length:
                size = squares[x]
                break
        if Str_length > squares[20]:
            print("The length of the string is too long. Please enter a string with a length of 400 or less.")
            exit()
        if Str_length < size:
            diff = size - Str_length
            for x in range(diff):
                String += "x"
        random_string = RandomFill(size)
        print(random_string)
        dims = isqrt(size)
        NumMatrix = List_to_Matrix(dims, random_string)
        CharMatrix = copy.deepcopy(NumMatrix)
        print(NumMatrix)
        Encrypted_Matrix, Encrypted_String = Encrypt_String_to_Matrix(String, CharMatrix)
        for x in range(dims):
            print(Encrypted_Matrix[x])
        print(f"Encrypted String: {Encrypted_String}")
        # Write new content (overwrites existing file)
        dict_to_write = {"Encrypted_String": Encrypted_String, "NumMatrix": NumMatrix}
        FolderName = "PathCipher"
        WriteName = f"{FolderName}/{FileName}"
        with open(WriteName, 'w') as f:
            f.write(f"{dict_to_write}")
    else:
        string = input("Enter the name of the file you wish to read the encrypted string from (add the .txt extension): ")
        FolderName = "PathCipher"
        ReadName = f"{FolderName}/{string}"
        with open(ReadName, 'r') as f:
            content = f.read()
        content = eval(content)
        String = content["Encrypted_String"]
        NumMatrix = content["NumMatrix"]
        CharMatrix = copy.deepcopy(NumMatrix)
        size = len(String)
        dims = isqrt(size)
        Decrypted_Matrix = Decrypt_String_to_Matrix(String, CharMatrix)
        for x in range(dims):
            print(Decrypted_Matrix[x])
        Decrypted_String = Get_String_From_Matrix(Decrypted_Matrix, NumMatrix, size)
        print(f"Decrypted String: {Decrypted_String}")
