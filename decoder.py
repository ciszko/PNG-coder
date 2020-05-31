from PIL import Image
import random
import string
import math
import io


def to_flat_list(input):
    return [item for sublist in input for item in sublist]

def img_to_list(img):
    img = Image.open(img)
    triplets = list(img.getdata())
    return to_flat_list(triplets)

def decode(message, key):
    message = img_to_list(message)
    key = img_to_list(key)

    key_len = key[0] + key[1] + key[2]

    key = key[3:]

    lol = ''
    for i in range(len(message)):
        lol += str(chr((message[i] - key[i%key_len])%255) )

    file = io.open('decoded.txt', 'w', encoding='utf-8')
    file.writelines(lol)


print("Upewnij się, że w tym folderze znajduje się plik coded.png oraz key.png")
input("Nacisnij ENTER")

try:
    decode('coded.png', 'key.png')
except Exception as ex:
    print(ex)

input("Udało się odkodować wiadomość")