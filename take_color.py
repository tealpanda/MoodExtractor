# take_color.py

from PIL import Image

def take_color(image_path):
    """Extracts all RGB pixel values from an image and returns them as a list of tuples."""
    img = Image.open(image_path).convert('RGB')
    return list(img.getdata())

def save_colors_to_file(colors, output_path):
    """Saves a list of (R, G, B) color tuples to a text file, one per line."""
    with open(output_path, 'w') as f:
        for color in colors:
            f.write(f"{color}\n")