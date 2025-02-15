import matplotlib.pyplot as plt
from cv2 import imread, vconcat, imwrite
from os import remove

def get_distinct_colors(n: int):
    cmap = plt.cm.get_cmap('tab20', n)
    cmap = [cmap(i) for i in range(n)] 

    def rgba_to_hex(r, g, b, a):
        return "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))
    
    hex_colors = [rgba_to_hex(r, g, b, a) for (r, g, b, a) in cmap]

    return hex_colors

def concat_images(names: list[str], savePath: str = "untitled", cleanup: bool = True):
    images = [imread(f'./img/{name}') for name in names]
    output = vconcat(images)
    imwrite(f'./img/{savePath}', output)
    if cleanup:
        for name in names:
            file_path = f'./img/{name}'
            remove(file_path)