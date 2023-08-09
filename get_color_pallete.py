import requests
from PIL import Image
import collections


def get_most_common_colors(image_url, n):
    # Download the image using requests
    response = requests.get(image_url, stream=True)
    response.raise_for_status()

    # Open the image using PIL
    img = Image.open(response.raw).convert("RGB")

    # Resize the image for faster processing (optional)
    img = img.resize((100, 100))

    # Convert the image to a list of RGB tuples
    rgb_values = list(img.getdata())

    # Count the occurrences of each color
    color_counter = collections.Counter(rgb_values)

    # Get the most common colors (n most common)
    most_common_colors = color_counter.most_common(n)

    # Convert RGB tuples to hexadecimal color codes
    hex_most_common_colors = [f'#{r:02x}{g:02x}{b:02x}' for (r, g, b), _ in most_common_colors]

    return hex_most_common_colors


# Replace 'image_url' with the actual image URL and 'n' with the desired number of most common colors
image_url = 'https://i.pinimg.com/564x/43/7c/70/437c70a45773b840b041546480980a7b.jpg'
n = 10
most_common_colors = get_most_common_colors(image_url, n)
print("Most common colors:", most_common_colors)
