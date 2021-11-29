"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GArc
from campy.graphics.gwindow import GWindow

STAR_SIZE = 50
MOON_SIZE = 150
BUILD_HEIGHT = 500
BUILD_WIDTH = 10
BRICK_HEIGHT = 500
BRICK_WIDTH = 50

window = GWindow(900, 500)


def main():
    """
    TODO:
    """
    sky = GRect(900, 600, x=0, y=0)
    sky.filled = True
    sky.color = 'midnightblue'
    sky.fill_color = 'midnightblue'
    window.add(sky)

    winding()
    mooning()
    staring()
    mountain()
    houses()
    bricking()
    # build()


def houses():

    house = GRect(70, 75)
    house.filled = True
    house.color = 'darkgray'
    house.fill_color = 'darkgray'
    window.add(house, 650, 475)

    house = GRect(40, 75)
    house.filled = True
    house.color = 'darkgray'
    house.fill_color = 'darkgray'
    window.add(house, 700, 450)

    house = GRect(200, 75)
    house.filled = True
    house.color = 'darkgray'
    house.fill_color = 'darkgray'
    window.add(house, 700, 490)

    house = GRect(19, 100)
    house.filled = True
    house.color = 'darkgray'
    house.fill_color = 'darkgray'
    window.add(house, 310, 400)

    house = GRect(200, 75)
    house.filled = True
    house.color = 'darkgray'
    house.fill_color = 'darkgray'
    window.add(house, 400, 490)

    house = GRect(50, 75)
    house.filled = True
    house.color = 'darkgray'
    house.fill_color = 'darkgray'
    window.add(house, 325, 475)

    house = GRect(40, 75)
    house.filled = True
    house.color = 'slategray'
    house.fill_color = 'slategray'
    window.add(house, 450, 425)
    light = GRect(10, 10)
    light.filled = True
    light.color = 'yellow'
    light.fill_color = 'yellow'
    window.add(light, 465, 440)

    house = GRect(40, 75)
    house.filled = True
    house.color = 'slategray'
    house.fill_color = 'slategray'
    window.add(house, 550, 450)
    light = GRect(10, 10)
    light.filled = True
    light.color = 'yellow'
    light.fill_color = 'yellow'
    window.add(light, 565, 465)

    house = GRect(40, 75)
    house.filled = True
    house.color = 'slategray'
    house.fill_color = 'slategray'
    window.add(house, 550, 475)
    light = GRect(10, 10)
    light.filled = True
    light.color = 'yellow'
    light.fill_color = 'yellow'
    window.add(light, 565, 490)

    house = GRect(40, 75)
    house.filled = True
    house.color = 'slategray'
    house.fill_color = 'slategray'
    window.add(house, 785, 475)
    light = GRect(10, 10)
    light.filled = True
    light.color = 'yellow'
    light.fill_color = 'yellow'
    window.add(light, 800, 490)

    house = GRect(40, 75)
    house.filled = True
    house.color = 'slategray'
    house.fill_color = 'slategray'
    window.add(house, 835, 475)
    light = GRect(10, 10)
    light.filled = True
    light.color = 'yellow'
    light.fill_color = 'yellow'
    window.add(light, 850, 490)


def mountain():

    moun = GOval(300, 200)
    moun.filled = True
    moun.color = 'black'
    moun.fill_color = 'darksage'
    window.add(moun, x=654, y=400)

    moun = GOval(400, 250)
    moun.filled = True
    moun.color = 'black'
    moun.fill_color = 'darksage'
    window.add(moun, x=450, y=450)

    moun = GOval(300, 150)
    moun.filled = True
    moun.color = 'black'
    moun.fill_color = 'darksage'
    window.add(moun, x=300, y=475)

    moun = GOval(50, 300)
    moun.filled = True
    moun.color = 'black'
    moun.fill_color = 'darksage'
    window.add(moun, x=700, y=400)

    moun = GOval(50, 500)
    moun.filled = True
    moun.color = 'black'
    moun.fill_color = 'darksage'
    window.add(moun, x=850, y=350)

    moun = GOval(150, 450)
    moun.filled = True
    moun.color = 'black'
    moun.fill_color = 'darksage'
    window.add(moun, x=550, y=400)

    moun = GOval(350, 100)
    moun.filled = True
    moun.color = 'black'
    moun.fill_color = 'darksage'
    window.add(moun, x=350, y=500)


