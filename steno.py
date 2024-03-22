# Python program implementing Image Steganography
# Created by: Jon Barker
# Date: 11-March, 2024

from PIL import Image


# Python program to convert decimal to binary
# Function to convert Decimal number 
# to Binary number 
def decimalToBinary(n): 
	return bin(n).replace("0b", "") 

# Function to Decode a Pixel Array to Binary.
# Input: Pixel array of length 9
# Output: Binary Sequency of Pixels
def get_binary(pixel_array):
    if len(pixel_array) != 9:
         raise ValueError('Improper Input Data Format')
    
    else:
        output_str = ""
        for value in range(2,9):
        
            # If even, its 0
            if pixel_array[value] % 2 == 0:
                    output_str = output_str + "0"
            
            # If odd, append a 1
            else:
                    output_str = output_str + "1"
        
        return output_str


# Function to Decode a Binary Sequence into it's ASCII value.
# Input: Binary Sequency
# Output: ASCII Letter
def binary_to_letter(binary):
    value = int(binary,2)
    letter = chr(value)
    return letter

# Function to Encode a Pixel Array with a singular string
# Input: Input Letter, Pixel Array to be encoded
# Output: Modified Pixel Array
def encode_letter(letter,pixel_array):
    if len(pixel_array) != 9:
         raise ValueError('Improper Input Data Format')
    
    number = ord(letter)

    binary = decimalToBinary(ord(letter))

    bias = len(pixel_array) - len(binary)

    for i in range(0, len(binary)):
         
        if int(binary[i]) == 0:
            if pixel_array[i + bias] % 2 == 1:
                pixel_array[i + bias] -= 1
        else:
            if pixel_array[i + bias] % 2 == 0:
                pixel_array[i + bias] += 1

    return pixel_array


# Function to decode a letter
# Input: Pixel Array
# Output: letter
def decode_letter(pixel_array):
    output = binary_to_letter(get_binary(pixel_array))
    return output


# Function to grab a pixel array at a specific start_x and start_y
# Input: frame, word to be encoded, start_x and start y
# Output: pixel array [][] of length [9] for every letter in encoded word

def get_pixel_array(frame, encoded_word,start_x = 100,start_y = 100):

    pixel_array = []

    for i in range(0,len(encoded_word)*3):
        r,g,b = frame[start_x,start_y + i]
        pixel_array.extend([r,g,b])
   
    #print(f"pixel array is {pixel_array}")
    return pixel_array

    
# Function to encode a letter in every pixel_array
# Parses through the pixel array and encodes a single letter
# Input: Encoded Word, pixel array
# Output: Modified Pixel Array     
  
def modify_array(encoded_word,pixel_array):
    new_array = []
    incrementer = 9
    for i in range(0,len(encoded_word)):
        to_be_modded_pixels = pixel_array[i * incrementer: i * incrementer + 9]
        modded_pixels = encode_letter(encoded_word[i],to_be_modded_pixels)
        new_array.extend([modded_pixels])
        #print(f"Before:{to_be_modded_pixels} \n After:{modded_pixels} \n \n")
    return new_array


# Function to embed a word in the image
# Input: frame, modified array,start_x,start_y
# Output: Modified Pixel Array     

def encode_pixels(frame,modified_array,start_x = 100, start_y = 100):
    #print(f'Modified Array = {modified_array}')
    incrementer = 0
    for i in range(0, len(modified_array)):
        for j in range(0,len(modified_array[i]),3):
            
            (r,g,b) = modified_array[i][j],modified_array[i][j+1],modified_array[i][j+2]
            pixel = (r,g,b)
            frame[start_x ,start_y + incrementer] = pixel
            incrementer += 1
        #print(f"Letter {i + 1} Encoded")         
    return frame




def main():

    # Input Any Image
    picture = Image.open("test.jpeg", 'r')
    encoded_picture = picture.copy()
    frame = encoded_picture.load()
    
    
    encoded_word = input("What Password Would You like to Encode?: ")
    
    pixel_array = get_pixel_array(frame,encoded_word)
    print(f"Pixel Array = {pixel_array}")
    
    
    modified_array = modify_array(encoded_word,pixel_array)

    
    encoded_image = encode_pixels(frame,modified_array)
    
    #Make sure extension is lossless (.png)
    encoded_picture.save('encoded_image.png')

    

     

if __name__ == "__main__":
     main()
         