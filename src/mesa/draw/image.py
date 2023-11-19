import pygame as pg


def load_image(path):
    return pg.image.load(path).convert_alpha()


def resize(image, size):
    return pg.transform.smoothscale(image, size)
