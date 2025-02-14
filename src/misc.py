import matplotlib.pyplot as plt
import cv2

def get_distinct_colors(n: int):
    cmap = plt.cm.get_cmap('tab20', n)
    cmap = [cmap(i) for i in range(n)] 

    def rgba_to_hex(r, g, b, a):
        return "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))
    
    hex_colors = [rgba_to_hex(r, g, b, a) for (r, g, b, a) in cmap]

    return hex_colors

def vconcat_resize(img_list, interpolation  
                   = cv2.INTER_CUBIC): 
    w_min = min(img.shape[1]  
                for img in img_list) 
      
    im_list_resize = [cv2.resize(img, 
                      (w_min, int(img.shape[0] * w_min / img.shape[1])), 
                                 interpolation = interpolation) 
                      for img in img_list] 
    return cv2.vconcat(im_list_resize) 