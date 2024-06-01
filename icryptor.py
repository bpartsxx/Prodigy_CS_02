from PIL import Image
import sys
import os
import random

from termcolor import cprint 
from pyfiglet import figlet_format
from colorama import init
from itertools import cycle



def seed(img):
    random.seed(hash(img.size))

def getPixels(img):
    w, h = img.size
    pxs = []
    for x in range(w):
        for y in range(h):
            pxs.append(img.getpixel((x, y)))
    return pxs

def scrambledIndex(pxs):
    idx = list(range(len(pxs)))
    random.shuffle(idx)
    return idx

def scramblePixels(img):
    seed(img)
    pxs = getPixels(img)
    idx = scrambledIndex(pxs)
    out = []
    print("Encrypting...")
    for i in idx:
        
        out.append(pxs[i])
    return out

def unScramblePixels(img):
    seed(img)
    pxs = getPixels(img)
    idx = scrambledIndex(pxs)
    out = list(range(len(pxs)))
    cur = 0
    print("Decrypting...")
    for i in idx:
        
        out[i] = pxs[cur]
        cur += 1
    return out

def storePixels(name, size, pxs):
    outImg = Image.new("RGB", size)
    w, h = size
    pxIter = iter(pxs)
    for x in range(w):
        for y in range(h):
            outImg.putpixel((x, y), next(pxIter))
    outImg.save(name)

def main():
    img = Image.open(sys.argv[2])
    operation=sys.argv[1]
    if operation == "encrypt":
        pxs = scramblePixels(img)
        storePixels("encrypted.png", img.size, pxs)
        input("Image encrypted. Press Enter to exit") 
    elif operation == "decrypt":
        pxs = unScramblePixels(img)
        storePixels("decrypted.png", img.size, pxs)
        input("Image decrypted. Press Enter to exit") 
    else:
        sys.exit("Unsupported operation: " + operation)
        
        
        
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
cprint(figlet_format('Icryptor1.0'),
       'red', 'on_black', attrs=['bold'])
print("Welcome to Icryptor1.0 | Made by 6p@rtsXX | Prodigy CS-02\n")
print("==========================================================")

if __name__ == "__main__":
    main()
