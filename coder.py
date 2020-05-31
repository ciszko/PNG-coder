from PIL import Image
import random
import string
import math

def create_key(key_len):
    img_size = int(math.sqrt(key_len//3) + 1)
    key_img = Image.new('RGB', (img_size, img_size))
    data = [create_first_triplet(key_len)]

    randomness = [random.randint(0, 255) for _ in range((img_size**2) * 3 - 3)]
    [x,y,z] = data[0]
    to_return = [x, y, z] + randomness

    triplets = into_triplets(to_return)

    key_img.putdata(triplets)
    key_img.save('key.png')
    return to_return

def constrain(min_val, max_val, val):
    return (min(max_val, max(min_val, val)))

# creates first triples that indicates the key lenght
def create_first_triplet(key_len):
    bottom = 0
    if key_len > 255:
        if key_len < 255*2:
            bottom = key_len - 255
        elif key_len < 255*3:
            bottom = key_len - 255*2
        else:
            key_len = key_len % (3*255)
    first   = random.randint(0, constrain(bottom, 255, key_len))

    if key_len - first > 255:
        second = random.randint(min((key_len - first - 255), 255), 255)
    else:
        second  = random.randint(0, key_len - first)
    third   = key_len - first - second
    return((first, second, third))

def to_ascii(lett):
    try:
        _ = ord(lett)
        return _
    except IndexError:
        return int(0)

def into_triplets(data):
    triplets = []
    for i in range(0, len(data)//3):
        triplets.append(tuple(data[3*i : 3*i + 3]))
    return triplets

def code_message(message, len_):
    original_key = create_key(len_)
    key_len = original_key[0] + original_key[1] + original_key[2]

    key = original_key[3:]
    coded = []
    mess = []

    
    for i in range(0,  len(message)):
        mess.append((ord(message[i])))

    u_lenght = len(message)
    img_size = int(math.sqrt(u_lenght//3) + 1)
    coded_img = Image.new('RGB', (img_size, img_size))  

    for i in range(0,  len(message)):
        coded.append((mess[i] + key[(i % key_len) ])%255)

    if (len(coded) % 3 == 1):
        for i in range(len(message) , ((img_size**2)*3)+1):
            coded.append(random.randint(0, 255))
    elif (len(coded) % 3 == 2):
        for i in range(len(message) , ((img_size**2)*3)+2):
            coded.append(random.randint(0, 255))     
    else:           
        for i in range(len(message) , ((img_size**2)*3)):
            coded.append(random.randint(0, 255))


    triplets = into_triplets(coded)

    coded_img.putdata(data = triplets)
    coded_img.save('coded.png')    



print("Aby zakodować wiadomość umieść jej treść w pliku message.txt")
print("BEZ POLSKICH ZNAKÓW")

g = int(input("Podaj długość klucza (max 3*255):"))

try:
    utf8_text=open('message.txt','r+').read()

    code_message(utf8_text, g)
except Exception as ex:
    print(ex)

print("Coded.png -> zakodowana wiadomość")
print("Key.png -> klucz")
input("Naciśnij ENTER aby wyjść z programu")