def mooning():
    moon = GOval(MOON_SIZE+50, MOON_SIZE+50)
    moon.filled = True
    moon.color = 'yellow'
    moon.fill_color = 'yellow'
    window.add(moon, x=700, y=100)
    moon = GOval(MOON_SIZE, MOON_SIZE)
    moon.filled = True
    moon.color = 'orange'
    moon.fill_color = 'orange'
    window.add(moon, x=725, y=125)
    moon = GOval(MOON_SIZE-50, MOON_SIZE-50)
    moon.filled = True
    moon.color = 'yellow'
    moon.fill_color = 'yellow'
    window.add(moon, x=780, y=135)


def staring():
    star1 = GOval(STAR_SIZE+25, STAR_SIZE+25)
    star1.filled = True
    star1.color = 'yellow'
    star1.fill_color = 'yellow'
    window.add(star1, 287.5, 237.5)
    star = GOval(STAR_SIZE, STAR_SIZE)
    star.filled = True
    star.color = 'orange'
    star.fill_color = 'orange'
    window.add(star, 300, 250)

    star2 = GOval(STAR_SIZE, STAR_SIZE)
    star2.filled = True
    star2.color = 'yellow'
    star2.fill_color = 'yellow'
    window.add(star2, 2.5, 0.5)
    star3 = GOval(STAR_SIZE-15, STAR_SIZE-15)
    star3.filled = True
    star3.color = 'orange'
    star3.fill_color = 'orange'
    window.add(star3, 10, 8)

    star2 = GOval(STAR_SIZE, STAR_SIZE)
    star2.filled = True
    star2.color = 'yellow'
    star2.fill_color = 'yellow'
    window.add(star2, -12.5, 292.5)
    star3 = GOval(STAR_SIZE-15, STAR_SIZE-15)
    star3.filled = True
    star3.color = 'orange'
    star3.fill_color = 'orange'
    window.add(star3, -5, 300)

    star4 = GOval(STAR_SIZE-10, STAR_SIZE-10)
    star4.filled = True
    star4.color = 'yellow'
    star4.fill_color = 'yellow'
    window.add(star4, 72.5, -17.5)
    star5 = GOval(STAR_SIZE-25, STAR_SIZE-25)
    star5.filled = True
    star5.color = 'orange'
    star5.fill_color = 'orange'
    window.add(star5, 80, -10)

    star6 = GOval(STAR_SIZE-10, STAR_SIZE-10)
    star6.filled = True
    star6.color = 'yellow'
    star6.fill_color = 'yellow'
    window.add(star6, 160.5, 27.5)
    star7 = GOval(STAR_SIZE-25, STAR_SIZE-25)
    star7.filled = True
    star7.color = 'orange'
    star7.fill_color = 'orange'
    window.add(star7, 168, 35)

    star = GOval(STAR_SIZE-10, STAR_SIZE-10)
    star.filled = True
    star.color = 'yellow'
    star.fill_color = 'yellow'
    window.add(star, 192.5, 192.5)
    star = GOval(STAR_SIZE-25, STAR_SIZE-25)
    star.filled = True
    star.color = 'orange'
    star.fill_color = 'orange'
    window.add(star, 200, 200)

    star8 = GOval(STAR_SIZE-20, STAR_SIZE-20)
    star8.filled = True
    star8.color = 'yellow'
    star8.fill_color = 'yellow'
    window.add(star8, 242.5, 42.5)
    star9 = GOval(STAR_SIZE-35, STAR_SIZE-35)
    star9.filled = True
    star9.color = 'orange'
    star9.fill_color = 'orange'
    window.add(star9, 250, 50)

    star8 = GOval(STAR_SIZE-20, STAR_SIZE-20)
    star8.filled = True
    star8.color = 'yellow'
    star8.fill_color = 'yellow'
    window.add(star8, 592.5, 62.5)
    star9 = GOval(STAR_SIZE-35, STAR_SIZE-35)
    star9.filled = True
    star9.color = 'orange'
    star9.fill_color = 'orange'
    window.add(star9, 600, 70)

    star = GOval(STAR_SIZE-20, STAR_SIZE-20)
    star.filled = True
    star.color = 'yellow'
    star.fill_color = 'yellow'
    window.add(star, 642.5, 92.5)
    star = GOval(STAR_SIZE-35, STAR_SIZE-35)
    star.filled = True
    star.color = 'orange'
    star.fill_color = 'orange'
    window.add(star, 650, 100)

    star = GOval(STAR_SIZE-20, STAR_SIZE-20)
    star.filled = True
    star.color = 'yellow'
    star.fill_color = 'yellow'
    window.add(star, 354, 54)

    star = GOval(STAR_SIZE, STAR_SIZE)
    star.filled = True
    star.color = 'yellow'
    star.fill_color = 'yellow'
    window.add(star, 870, 354)

    star = GOval(STAR_SIZE, STAR_SIZE)
    star.filled = True
    star.color = 'yellow'
    star.fill_color = 'yellow'
    window.add(star, 87, 135)

    star = GOval(STAR_SIZE+10, STAR_SIZE+10)
    star.filled = True
    star.color = 'yellow'
    star.fill_color = 'yellow'
    window.add(star, 350, 150)

    star = GOval(STAR_SIZE-10, STAR_SIZE-10)
    star.filled = True
    star.color = 'yellow'
    star.fill_color = 'yellow'
    window.add(star, 550, 456)

    star = GOval(STAR_SIZE-20, STAR_SIZE-20)
    star.filled = True
    star.color = 'yellow'
    star.fill_color = 'yellow'
    window.add(star, 650, 135)

    star = GOval(STAR_SIZE-35, STAR_SIZE-35)
    star.filled = True
    star.color = 'orange'
    star.fill_color = 'orange'
    window.add(star, 456, 123)

    star = GOval(STAR_SIZE-35, STAR_SIZE-35)
    star.filled = True
    star.color = 'orange'
    star.fill_color = 'orange'
    window.add(star, 423, 423)

    star = GOval(STAR_SIZE-35, STAR_SIZE-35)
    star.filled = True
    star.color = 'orange'
    star.fill_color = 'orange'
    window.add(star, 654, 198)

    star = GOval(STAR_SIZE-35, STAR_SIZE-35)
    star.filled = True
    star.color = 'orange'
    star.fill_color = 'orange'
    window.add(star, 157, 254)

    star = GOval(STAR_SIZE-35, STAR_SIZE-35)
    star.filled = True
    star.color = 'orange'
    star.fill_color = 'orange'
    window.add(star, 324, 576)


