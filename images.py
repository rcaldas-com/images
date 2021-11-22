#!/bin/env python3
import os
from PIL import Image

for fname in os.listdir('files'):
    if fname.endswith(".jpg"):
        image = Image.open(os.path.join('files', fname))
        image.thumbnail(size=(1620,1620))
        image.save(os.path.join('files', fname), optimize=True, quality=60)
