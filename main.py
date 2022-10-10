import pygame
from sys import exit
from Situation import Situation


def main():
    study_library = Situation("Hey", "img_40")
    study_library.show_text()


if __name__ == '__main__':
    main()