def winding():
    wind = GRect(300, 12)
    wind.filled = True
    wind.color = 'white'
    wind.fill_color = 'white'
    window.add(wind, 442, 287)
    wind = GRect(300, 12)
    wind.filled = True
    wind.color = 'skyblue'
    wind.fill_color = 'skyblue'
    window.add(wind, 550, 298)
    wind = GRect(300, 12)
    wind.filled = True
    wind.color = 'slateblue'
    wind.fill_color = 'slateblue'
    window.add(wind, 600, 320)

    wind = GRect(300, 12)
    wind.filled = True
    wind.color = 'white'
    wind.fill_color = 'white'
    window.add(wind, 150, 81)
    wind = GRect(150, 12)
    wind.filled = True
    wind.color = 'skyblue'
    wind.fill_color = 'skyblue'
    window.add(wind, 87, 17)
    wind = GRect(300, 12)
    wind.filled = True
    wind.color = 'slateblue'
    wind.fill_color = 'slateblue'
    window.add(wind, 59, 2)

    wind = GRect(156, 10)
    wind.filled = True
    wind.color = 'white'
    wind.fill_color = 'white'
    window.add(wind, 804, 420)
    wind = GRect(651, 10)
    wind.filled = True
    wind.color = 'skyblue'
    wind.fill_color = 'skyblue'
    window.add(wind, 654, 354)
    wind = GRect(456, 10)
    wind.filled = True
    wind.color = 'slateblue'
    wind.fill_color = 'slateblue'
    window.add(wind, 456, 456)

    wind = GRect(156, 10)
    wind.filled = True
    wind.color = 'white'
    wind.fill_color = 'white'
    window.add(wind, 402, 420)
    wind = GRect(651, 10)
    wind.filled = True
    wind.color = 'skyblue'
    wind.fill_color = 'skyblue'
    window.add(wind, 358, 354)
    wind = GRect(456, 10)
    wind.filled = True
    wind.color = 'slateblue'
    wind.fill_color = 'slateblue'
    window.add(wind, 135, 456)

    wind = GRect(190, 10)
    wind.filled = True
    wind.color = 'white'
    wind.fill_color = 'white'
    window.add(wind, 34, 531)
    wind = GRect(910, 10)
    wind.filled = True
    wind.color = 'skyblue'
    wind.fill_color = 'skyblue'
    window.add(wind, 15, 453)
    wind = GRect(384, 10)
    wind.filled = True
    wind.color = 'slateblue'
    wind.fill_color = 'slateblue'
    window.add(wind, 54, 165)

    wind = GRect(600, 7)
    wind.filled = True
    wind.color = 'white'
    wind.fill_color = 'white'
    window.add(wind, 435, 198)
    wind = GRect(153, 15)
    wind.filled = True
    wind.color = 'skyblue'
    wind.fill_color = 'skyblue'
    window.add(wind, 654, 513)
    wind = GRect(987, 2)
    wind.filled = True
    wind.color = 'slateblue'
    wind.fill_color = 'slateblue'
    window.add(wind, 768, 123)

    wind = GRect(600, 7)
    wind.filled = True
    wind.color = 'white'
    wind.fill_color = 'white'
    window.add(wind, 123, 453)
    wind = GRect(153, 15)
    wind.filled = True
    wind.color = 'skyblue'
    wind.fill_color = 'skyblue'
    window.add(wind, 453, 354)
    wind = GRect(987, 2)
    wind.filled = True
    wind.color = 'slateblue'
    wind.fill_color = 'slateblue'
    window.add(wind, 654, 132)

    wind = GRect(600, 7)
    wind.filled = True
    wind.color = 'white'
    wind.fill_color = 'white'
    window.add(wind, 0, 456)
    wind = GRect(153, 15)
    wind.filled = True
    wind.color = 'skyblue'
    wind.fill_color = 'skyblue'
    window.add(wind, 30, 320)
    wind = GRect(987, 30)
    wind.filled = True
    wind.color = 'slateblue'
    wind.fill_color = 'slateblue'
    window.add(wind, 45, 153)

    wind = GRect(600, 7)
    wind.filled = True
    wind.color = 'white'
    wind.fill_color = 'white'
    window.add(wind, 2, 234)
    wind = GRect(153, 15)
    wind.filled = True
    wind.color = 'skyblue'
    wind.fill_color = 'skyblue'
    window.add(wind, 12, 123)
    wind = GRect(987, 12)
    wind.filled = True
    wind.color = 'slateblue'
    wind.fill_color = 'slateblue'
    window.add(wind, 51, 435)

    wind = GRect(600, 7)
    wind.filled = True
    wind.color = 'white'
    wind.fill_color = 'white'
    window.add(wind, 750, 90)
    wind = GRect(153, 15)
    wind.filled = True
    wind.color = 'skyblue'
    wind.fill_color = 'skyblue'
    window.add(wind, 600, 20)
    wind = GRect(987, 12)
    wind.filled = True
    wind.color = 'slateblue'
    wind.fill_color = 'slateblue'
    window.add(wind, 840, 15)

    wind = GRect(156, 20)
    wind.filled = True
    wind.color = 'white'
    wind.fill_color = 'white'
    window.add(wind, 132, 317)
    wind = GRect(354, 15)
    wind.filled = True
    wind.color = 'skyblue'
    wind.fill_color = 'skyblue'
    window.add(wind, 654, 324)
    wind = GRect(715, 13)
    wind.filled = True
    wind.color = 'slateblue'
    wind.fill_color = 'slateblue'
    window.add(wind, 159, 9)

