# QUESTION 2: MAKE AN ENCRYPTION AND DECRYPTION PROGRAM USING CAESAR CYPHER METHOD

#ENCRYPTION
def caesar_cipher_encrypt(original_sentence):

    encrypted_string = ""

    for i in original_sentence:
        ascii_code = ord(i)
        ascii_code += 3
        encrypted = chr(ascii_code)
        encrypted_string += encrypted

    return encrypted_string


my_sentence = input("Enter the sentence here that you want to encrypt: ")
encrypted_string = caesar_cipher_encrypt(my_sentence)
print(encrypted_string)


#DECRYPTION
def caesar_cypher_decrypt(original_sentence):

    decrypted_result = ""
    for i in original_sentence:
        ascii_code1 = ord(i)
        ascii_code1 -= 3
        decrypted = chr(ascii_code1)
        decrypted_result += decrypted

    return decrypted_result


my_sentence1 = input("Enter the sentence here that you want to decrypt: ")
decrypted_result = caesar_cypher_decrypt(my_sentence1)
print(decrypted_result)