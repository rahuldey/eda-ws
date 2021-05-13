import random
import uuid
import os
from io import StringIO
from PIL import Image, ImageDraw
import pandas as pd
from eda.ws.config import image_directory


class VisualizationCtrl(object):
    def __init__(self, file):
        self.file = file
        self.directory = image_directory

    def process_file(self):
        try:
            print(pd.read_csv(StringIO(str(self.file.read(), "utf8")), encoding="utf8"))

            filenames = []

            for i in range(3):
                filename = str(uuid.uuid4())
                filenames.append(f"{filename}.jpg")
                self.generate_random_image(filename, 1280, 720)

            return None, filenames
        except Exception as e:
            return str(e), None

    def generate_random_image(self, filename, width, height):
        rand_pixels = [random.randint(0, 255) for _ in range(width * height * 3)]
        rand_pixels_as_bytes = bytes(rand_pixels)

        random_image = Image.frombytes("RGB", (width, height), rand_pixels_as_bytes)

        draw_image = ImageDraw.Draw(random_image)
        draw_image.text(xy=(0, 0), text=filename, fill=(255, 255, 255))
        random_image.save(os.path.join(self.directory, f"{filename}.jpg"))