def bricking():

    brick = GRect(BRICK_WIDTH-30, BRICK_HEIGHT)
    brick.filled = True
    window.add(brick, 185, 100)

    brick = GRect(BRICK_WIDTH-20, BRICK_HEIGHT-100)
    brick.filled = True
    window.add(brick, 180, 200)

    brick = GRect(BRICK_WIDTH-5, BRICK_HEIGHT-300)
    brick.filled = True
    window.add(brick, 200, 300)

    brick = GRect(BRICK_WIDTH-5, BRICK_HEIGHT-300)
    brick.filled = True
    window.add(brick, 150, 350)

    brick = GRect(BRICK_WIDTH-5, BRICK_HEIGHT-300)
    brick.filled = True
    window.add(brick, 125, 400)

    brick = GRect(BRICK_WIDTH-5, BRICK_HEIGHT-300)
    brick.filled = True
    window.add(brick, 215, 425)


def build():

    building = GRect(BUILD_WIDTH-5, BUILD_HEIGHT)
    building.filled = True
    building.color = 'saddlebrown'
    building.fill_color = 'saddlebrown'
    window.add(building, 190, 100)

    building = GRect(BUILD_WIDTH-5, BUILD_HEIGHT-300)
    building.filled = True
    building.color = 'saddlebrown'
    building.fill_color = 'saddlebrown'
    window.add(building, 200, 300)

    building = GRect(BUILD_WIDTH-5, BUILD_HEIGHT-200)
    building.filled = True
    building.color = 'saddlebrown'
    building.fill_color = 'saddlebrown'
    window.add(building, 250, 400)

    building = GRect(BUILD_WIDTH-5, BUILD_HEIGHT-200)
    building.filled = True
    building.color = 'saddlebrown'
    building.fill_color = 'saddlebrown'
    window.add(building, 150, 400)

    building = GRect(BUILD_WIDTH-5, BUILD_HEIGHT-200)
    building.filled = True
    building.color = 'saddlebrown'
    building.fill_color = 'saddlebrown'
    window.add(building, 150, 400)


if __name__ == '__main__':
    main()
