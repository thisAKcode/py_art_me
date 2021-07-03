# https://www.youtube.com/watch?v=XSgerkCVbFc

import cairo, PIL, argparse, math, random
from PIL import Image, ImageDraw

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", help="Specify Width", default=3000, type=int)
    parser.add_argument("--height", help="Specigy Height", default=2000, type=int)
    parser.add_argument("")
