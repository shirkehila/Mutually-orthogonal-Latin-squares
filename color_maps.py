def index_to_hex_color(index):
    # Define a mapping of index values to hex color values
    color_map = _generate_color_map(COLORS)
    return color_map.get(index, '#000000')


def _generate_color_map(list_of_colors):
    return {
        i: list_of_colors[i] for i in range(len(list_of_colors))
    }


COLORS = ['#007c84', '#bbe0ce', '#f7a08c', '#587c7c', '#003f5e', '#fedcc1', '#e8d666', '#9ea615', '#f1573f']

color_map_1 = {
    0: '#D0CFCD',  # Red
    1: '#88A29B',  # Yellow
    2: '#55A69F',  # Green
    3: '#016970',  # Blue
    4: '#02555E',  # Dark Blue
    5: '#DD9984',  # Orange
    6: '#C1806C',  # Magenta
    7: '#966552',  # Teal
    8: '#4C3D37',  # Purple
}
