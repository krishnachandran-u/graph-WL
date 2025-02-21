import matplotlib.pyplot as plt
import cv2
import os
import numpy as np

def get_distinct_colors(n: int):
    cmap = plt.cm.get_cmap('tab20', n)
    cmap = [cmap(i) for i in range(n)] 

    def rgba_to_hex(r, g, b, a):
        return "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))
    
    hex_colors = [rgba_to_hex(r, g, b, a) for (r, g, b, a) in cmap]

    return hex_colors

from PIL import Image

def concat_images(img_names: list[str], direction: str = "h", save_path: str = "concatenated_image.jpg", cleanup: bool = True):
    images = [Image.open(f'./img/{img_name}') for img_name in img_names]

    max_width = max(img.width for img in images)
    max_height = max(img.height for img in images)

    if direction == "h":  
        new_width = sum(img.width for img in images)
        new_height = max_height
    elif direction == "v": 
        new_width = max_width
        new_height = sum(img.height for img in images)
    else:
        raise ValueError("Direction must be 'h' (horizontal) or 'v' (vertical)")

    new_image = Image.new("RGB", (new_width, new_height), "white")

    offset = 0
    for img in images:
        if direction == "h":
            new_image.paste(img, (offset, (max_height - img.height) // 2))  
            offset += img.width
        else:
            new_image.paste(img, ((max_width - img.width) // 2, offset))  
            offset += img.height

    new_image.save(f"./img/{save_path}")

    if cleanup:
        for img_name in img_names:
            os.remove(f'./img/{img_name}')
    
    return new_image
