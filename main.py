# Author: Matthew Jacobs
# Padder V1.0

"""
This program adds padding to images in the imgs/input folder and saves them to the imgs/output folder.
Created as a solution to aid in image processing for my business website.
"""

import sys
from PIL import Image
from os import listdir

def main(padValue=115) -> None:
    # read images from imgs/input folder
    arr = [x for x in listdir('imgs/input') if not x.startswith('.')]

    for i in range(len(arr)):
        img = Image.open('imgs/input/' + arr[i])
        img = img.convert('RGBA')
        width, height = img.size

        newWidth = width + padValue
        newHeight = height + padValue

        newImg = Image.new('RGBA', img.size, 'WHITE')
        newImg.paste(img, (0, 0), img)

        output = Image.new(newImg.mode, (newWidth, newHeight), (255, 255, 255))
        output.paste(newImg, (int(padValue/2), int(padValue/2)))

        output.save('imgs/output/' + ('p_' + arr[i]))

        img.close()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-h':
        print('Usage: python3 main.py [padding value]')
        print('Default padding value is 115')
        sys.exit(0)

    main(int(sys.argv[1])) if len(sys.argv) > 1 else main()