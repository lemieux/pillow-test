# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from PIL import Image
import sys


FILE_NAME = './ferrari-01.jpg'
BASE_FILE_NAME = FILE_NAME.replace('.jpg', '-jpg')
ROTATE_FILE_NAME = '{0}-rotate-{1}.jpg'
CROP_FILE_NAME = '{0}-crop-{1}-{2}-{3}-{4}.jpg'
CROP_ROTATE_FILE_NAME = '{0}-crop-rotate-{1}-{2}-{3}-{4}-{5}.jpg'
ROTATE_COMMAND = "rotate"
CROP_COMMAND = "crop"
CROP_ROTATE_COMMAND = "crop-rotate"


def rotate(rotation):
    save_file_name = ROTATE_FILE_NAME.format(BASE_FILE_NAME, rotation)
    pil_image = Image.open(FILE_NAME)
    pil_image_crop = pil_image.rotate(rotation)
    pil_image_crop.format = "JPEG"
    pil_image_crop.layer = pil_image.layer
    pil_image_crop.quantization = pil_image.quantization
    pil_image_crop.save(save_file_name, format="JPEG",
                quality="keep", optimize=True)
    pil_image_crop.show()


def crop(x, y, width, height):
    save_file_name = CROP_FILE_NAME.format(BASE_FILE_NAME, x, y, width, height)
    pil_image = Image.open(FILE_NAME)
    pil_image_crop = pil_image.crop((x, y, x + width, y + height))
    pil_image_crop.format = "JPEG"
    pil_image_crop.layer = pil_image.layer
    pil_image_crop.quantization = pil_image.quantization
    pil_image_crop.save(save_file_name, format="JPEG",
                quality="keep", optimize=True)
    pil_image_crop.show()


def crop_rotate(x, y, width, height, angle):
    save_file_name = CROP_ROTATE_FILE_NAME.format(BASE_FILE_NAME, angle, x, y, width, height)
    pil_image = Image.open(FILE_NAME)
    pil_image = pil_image.rotate(angle)
    pil_image = pil_image.crop((x, y, x + width, y + height))
    pil_image = pil_image.resize((int(width * 0.5), int(height * 0.5)))
    pil_image.save(save_file_name)
    pil_image.show()


if __name__ == '__main__':
    arguments = sys.argv
    if len(arguments) < 2:
        print "Not enough arguments"
    else:
        command = str.lower(arguments[1])
        if command == ROTATE_COMMAND:
            if len(arguments) < 3:
                print "You need to provide an angle"
            else:
                angle = int(arguments[2])
                print "Rotation : {0} degrees".format(angle)
                rotate(angle)
        elif command == CROP_COMMAND:
            if len(arguments) < 6:
                print "You need to provide crop coordinates"
            else:
                x = int(arguments[2])
                y = int(arguments[3])
                width = int(arguments[4])
                height = int(arguments[5])
                print "Cropping : x:{0}, y:{1}, width:{2}, height:{3} ".format(x, y, width, height)
                crop(x, y, width, height)
        elif command == CROP_ROTATE_COMMAND:
            if len(arguments) < 7:
                print "You need to provide an angle and crop coordinates"
            else:
                angle = int(arguments[2])
                x = int(arguments[3])
                y = int(arguments[4])
                width = int(arguments[5])
                height = int(arguments[6])
                print "Cropping and rotate : x:{0}, y:{1}, width:{2}, height:{3} / angle :{4} ".format(x, y, width, height, angle)
                crop_rotate(x, y, width, height, angle)
