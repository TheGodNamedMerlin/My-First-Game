import pygame as pg, os


def load_options():
    options = []
    with open("data/resources/options.txt","r") as file:
        for line in file:
            option, key = line.split(":")
            options.append((option, key.strip("\n")))
    return options


def load_background_images():
    pictures = []
    picture_names = os.listdir("data/resources/images/Background_images/")
    for picture in picture_names:
        pictures.append(pg.image.load("data/resources/images/Background_images/" + str(picture)))

    return pictures

def load_save_data():
    save_data = []
    with open("data/resources/save_data","r") as file:
        for line in file:
            name, place = line.split(":")
            save_data.append((name, place.strip("\n")))
    return save_data