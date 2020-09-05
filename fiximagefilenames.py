import magic
import os
extensions = {'.jpg', '.jpeg'}
mime = magic.Magic(mime=True)
image_dir="./simple_images/"
for root, dirs, files in os.walk(image_dir):
    for file in files:
        file_type = mime.from_file(os.path.join(root, file))  # checks file data instead of name to typecheck
        file_extension = f'.{file_type.split("/")[1]}'
        if file_extension not in extensions:
            print(f"{file} is not a JPEG!!!!")
            os.remove(os.path.join(root, file))