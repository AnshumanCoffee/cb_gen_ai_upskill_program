import os
import re

def get_unique_filename(target_folder, filename):
    base_name, extension = os.path.splitext(filename)
    counter = 1
    unique_filename = filename

    while os.path.exists(os.path.join(target_folder, unique_filename)):
        pattern = r"(.+)_\d+$"
        match = re.match(pattern, base_name)
        if match:
            base_name = match.group(1)
        unique_filename = f"{base_name}_{counter}{extension}"
        counter += 1

    return unique_filename
