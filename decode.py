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


def decode_letter(pixel_array):
    output = binary_to_letter(get_binary(pixel_array))
    return output

def get_pixel_array(frame, encoded_word,start_x = 100,start_y = 100):

    pixel_array = []

    for i in range(0,len(encoded_word)*3):
        r,g,b = frame[start_x,start_y + i]
        pixel_array.extend([r,g,b])
   
    #print(f"pixel array is {pixel_array}")
    return pixel_array

   


def decode_word(encoded_word_len,frame,start_x = 100,start_y = 100):
    word = "s" * encoded_word_len
    pixel_array = get_pixel_array(frame,word,start_x,start_y)
    word_array = []
    incrementer = 9
    for i in range(0,encoded_word_len):
        to_be_modded_pixels = pixel_array[i * incrementer: i * incrementer + 9]
        word_array.extend([to_be_modded_pixels])

    output = ""
    for i in range(0,len(word_array)):
        letter = decode_letter(word_array[i])
        #print(f"Decoded letter is {letter} \n")
        output = output + letter
    
    print(f"Decoded Word is {output} \n")

    return output


def main():
    #picture = Image.open("test.jpeg", 'r')
    picture = Image.open("encoded_image.png", 'r')
    frame = picture.load()
    print("\n")
    encoded_len = int(input("What is length of password?"))
    decode_word(encoded_len,frame)
    

     

if __name__ == "__main__":
     main()
         