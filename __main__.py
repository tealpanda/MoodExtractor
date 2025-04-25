# __main__.py

import sys
import os
from take_color import take_color, save_colors_to_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m color_extractor <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    output_path = os.path.splitext(image_path)[0] + '_colors.txt'

    colors = take_color(image_path)
    save_colors_to_file(colors, output_path)

    print(f"Extracted {len(colors)} colors from {image_path}.")
    print(f"Saved to {output_path}")

if __name__ == '__main__':
    main()