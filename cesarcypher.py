#University id=2358583
"""
This module provides a simple implementation of the Caesar Cipher encryption and decryption algorithm.
"""
def welcome():
        '''
        This function writes a welcome text
        '''
        print('Welcome to the Caesar Cipher \nThis program encrypts and decrypts text with the caesar cipher')

def enter_message():
        a = input('Would you like to encrypt (e) or decrypt (d): ')
        a = a.lower()
        if a == 'e':
            No_change_text = input('What message would you like to encrypt: ').upper()
            shift()
            changedtext = encrypt(No_change_text, shift)
            print(f'Enter text: {No_change_text}')

        elif a == 'd':
            changedtext = input('What message would you like to decrypt: ').upper()
            shift = int(input('what is the shift number:'))
            No_change_text = decrypt(changedtext, shift)
            print(f' Enter text : {No_change_text}')

        else:
            print('Invalid mode')
            enter_message()
def encrypt(plaintext, key):
    """
    Encrypt the text using the given shift key and return the resulting ciphertext
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_num = len(alphabet)
    encrypted_text = ''
    for string in plaintext:
        string = string.upper()
        if not string == ' ':
            index = alphabet.find(string)
            if index == -1:
                encrypted_text += string
            else:
                new_index = (index + key) % alphabet_num
                encrypted_text += alphabet[new_index]
        else:
            encrypted_text += ' '
    return encrypted_text

def decrypt(ciphertext, key):
    """
    Decrypt the ciphertext using the given shift key and return the resulting no change text
    """
    No_change_text = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_num = len(alphabet)
    for string in ciphertext:
        string = string.upper()
        if not string == ' ':
            index = alphabet.find(string)
            if index == -1:
                No_change_text += string
            else:
                new_index = (index - key) % alphabet_num
                No_change_text += alphabet[new_index]
        else:
            No_change_text += ' '
    return No_change_text

def another_message():
    option= input ("would you like to encrypt or decrypt another message(y/n)").lower()
    if option =='y'or 'n':
        return option
    else:
        return another_message()
         

def message_or_file():
    choice1 = input("enter (e) for encrypt or (d)for decrypt:").lower()  #changing into small letter 
    choice2 = input("enter(c) for console or (f)for file:").lower() #chnaging into small letter
    if choice1 == 'e' and choice2 == 'c':
        message = input("what message you would like to encrypt:")
        encrypt(message)
    elif choice1 == 'd' and choice2 == 'c':
        message=input("what message you would like to encrypt:")
        decrypt(message)
    elif choice1 == 'e' and choice2 == 'f':
        filename=input("enter the filename:")
        is_file(filename)
    elif choice1 == 'd' and choice2 == 'f':
        filename=input(" enter the filename:")
        is_file(filename)
    if choice2 == 'c':
        return choice1, None, message
    elif choice2 == 'f':
        return choice1 , filename, None
    else:
        message_or_file()
    
        
    
    
def is_file(file1):
    try:
        with open (file1,'r') as f:# reading 
            True
    except IOError: #excepting the IOerror
        return False

def write_message(characters):
    file3=input("enter filename:")
    with open(file3, 'w') as file2:
            for character in characters: # list traversal
                file2.write(character)
            print('File saved successfully')
   


def shift():
    shift = int(input('What is the shift number: '))
    return shift

def process_file(choice, filename, shiftnumber):
    with open(filename, 'r') as file1: # opening file to read
        temp_list = []
        if choice == 'e': # running if the choice is e
            for line in file1: # file traversal
                for character in line: # string traversal
                    temp_character = encrypt(character.upper(),shiftnumber) # calling encrypt function
                    temp_list.append(temp_character)
        else: # if choice is decryption
            for line in file1: # file traversal
                for character in line: # string traversal
                    temp_character = decrypt(character.upper(), shiftnumber) # calling decrypt function
                    temp_list.append(temp_character)
    return temp_list

def main():
    welcome()# calling welcome function
    choice, filename, message = message_or_file()
    x=shift()
    if filename is None:
        if choice == 'e':
            print(encrypt(message,x))
        elif choice =='d':
            print(decrypt(message,x))
        else:
            message_or_file()
    else:
        changed_text_list = process_file(choice, filename, x)
        write_message(changed_text_list)
        another_message()
    print("Thank you for using program, Goodbye")   

main()





