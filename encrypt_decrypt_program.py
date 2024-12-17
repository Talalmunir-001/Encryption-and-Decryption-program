# QUESTION 2: MAKE AN ENCRYPTION AND DECRYPTION PROGRAM USING CAESAR CYPHER METHOD

# FUNCTION FOR ENCRYPTION
def caesar_cipher_encrypt(original_sentence):

    encrypted_string = ""

    for i in original_sentence:
        ascii_code = ord(i)
        ascii_code += 3
        encrypted = chr(ascii_code)
        encrypted_string += encrypted

    return encrypted_string


# FUNCTION FOR DECRYPTION
def caesar_cypher_decrypt(original_sentence):

    decrypted_result = ""
    for i in original_sentence:
        ascii_code1 = ord(i)
        ascii_code1 -= 3
        decrypted = chr(ascii_code1)
        decrypted_result += decrypted

    return decrypted_result


print("Select one of these \nWrite 1 for Encryption \nWrite 2 for Decryption")
selection = input("Enter your selection here: ")
