# PNG-coder
Algorithm for coding messages into PNG

## Usage

### Coding
Run coder.py for instructions
### Decoding
Script will try to find coded.png file and the output will be produced as decoded.txt. Both coded.png and key.png must be in the same directory.

## How is it working?
The algorithm uses RGB and pixels as a list to store next characters in a message. It supports first 255 ASCII characters. Each symbol is represented as each value  of RGB in a pixel.  For example having written "UwU" would result in ![#557755](https://via.placeholder.com/15/557755/000000?text=+) `rgb(85,119,85)`. Firstly, the random key of given lenght  is being generated. The very first pixel of the key indicates the lenght of it. Basically it's a sum of RGB values. Next key characters are coded in RGB values. If key lenght will not result in perfectly square image then the rest of it is generated randomly to compose a square PNG. Message is being coded by summing individual key values with message characters.  
