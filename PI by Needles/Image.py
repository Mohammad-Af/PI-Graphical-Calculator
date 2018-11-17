from PIL import Image
from pathlib import Path
from math import sin, cos, radians
from Coordinate_plane import Quadrant


def create_img(theta, needle_name):
    h = 19.0
    w = 257.0
    size_w = abs(int(h * sin(radians(theta)) + w * cos(radians(theta))))
    size_h = abs(int(w * sin(radians(theta)) + h * cos(radians(theta))))
    MAX = int(max(size_w, size_h))
    src_img = Image.open("needle.ppm")
    img = src_img.convert('RGBA')
    rot = img.rotate(theta, False, True).resize((size_w, size_h))
    back = Image.new("RGBA", (MAX, MAX), None)
    back.paste(rot, ((MAX - size_w) // 2, (MAX - size_h) // 2), rot)
    back.save(needle_name)


def load_img(theta):
    needle_name = "needles/" + str(theta) + ".png"
    needle_img = Path(needle_name)

    if not needle_img.exists():
        if 90 <= theta <= 180:
            flip_img(theta, Quadrant.SECOND)
        elif 270 <= theta <= 360:
            flip_img(theta, Quadrant.FORTH)
        else:
            create_img(theta, needle_name)
    return needle_name


def flip_img(theta, quadrant):
    quadrant_angle = 180 * (quadrant.value - 1)
    name = "needles/" + str(quadrant_angle - theta) + ".png"
    path = Path(name)
    if path.exists():
        image = Image.open(name)
        image.transpose(Image.FLIP_LEFT_RIGHT).save("needles/" + str(theta) + ".png")
    else:
        create_img(quadrant_angle - theta, name)
        flip_img(theta, quadrant)
