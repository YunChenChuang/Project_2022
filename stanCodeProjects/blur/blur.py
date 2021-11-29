"""
File: blur.py
Name: AO Chuang
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(old_img):
    """
    :param old_img: SimpleImage, the original image
    :return blurred_img: SimpleImage, the blurred image
    """
    blurred_img = SimpleImage.blank(old_img.height, old_img.width)  # a new image with the same size as 'old_img'

    for x in range(old_img.height):
        for y in range(old_img.width):
            red_sum = 0  # the summation of red pixel of pixels in the given range
            green_sum = 0  # the summation of green pixel of pixels in the given range
            blue_sum = 0  # the summation of blue pixel of pixels in the given range
            count = 0  # counting the number of the pixel in the range
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x + i
                    pixel_y = y + i
                    if 0 <= pixel_x < old_img.height:  # pixels out of the image range will not included
                        if 0 <= pixel_y < old_img.width:
                            pixel = old_img.get_pixel(pixel_x, pixel_y)
                            red_sum += pixel.red
                            green_sum += pixel.green
                            blue_sum += pixel.blue
                            count += 1
            blurred_pixel = blurred_img.get_pixel(x, y)
            blurred_pixel.red = red_sum / count
            blurred_pixel.green = green_sum / count
            blurred_pixel.blue = blue_sum / count
    return blurred_img


def main():
    """
    This program will blur the given image
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
