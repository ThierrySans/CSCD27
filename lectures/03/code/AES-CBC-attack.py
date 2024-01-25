#!/usr/local/bin/python3

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def professor(student, course, grade):
    key = b'SecFailUnivrsity'
    iv = b'0123456789ABCDEF'
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = student.encode() + course.encode() + grade.to_bytes(2, byteorder='big') + b'00000000000000'
    return cipher.encrypt(plaintext);
    
def registrar(ciphertext):
    key = b'SecFailUnivrsity'
    iv = b'0123456789ABCDEF'
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = cipher.decrypt(ciphertext);
    student = plaintext[:10].decode()
    course = plaintext[10:16].decode()
    grade = int.from_bytes(plaintext[16:18], byteorder='big')
    return student, course, grade

ciphertext = professor('0123456789', 'CSCD27', 0)
student, course, grade = registrar(ciphertext)
print(student, course, grade)

################# attack ###############

### idea: the attacker knows the ciphertext but not the key

prefix = ciphertext[:16]
suffix = get_random_bytes(16)
student, course, grade = registrar(prefix + suffix)
print(student, course, grade)

### brute-force attack

def attack(ciphertext):
    prefix = ciphertext[:16]
    while True:
        suffix = get_random_bytes(16)
        student, course, grade = registrar(prefix + suffix)
        if (80 < grade < 100):
            break
    print(student, course, grade)

attack(ciphertext)