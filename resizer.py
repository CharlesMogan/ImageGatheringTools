import os
from PIL import Image


def resize_image(src_img, size=(299, 299), bg_color="white"):
    src_img.thumbnail(size, Image.ANTIALIAS)
    new_image = Image.new("RGB", size, bg_color)
    new_image.paste(src_img, (int((size[0] - src_img.size[0]) / 2), int((size[1] - src_img.size[1]) / 2)))
    return new_image


for root, dirs, files in os.walk("./simple_images"):
    for directory in dirs:
        os.makedirs(os.path.join("./resized_images3", directory),exist_ok=True)
        for root2, dirs2, files2 in os.walk(os.path.join(root,directory)):
            for file in files2:
                print(os.path.join(root2,file))
                og_image = Image.open(os.path.join(root2, file))
                resized_image = resize_image(og_image)
                resized_image.save(os.path.join("./resized_images3", directory, file))


