# https://www.youtube.com/watch?v=v_raWlX7tZY&list=UUxVRDu9ujwOrmDxu72V3ujQ
import PIL
from pathlib import Path

from PIL import Image

# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# path separator on Windows
test2 = 'C:/py_art_me/project2/Capture.JPG'

image = Image.open(test2)
width, height = image.size
print(width)
print(height)
print(599/710)

def setsize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width 
    ratio = height / width / 1.65 # # maintain the aspect ratio
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image) #(100,84)
print(setsize_image(image, new_width=100).size)


# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

def main(new_width=100):
    # attempt to open image from user-input
    #path = input("Enter a valid pathname to an image:\n")
    # attempt to open image from hard coded thing
    path = test2
    try:
        image = Image.open(path)
    except:
        print(path, " is not a valid pathname to an image.")
        return
    
    
# convert image to ascii    
    new_image_data = pixels_to_ascii(grayify(setsize_image(image)))
    
    # format
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    # print result
    print(ascii_image)
    
    # save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
 
# run program
main()