import copy
from math import isqrt
import random

squares = {i: i**2 for i in range(1, 21)}

def Int_to_Char_Matrix(matrix):
    # This function converts a matrix of ints to a matrix of chars.
    char_matrix = copy.deepcopy(matrix)
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            char_matrix[x][y] = str(matrix[x][y])
    return char_matrix

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
        while True:
            String = input("Enter the string you wish to encrypt: ")
            Str_length = len(String)
            String = String.replace(" ", "x")
            String = String.lower()
            if Str_length > squares[20]:
                print("The length of the string is too long. Please enter a string with a length of 400 or less.")
            else:
                break
        enc_file = input("Enter the name of the file to save the encrypted string (e.g., encrypted.txt): ")
        matrix_file = input("Enter the name of the file to save the matrix (e.g., matrix.txt): ")
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
        if Str_length < size:
            diff = size - Str_length
            for x in range(diff):
                String += "x"
        print("Would you like to use a random matrix as the key for the encryption? (y/n)")
        answer = input()
        answer = answer.lower()
        dims = isqrt(size)
        if answer == 'y':    
            random_string = RandomFill(size)
            print(random_string)
            NumMatrix = List_to_Matrix(dims, random_string)
        elif answer == 'n':
            while True:
                print(f"Please enter the matrix you wish to use for the encryption. (The matrix should be a square matrix of size {dims}x{dims})")
                print("Enter in the form of [[0, 1, 2], [3, 4, 5], [6, 7, 8]]")
                matrix_input = input("Enter the matrix: ")
                NumMatrix = eval(matrix_input)
                try :
                    if len(NumMatrix) != dims:
                        print(f"The matrix is not the correct size. Please enter a square matrix of size {dims}x{dims}.")
                        continue
                    for x in range(len(NumMatrix)):
                        if len(NumMatrix[x]) != dims:
                            print(f"The matrix is not the correct size. Please enter a square matrix of size {dims}x{dims}.")
                            continue
                    break
                except:
                    print("The matrix is not in the correct format or size. Please enter the matrix in the form of [[0, 1, 2], [3, 4, 5], [6, 7, 8]] with dimensions {dims}x{dims}.")
                    continue   
        CharMatrix = copy.deepcopy(NumMatrix)
        print(NumMatrix)
        Encrypted_Matrix, Encrypted_String = Encrypt_String_to_Matrix(String, CharMatrix)
        for x in range(dims):
            print(Encrypted_Matrix[x])
        print(f"Encrypted String: {Encrypted_String}")
        # Save encrypted string
        if not enc_file.endswith('.txt'):
            enc_file += '.txt'
        with open(enc_file, 'w') as f:
            f.write(Encrypted_String)
        # Save matrix
        if type(NumMatrix[0][0]) == int:
            NumMatrix = Int_to_Char_Matrix(NumMatrix)
        if not matrix_file.endswith('.txt'):
            matrix_file += '.txt'
        with open(matrix_file, 'w') as f:
            f.write(str(NumMatrix))
        print(f"Encrypted string saved to {enc_file}")
        print(f"Matrix saved to {matrix_file}")
    else:
        enc_file = input("Enter the name of the file containing the encrypted string (e.g., encrypted.txt): ")
        matrix_file = input("Enter the name of the file containing the matrix (e.g., matrix.txt): ")
        with open(enc_file, 'r') as f:
            String = f.read().strip()
        with open(matrix_file, 'r') as f:
            NumMatrix = eval(f.read())
        CharMatrix = copy.deepcopy(NumMatrix)
        size = len(String)
        dims = isqrt(size)
        Decrypted_Matrix = Decrypt_String_to_Matrix(String, CharMatrix)
        for x in range(dims):
            print(Decrypted_Matrix[x])
        Decrypted_String = Get_String_From_Matrix(Decrypted_Matrix, NumMatrix, size)
        print(f"Decrypted String: {Decrypted_String}")
